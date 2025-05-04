from fastapi import FastAPI
from app.routes.commits import router as commits_router

app = FastAPI(
    title="Crucible API",
    version="0.1.0"
)

app.include_router(commits_router, prefix="/commits", tags=["commits"])

@app.get("/")
async def health():
    return {"status": "alive"}