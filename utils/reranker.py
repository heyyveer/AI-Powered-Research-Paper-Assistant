import streamlit as st
from sentence_transformers import CrossEncoder


@st.cache_resource
def get_reranker():
    """
    Load and cache the Cross Encoder model.
    """

    reranker = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    return reranker


def rerank_documents(
    question,
    docs,
    reranker,
    top_k=5
):
    """
    Re-rank retrieved documents using Cross Encoder.

    Returns:
        ranked_docs -> [(doc, score), ...]
    """

    pairs = [
        (question, doc.page_content)
        for doc in docs
    ]

    scores = reranker.predict(
        pairs
    )

    ranked_docs = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_docs[:top_k]