from utils.embeddings import get_embeddings

embeddings = get_embeddings()

vector = embeddings.embed_query(
    "What is machine learning?"
)

print(len(vector))