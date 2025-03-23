from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import RETRIEVER_K

class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vector_store = None
        
    def create_vector_store(self, documents):
        """Create a vector store from documents."""
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        return self.vector_store
    
    def get_retriever(self, search_type="similarity", k=RETRIEVER_K):
        """Get a retriever from the vector store."""
        if self.vector_store is None:
            raise ValueError("Vector store has not been created yet.")
        
        return self.vector_store.as_retriever(
            search_type=search_type, 
            search_kwargs={"k": k}
        ) 