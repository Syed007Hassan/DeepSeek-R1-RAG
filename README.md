# DeepSeek-R1 RAG System

![image](https://github.com/user-attachments/assets/4cb1143e-252a-4ff0-8384-420119eee4ab)

A Retrieval-Augmented Generation (RAG) system built with DeepSeek-R1, Ollama, and Streamlit.

## Features

- PDF document upload and processing
- Semantic chunking of documents
- Vector embedding and storage with FAISS
- Question answering with DeepSeek-R1 model via Ollama
- User-friendly Streamlit interface

## Project Structure

```
.
├── config.py                # Configuration settings
├── main.py                  # Main application entry point
├── requirements.txt         # Python dependencies
├── services/
│   ├── __init__.py          # Services package initialization
│   ├── document_loader.py   # Document loading and processing
│   ├── llm_service.py       # LLM and QA chain configuration
│   ├── ui_service.py        # Streamlit UI components
│   └── vector_store.py      # Vector database management
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Install Ollama following the instructions at [ollama.ai](https://ollama.ai)

3. Pull the DeepSeek-R1 model:

```bash
ollama pull deepseek-r1
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

The application will be accessible at http://localhost:8501 in your web browser.

## Usage

1. Upload a PDF document using the file uploader
2. Wait for the document to be processed and indexed
3. Enter your question in the text input field
4. View the AI-generated response based on the content of your document

## Requirements

- Python 3.8+
- Ollama installed and running locally
- Sufficient disk space for the DeepSeek-R1 model (approx. 9GB) 
