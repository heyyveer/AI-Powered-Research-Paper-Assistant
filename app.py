import streamlit as st
from dotenv import load_dotenv

from utils.pdf_loader import extract_text_from_pdf
from utils.chunking import split_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.rag_pipeline import get_llm

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

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

        # Create Vector Store
        vector_db = create_vector_store(
            chunks,
            embeddings
        )

        # Load Gemini
        llm = get_llm()

    # Sidebar
    with st.sidebar:

        st.header("📄 Paper Statistics")

        st.metric(
            "Chunks",
            len(chunks)
        )

        st.metric(
            "Characters",
            len(text)
        )

        st.success("Paper Loaded")

        if st.button("🗑 Clear Chat"):

            st.session_state.messages = []

            st.rerun()

    st.success("✅ PDF Processed Successfully")

    # Display Chat History
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # Chat Input
    question = st.chat_input(
        "Ask a question about the paper"
    )

    if question:

        # Store User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        with st.spinner("Generating Answer..."):

            # Retrieve Relevant Chunks
            docs = vector_db.similarity_search(
                question,
                k=4
            )

            # Build Context
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

            # Generate Response
            response = llm.invoke(prompt)

            answer = response.content

            usage = response.usage_metadata

        # Store Assistant Message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Display Assistant Response
        with st.chat_message("assistant"):

            st.markdown(answer)
            
        with st.expander("📊 Token Usage"):

            st.write(
                f"Input Tokens: {usage.get('input_tokens', 'N/A')}"
            )

            st.write(
                f"Output Tokens: {usage.get('output_tokens', 'N/A')}"
            )

            st.write(
                f"Total Tokens: {usage.get('total_tokens', 'N/A')}"
            )        
        # Debug Context
        with st.expander("🔍 Retrieved Context"):

            st.write(context)