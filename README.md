# advokc-chatbot

# ADVOKC Civic-tech AI Chatbot (Open-Source LLM Edition)

An open-source AI chatbot designed to provide civic education, track government promises, and disseminate information about ADVOKC’s advocacy activities in Nigeria.

## ✨ Features

- AI-generated civic information using open-source LLaMA 3 / Mistral
- Retrieval-augmented generation for verifiable responses
- Promise tracking by political leaders and institutions
- ADVOKC project and event information
- Natural language interface
- Web-based frontend with optional WhatsApp integration

## 📌 Architecture

- **LLM:** LLaMA 3 (Meta) / Mistral 7B via Hugging Face
- **Embedding Model:** Instructor-Embeddings / SentenceTransformers
- **Vector Database:** ChromaDB (local, self-hosted)
- **Backend:** FastAPI
- **Frontend:** React.js / Next.js
- **Deployment:** Railway / Render / DigitalOcean (GPU support)

## 📂 Project Structure

advokc_chatbot/
├── backend/
│ ├── app/
│ ├── rag/
│ │ ├── model_loader.py
│ │ ├── embedder.py
│ │ ├── retriever.py
│ │ └── chatbot.py
│ ├── data/
│ └── main.py
├── frontend/
│ └── (React-based chat UI)
├── vector_store/
├── README.md
└── requirements.txt


## 📥 Setup Instructions

### Backend Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
