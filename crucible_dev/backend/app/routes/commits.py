from fastapi import APIRouter, HTTPException
from app.schemas import CommitCreate, Commit  # see below
from app.services.qdrant_client import QdrantService
from app.utils.embeddings import embed_text

router = APIRouter()
qdrant = QdrantService()

@router.post("/new", response_model=Commit, status_code=201)
async def create_commit(commit: CommitCreate):
    vector  = embed_text(commit.message)
    payload = commit.dict()
    try:
        point_id = qdrant.store_vector("commits", vector, payload)
    except Exception as e:
        raise HTTPException(500, str(e))
    return Commit(**payload, point_id=point_id, status="ok")