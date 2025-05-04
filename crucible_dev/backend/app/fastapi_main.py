from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Commit(BaseModel):
    id: str
    text: str
    timestamp: float

@app.post("/commits/new")
async def new_commit(commit: Commit):
    return {"status": "received", "commit_id": commit.id}
