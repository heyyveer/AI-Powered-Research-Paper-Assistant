import streamlit as st
from dotenv import load_dotenv

from utils.pdf_loader import extract_text_from_pdf
from utils.chunking import split_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.rag_pipeline import get_llm

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 AI Research Paper Assistant")

# PDF Upload
pdf = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if pdf:

    with st.spinner("Processing PDF..."):

        # Extract text
        text = extract_text_from_pdf(pdf)

        # Create chunks
        chunks = split_text(text)

        # Create embeddings
        embeddings = get_embeddings()

        # Create FAISS vector database
        vector_db = create_vector_store(
            chunks,
            embeddings
        )

        # Load Gemini
        llm = get_llm()

    st.success("✅ PDF Processed Successfully")

    st.info(f"Total Chunks Created: {len(chunks)}")

    # Question Input
    question = st.text_input(
        "Ask a question about the paper"
    )

    if question:

        with st.spinner("Generating Answer..."):

            # Retrieve relevant chunks
            docs = vector_db.similarity_search(
                question,
                k=4
            )

            # Build context
            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            # Prompt
            prompt = f"""
You are an expert research paper assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply:

"I could not find this information in the uploaded paper."

Context:
{context}

Question:
{question}
"""

            # Gemini response
            response = llm.invoke(prompt)

        st.subheader("📌 Answer")

        st.write(response.content)

        # Optional Debug Section
        with st.expander("Retrieved Context"):
            st.write(context)