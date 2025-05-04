from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.qdrant_client import QdrantService
from utils.embeddings import embed_text

router = APIRouter()

class CommitCreate(BaseModel):
    user_id: str
    message: str
    timestamp: float

qdrant = QdrantService()

@router.post("/new")
async def create_commit(commit: CommitCreate):
    vector = embed_text(commit.message)
    success = qdrant.store_vector(
        collection_name="commits",
        point_id=f"{commit.user_id}-{commit.timestamp}",
        vector=vector,
        payload={
            "user_id": commit.user_id,
            "message": commit.message,
            "timestamp": commit.timestamp
        }
    )
    if not success:
        raise HTTPException(status_code=500, detail="Failed to store commit")
    return {"status": "ok"}