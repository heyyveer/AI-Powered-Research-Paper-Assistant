from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store

chunks = [
    "Machine learning is a subset of AI",
    "Deep learning uses neural networks",
    "RAG combines retrieval and generation"
]

embeddings = get_embeddings()

db = create_vector_store(
    chunks,
    embeddings
)

results = db.similarity_search(
    "What is RAG?",
    k=2
)

for doc in results:
    print(doc.page_content)