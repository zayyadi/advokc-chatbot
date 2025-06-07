# ADVOKC Civic-Tech AI Chatbot

This project is a civic-tech AI chatbot for ADVOKC, designed to answer civic-related queries in Nigeria, track government promises, and provide details about ADVOKC’s advocacy efforts.

## Project Overview

*   **AI Chatbot:** Powered by an open-source LLM (e.g., LLaMA 3, Mistral 7B) using a RAG pipeline with LangChain.
*   **Knowledge Base:** Utilizes Nigerian civic legal frameworks, campaign promises, and ADVOKC's activity data.
*   **Promise Tracking:** Features a module to monitor the status of political promises.
*   **Tech Stack:** FastAPI (backend), React/Next.js (frontend), ChromaDB (vector store), PostgreSQL (database).

## Getting Started

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the FastAPI application:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will typically be available at `http://127.0.0.1:8000`.
