import streamlit as st
from dotenv import load_dotenv

from utils.pdf_loader import extract_text_from_pdf
from utils.chunking import split_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.rag_pipeline import get_llm

from utils.summarizer import (
    generate_summary_prompt
)

from utils.reranker import (
    get_reranker,
    rerank_documents
)

from utils.cache_manager import (
    generate_pdf_hash,
    get_index_path,
    index_exists
)

from utils.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)

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

        embeddings = get_embeddings()

        pdf_hash = generate_pdf_hash(pdf)

        index_path = get_index_path(pdf_hash)
        
        text = extract_text_from_pdf(pdf)

        st.session_state.paper_text = text

        if index_exists(pdf_hash):

            st.success("⚡ Existing Index Found")

            vector_db = load_vector_store(
                embeddings,
                index_path
            )

            chunks = None

        else:

            st.info("📄 Processing PDF...")

            chunks = split_text(text)

            vector_db = create_vector_store(
                chunks,
                embeddings
            )

            save_vector_store(
                vector_db,
                index_path
            )

            st.success("✅ Index Saved")

            st.session_state.chunk_count = len(chunks)

        st.session_state.char_count = len(text)

        llm = get_llm()
        reranker = get_reranker()

    # Sidebar
    with st.sidebar:

        st.header("📄 Paper Statistics")

        st.metric(
            "Chunks",
            st.session_state.get(
                "chunk_count",
                "Cached"
            )
        )

        st.metric(
            "Characters",
            st.session_state.get(
                "char_count",
                "N/A"
            )
        )

        st.success("Paper Loaded")

        if st.button("🗑 Clear Chat"):

            st.session_state.messages = []

            st.rerun()

    st.success("✅ PDF Processed Successfully")

    st.subheader("📑 Research Paper Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        executive_btn = st.button(
            "📄 Executive Summary"
        )

    with col2:
        methodology_btn = st.button(
            "🔬 Methodology"
        )

    with col3:
        results_btn = st.button(
            "📊 Results"
        )

    col4, col5 = st.columns(2)

    with col4:
        limitations_btn = st.button(
            "⚠️ Limitations"
        )

    with col5:
        future_btn = st.button(
            "🚀 Future Work"
        )

    summary_type = None

    if executive_btn:
        summary_type = "executive"

    elif methodology_btn:
        summary_type = "methodology"

    elif results_btn:
        summary_type = "results"

    elif limitations_btn:
        summary_type = "limitations"

    elif future_btn:
        summary_type = "future_work"


    if summary_type:

        with st.spinner(
            "Generating Summary..."
        ):

            docs = vector_db.similarity_search(
                "summarize the research paper",
                k=20
            )

            context = "\n\n".join(
                [
                    doc.page_content
                    for doc in docs
                ]
            )

            prompt = generate_summary_prompt(
                summary_type,
                context
            )

            response = llm.invoke(
                prompt
            )

            st.subheader(
                "📋 Summary"
            )

            st.write(
                response.content
            )
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
                k=20
            )
            ranked_docs = rerank_documents(
                question,
                docs,
                reranker,
                top_k=5
            )

            docs = [
                doc
                for doc, score in ranked_docs
            ]
            docs = rerank_documents(
                question,
                docs,
                reranker,
                top_k=5
            )

            # Build Context
            context = "\n\n".join(
                [doc.page_content for doc, score in ranked_docs]
            )

            with st.expander("🔍 Retrieved Chunks"):

                for i, (doc, score) in enumerate(
                    ranked_docs,
                    start=1
                ):

                    st.markdown(
                        f"### Chunk {i} | Score: {score:.4f}"
                    )

                    st.write(
                        doc.page_content[:700]
                    )


            with st.expander("📊 Reranking Scores"):

                for i, (doc, score) in enumerate(
                    ranked_docs,
                    start=1
                ):

                    st.write(
                        f"Chunk {i}: {score:.4f}"
                    )

            # Prompt
            prompt = f"""
            You are an expert research paper analyst.

            Use ONLY the provided context.

            Rules:
            1. Do not use outside knowledge.
            2. If information is missing, explicitly say so.
            3. Answer in a structured format.
            4. Mention important findings and limitations when relevant.
            5. Be concise but accurate.

            Context:
            {context}

            Question:
            {question}

            Answer:
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