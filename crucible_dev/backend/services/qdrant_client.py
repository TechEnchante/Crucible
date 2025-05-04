from qdrant_client import QdrantClient
import os

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=os.getenv("QDRANT_URL", "qdrant:6333"),
            api_key=os.getenv("QDRANT_API_KEY")
        )
        self._ensure_collection()

    def _ensure_collection(self):
        if "commits" not in self.client.get_collections():
            self.client.create_collection(
                collection_name="commits",
                vector_size=768,
                distance="Cosine"
            )

    def store_vector(self, collection_name: str, point_id: str, vector: list, payload: dict) -> bool:
        self.client.upsert(
            collection_name=collection_name,
            points=[{
                "id": point_id,
                "vector": vector,
                "payload": payload
            }]
        )
        return True