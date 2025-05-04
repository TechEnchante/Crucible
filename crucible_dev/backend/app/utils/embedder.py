from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

#Given a single string, returns its 768-dim semantic embedding
def embed_text(text: str) -> list[float]:
    return model.encode(text).tolist()