import streamlit as st
from services import DocumentLoader, VectorStore, LLMService, UIService

class RAGApplication:
    def __init__(self):
        # Initialize services
        self.ui = UIService()
        self.document_loader = DocumentLoader()
        self.vector_store = VectorStore()
        self.llm_service = LLMService()
        
        # Set up session state for persistence
        if 'documents_processed' not in st.session_state:
            st.session_state.documents_processed = False
        if 'retriever' not in st.session_state:
            st.session_state.retriever = None
        
    def run(self):
        # Display application title
        self.ui.display_title("Build a RAG System with DeepSeek R1 & Ollama")
        
        # Handle file upload
        uploaded_file = self.ui.display_file_uploader("Upload a PDF file", "pdf")
        
        if uploaded_file is not None:
            # Process the document if not already processed
            if not st.session_state.documents_processed:
                with self.ui.display_spinner("Processing document..."):
                    # Save and load the document
                    temp_path = self.document_loader.save_uploaded_file(uploaded_file)
                    documents = self.document_loader.load_and_split_pdf(temp_path)
                    
                    # Create vector store and retriever
                    self.vector_store.create_vector_store(documents)
                    st.session_state.retriever = self.vector_store.get_retriever()
                    
                    # Set up QA chain
                    self.llm_service.setup_qa_chain(st.session_state.retriever)
                    
                    # Mark as processed
                    st.session_state.documents_processed = True
                    
                    # Clean up temp file
                    self.document_loader.cleanup_temp_files(temp_path)
                
                # Add a success message
                st.success("Document processed successfully! You can now ask questions.")
            
            # Handle user query
            user_input = self.ui.display_text_input("Ask a question related to the PDF :")
            
            if user_input:
                try:
                    with self.ui.display_spinner("Processing..."):
                        # Re-setup the QA chain with the retriever from session state
                        if not hasattr(self.llm_service, 'qa_chain') or self.llm_service.qa_chain is None:
                            self.llm_service.setup_qa_chain(st.session_state.retriever)
                        
                        response = self.llm_service.answer_question(user_input)
                        self.ui.display_response(response)
                except Exception as e:
                    st.error(f"Error processing question: {str(e)}")
                    st.info("Try uploading the document again if the error persists.")
                    # Reset the processed state to allow re-uploading
                    st.session_state.documents_processed = False
        else:
            self.ui.display_info("Please upload a PDF file to proceed.")

if __name__ == "__main__":
    app = RAGApplication()
    app.run() 