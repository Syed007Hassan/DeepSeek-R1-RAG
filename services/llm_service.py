from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import RetrievalQA
from config import MODEL_NAME, QA_PROMPT_TEMPLATE, DOCUMENT_PROMPT_TEMPLATE

class LLMService:
    def __init__(self, model_name=MODEL_NAME):
        self.llm = Ollama(model=model_name)
        self.qa_chain = None
        
    def setup_qa_chain(self, retriever):
        """Set up question-answering chain with retriever."""
        # Create the prompt template
        qa_prompt = PromptTemplate.from_template(QA_PROMPT_TEMPLATE)
        
        # Create the LLM chain
        llm_chain = LLMChain(
            llm=self.llm,
            prompt=qa_prompt,
            verbose=True
        )
        
        # Create the document prompt
        document_prompt = PromptTemplate(
            input_variables=["page_content", "source"],
            template=DOCUMENT_PROMPT_TEMPLATE
        )
        
        # Create the document chain
        combine_documents_chain = StuffDocumentsChain(
            llm_chain=llm_chain,
            document_variable_name="context",
            document_prompt=document_prompt
        )
        
        # Create the retrieval QA chain
        self.qa_chain = RetrievalQA(
            combine_documents_chain=combine_documents_chain,
            retriever=retriever,
            return_source_documents=True,
            verbose=True
        )
        
        return self.qa_chain
    
    def answer_question(self, question):
        """Answer a question using the QA chain."""
        if self.qa_chain is None:
            raise ValueError("QA chain has not been set up yet.")
        
        try:    
            response = self.qa_chain(question)
            return response["result"]
        except Exception as e:
            # Add more robust error handling
            print(f"Error during question answering: {str(e)}")
            return f"An error occurred while processing your question. Please try again. Error: {str(e)}" 