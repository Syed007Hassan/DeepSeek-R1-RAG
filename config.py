# Application configuration

# Color palette
PRIMARY_COLOR = "#1E90FF"
SECONDARY_COLOR = "#FF6347"
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#4561e9"

# LLM settings
MODEL_NAME = "deepseek-r1:7b"
RETRIEVER_K = 3

# Prompt templates
QA_PROMPT_TEMPLATE = """
1. Use the following pieces of context to answer the question at the end.
2. If you don't know the answer, just say that "I don't know" but don't make up an answer on your own.
3. Keep the answer crisp and limited to 3,4 sentences.

Context: {context}
Question: {question}
Helpful Answer:"""

# This template is no longer used with the new chain structure
DOCUMENT_PROMPT_TEMPLATE = "Context:\ncontent:{page_content}\nsource:{source}" 