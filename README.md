# 📚 AI-Powered Research Paper Assistant

An intelligent Research Paper Assistant built using Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), Vector Databases, and Natural Language Processing (NLP). The application allows users to upload research papers and interact with them through natural language queries, making academic research faster, easier, and more efficient.

---

## 🚀 Features

### 📄 Research Paper Upload

* Upload research papers in PDF format.
* Automatically extract and process text content.

### 🔍 Semantic Search

* Retrieve relevant information based on meaning rather than keyword matching.
* Powered by vector embeddings and FAISS.

### 🤖 AI-Powered Question Answering

* Ask questions directly about the uploaded paper.
* Answers are generated using Gemini and grounded in retrieved paper content.

### 💬 Conversational Chat Interface

* ChatGPT-style interface.
* Maintains conversation history during the session.

### 🧠 Retrieval-Augmented Generation (RAG)

* Combines semantic retrieval with LLM reasoning.
* Reduces hallucinations by providing paper-specific context.

### 📊 Token Usage Tracking

* Monitor LLM token consumption.
* Useful for cost and performance analysis.

---

## 🏗️ System Architecture

PDF Upload
↓
Text Extraction
↓
Text Chunking
↓
Embedding Generation
↓
FAISS Vector Database
↓
Semantic Retrieval
↓
Gemini LLM
↓
Context-Aware Answer Generation

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / Machine Learning

* LangChain
* Sentence Transformers
* Gemini API

### Vector Database

* FAISS

### NLP

* Text Chunking
* Semantic Search
* Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```text
AI-Powered-Research-Paper-Assistant/

├── app.py
├── requirements.txt
├── .env
│
├── data/
│   └── uploaded_pdfs/
│
├── utils/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
└── research/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Powered-Research-Paper-Assistant.git

cd AI-Powered-Research-Paper-Assistant
```

### Create Virtual Environment

```bash
python -m venv research
```

### Activate Environment

#### Windows

```bash
research\Scripts\activate
```

#### Linux / Mac

```bash
source research/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Current Capabilities

* PDF Upload and Processing
* Research Paper Question Answering
* Semantic Search
* Conversational Interface
* Token Usage Monitoring
* Gemini Integration
* FAISS-Based Retrieval

---

## Release History

### v1.0 - Core RAG System

- PDF Upload & Processing
- Semantic Search with FAISS
- BGE Embeddings
- Gemini 2.5 Flash Integration
- Persistent FAISS Caching
- Hash-Based Document Lookup
- Cross-Encoder Re-Ranking
- Conversational Research Q&A
- Token Usage Tracking
 
---

## 🔮 Future Enhancements

* Multiple PDF Upload Support
* Research Paper Comparison
* Executive Summary Generation
* Methodology Summary
* Results Summary
* Citation Generation
* Flashcard Generation
* MCQ Generation
* Literature Review Assistant
* Hybrid Search (BM25 + Vector Search)
* Research Insights Dashboard

---

<<<<<<< Updated upstream
=======
<!-- ## 📈 Resume Description -->

<!-- Developed an AI-Powered Research Paper Assistant using Retrieval-Augmented Generation (RAG), FAISS, Sentence Transformers, LangChain, and Gemini API. Implemented semantic document retrieval, conversational question answering, vector search, and contextual response generation to improve research paper comprehension and information extraction. -->

---

>>>>>>> Stashed changes
## 👨‍💻 Author

Veer Tiwari

B.Tech Student | Data Science & AI/ML Enthusiast | Machine Learning Engineer Aspirant
