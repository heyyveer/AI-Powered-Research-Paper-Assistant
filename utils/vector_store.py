from langchain_community.vectorstores import FAISS


def create_vector_store(
    chunks,
    embeddings
):

    vector_db = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_db


def save_vector_store(
    vector_db,
    index_path
):

    vector_db.save_local(
        index_path
    )


def load_vector_store(
    embeddings,
    index_path
):

    vector_db = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db