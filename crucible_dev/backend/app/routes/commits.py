import uuid
from fastapi import APIRouter, HTTPException
from app.schemas import CommitCreate, Commit  # see below
from app.services.qdrant_client import QdrantService
from app.utils.embeddings import embed_text

router = APIRouter()
qdrant = QdrantService()


@router.post(
    "/new",
    response_model=Commit,
    status_code=201,
    summary="Create a new commit vector"
)
async def create_commit(commit: CommitCreate):
    #Embed the incoming message
    vector = embed_text(commit.message)

    #Prepare your metadata payload
    payload = commit.dict()

    #Generate a UUID for this point
    point_id = str(uuid.uuid4())

    #Store with explicit point_id, vector & payload
    try:
        qdrant.store_vector("commits", point_id, vector, payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    #Return everything back to the client
    return Commit(**payload, point_id=point_id, status="ok")