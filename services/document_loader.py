from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

class DocumentLoader:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        
    def save_uploaded_file(self, uploaded_file, temp_path="temp.pdf"):
        """Save the uploaded file to a temporary location."""
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        return temp_path
    
    def load_and_split_pdf(self, file_path):
        """Load PDF and split into semantic chunks."""
        loader = PDFPlumberLoader(file_path)
        docs = loader.load()
        
        # Split into semantic chunks
        text_splitter = SemanticChunker(self.embeddings)
        documents = text_splitter.split_documents(docs)
        
        return documents
    
    def cleanup_temp_files(self, file_path):
        """Clean up temporary files."""
        if os.path.exists(file_path):
            os.remove(file_path) 