# AI Document Assistant (RAG-Based Document QA System)

AI Document Assistant is an intelligent **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask questions about their content. The system retrieves relevant information from the documents using **semantic search** and generates accurate responses using a **Large Language Model (LLM)**.

This project demonstrates how modern AI systems combine **vector databases, embeddings, and LLMs** to build practical document intelligence tools.

---

# Key Features

• Upload multiple **PDF and DOCX documents**
• Ask questions about the uploaded documents
• **Semantic search** using vector embeddings
• **Retrieval-Augmented Generation (RAG)** architecture
• AI-powered responses using **Groq Llama 3.1 model**
• **Source citation** for retrieved document chunks
• **ChatGPT-style conversational interface**
• Persistent chat history during the session
• Option to **download conversation history**

---

# Architecture

The system follows a **RAG pipeline** to ensure accurate answers.

User Question
↓
Vector Search (FAISS)
↓
Retrieve Relevant Document Chunks
↓
Combine Context + Question
↓
LLM (Groq Llama 3.1)
↓
Generated Answer with Sources

---

# Technologies Used

### AI / Machine Learning

* Retrieval-Augmented Generation (RAG)
* HuggingFace Sentence Transformers
* Groq Llama 3.1 LLM

### Backend / AI Frameworks

* LangChain
* FAISS Vector Database

### Document Processing

* PyPDF
* python-docx

### Frontend

* Streamlit

### Other Tools

* Python
* dotenv

---

# Project Structure

```
AI-Document-Query-System
│
├── app.py              # Streamlit UI
├── ingest.py           # Document processing & vector store creation
├── query.py            # RAG retrieval + LLM generation
├── requirements.txt
├── .env
└── vector_store
```

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/AI-Document-Assistant.git
cd AI-Document-Assistant
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Setup Environment Variables

Create a `.env` file and add your **Groq API key**

```
GROQ_API_KEY=your_api_key_here
```

You can get the key from:

[https://console.groq.com/keys](https://console.groq.com/keys)

---

# Run the Application

```
streamlit run app.py
```

Then open the browser at

```
http://localhost:8501
```

---

# Example Use Cases

• Enterprise document search
• Research paper question answering
• Legal document analysis
• Knowledge base assistant
• Customer support documentation search

---

# Snapshot of Project

<img width="1864" height="808" alt="image" src="https://github.com/user-attachments/assets/7aafbe06-09b1-4afe-99f0-49aa5cdbcb84" />

---

# Author

**Shubham Vishwakarma**
LinkedIn:
[https://linkedin.com/in/shubham-vishwakarma-358332209](https://linkedin.com/in/shubham-vishwakarma-358332209)
