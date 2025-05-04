import os
import uvicorn
from datetime import date
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field

from app.services.qdrant_client import QdrantService
from app.utils.embedder import embed_text

#Define your input and output schemas
class CommitIn(BaseModel):
    current_date: date = Field(..., description="Record creation date")
    goal_category: str = Field(..., description="High-level category for this goal")
    goal_message: str = Field(..., description="Short description of the goal")
    definition_of_done: str = Field(..., description="How we know it's done")
    due_date: date = Field(..., description="When the goal should be completed")
    username: str = Field(..., description="User submitting this goal")

class CommitOut(BaseModel):
    uuid: str = Field(..., description="Generated UUID of the stored commit")

app = FastAPI(
    title="Goals + Embeddings API",
    version="1.0.0",
    description="Submit a goal, embed its text, and store in Qdrant"
)

#Dependency to get your Qdrant client
def get_qdrant_service() -> QdrantService:
    return QdrantService()

#The pipeline endpoint
@app.post("/commits", response_model=CommitOut, status_code=201)
async def create_commit(
    commit: CommitIn,
    qdrant: QdrantService = Depends(get_qdrant_service),
):
    #User-entered data is already validated in `commit`
    #Build a single string to embed (you can adjust this)
    to_embed = " | ".join([
        commit.goal_category,
        commit.goal_message,
        commit.definition_of_done,
    ])

    #Embed it
    try:
        vector = embed_text(to_embed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding failed: {e}")

    #Insert into Qdrant (generates its own UUID)
    try:
        point_id = qdrant.store_vector(
            collection_name="commits",
            vector=vector,
            payload=commit.dict()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Qdrant write failed: {e}")

    #Return the UUID
    return CommitOut(uuid=point_id)

#simple healthcheck
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

#Allow `python app/main.py` to start the server
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )