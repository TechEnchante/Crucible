from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

#Encodes 'text' into a high-dimensional vector using the all-mpnet-base-v2 SentenceTransformer
def embed_text(text: str) -> list[float]:
    #'model.encode' returns a numpy array of floats 
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()