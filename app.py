import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.chunking import split_text

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚"
)

st.title("📚 AI Research Paper Assistant")

pdf = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if pdf:

    text = extract_text_from_pdf(pdf)

    chunks = split_text(text)

    st.success("PDF Processed Successfully")

    st.write(f"Total Chunks: {len(chunks)}")

    st.subheader("First Chunk")

    st.write(chunks[0])