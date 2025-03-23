import streamlit as st
from config import PRIMARY_COLOR, SECONDARY_COLOR, BACKGROUND_COLOR, TEXT_COLOR

class UIService:
    def __init__(self):
        self.configure_page()
        
    def configure_page(self):
        """Configure the Streamlit page with custom CSS."""
        st.markdown(f"""
            <style>
            .stApp {{
                background-color: {BACKGROUND_COLOR};
                color: {TEXT_COLOR};
            }}
            .stButton>button {{
                background-color: {PRIMARY_COLOR};
                color: white;
                border-radius: 5px;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
            }}
            .stTextInput>div>div>input {{
                border: 2px solid {PRIMARY_COLOR};
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }}
            .stFileUploader>div>div>div>button {{
                background-color: {SECONDARY_COLOR};
                color: white;
                border-radius: 5px;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
            }}
            </style>
        """, unsafe_allow_html=True)
    
    def display_title(self, title):
        """Display the app title."""
        st.title(title)
        
    def display_file_uploader(self, label, file_type):
        """Display a file uploader."""
        return st.file_uploader(label, type=file_type)
    
    def display_text_input(self, label):
        """Display a text input field."""
        return st.text_input(label)
    
    def display_response(self, response):
        """Display the response from the LLM."""
        st.write("Response:")
        st.write(response)
        
    def display_spinner(self, text):
        """Create a spinner context manager."""
        return st.spinner(text)
    
    def display_info(self, text):
        """Display informational text."""
        st.write(text) 