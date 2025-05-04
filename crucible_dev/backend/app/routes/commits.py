from datetime import date
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException
from app.services.qdrant_client import QdrantService
from app.utils.embedder import embed_text

router = APIRouter(prefix="/commits", tags=["commits"])

class CommitIn(BaseModel):
    current_date: date = Field(..., description="Record creation date")
    goal_category: str = Field(..., description="High-level category for this goal")
    goal_message: str = Field(..., description="Short description of the goal")
    definition_of_done: str = Field(..., description="How we know it's done")
    due_date: date = Field(..., description="When the goal should be completed")
    username: str = Field(..., description="User submitting this goal")

class CommitOut(BaseModel):
    uuid: str

def get_qdrant_service() -> QdrantService:
    return QdrantService()

@router.post("/", response_model=CommitOut, status_code=201)
async def create_commit(
    commit: CommitIn,
    qdrant: QdrantService = Depends(get_qdrant_service),
):
    text = " | ".join([
        commit.goal_category,
        commit.goal_message,
        commit.definition_of_done,
    ])

    try:
        vector = embed_text(text)
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Embedding error: {e}")

    payload = commit.dict()

    try:
        point_id = qdrant.store_vector("commits", vector, payload)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Qdrant error: {e}")

    return CommitOut(uuid=point_id)