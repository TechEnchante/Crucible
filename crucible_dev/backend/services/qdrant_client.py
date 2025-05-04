from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
import os
import uuid

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=os.getenv("QDRANT_URL", "http://localhost:6333"),
            api_key=os.getenv("QDRANT_API_KEY", None)
        )
        self.client.recreate_collection(
            collection_name="commits",
            vectors_config={
                "vector": VectorParams(size=768, distance=Distance.COSINE)
            }
        )

    def store_vector(self, collection_name: str, vector: list, payload: dict) -> str:
        #ensure the collection exists
        existing = [c.name for c in self.client.get_collections().collections]
        if collection_name not in existing:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config={
                    "embedding": rest.VectorParams(
                        size=768,
                        distance=rest.Distance.COSINE
                    )
                }
            )

        point_id = str(uuid.uuid4())
        self.client.upsert(
            collection_name=collection_name,
            points=[{
                "id":       point_id,
                "vectors":  {"embedding": vector},
                "payload":  payload
            }]
        )
        return point_id