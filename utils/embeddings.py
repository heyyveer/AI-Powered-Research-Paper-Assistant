import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings

@st.cache_resource
def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5"
    )

    return embeddings