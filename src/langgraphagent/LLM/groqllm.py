import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls

    def get_groq_llm(self):
        try:
            groq_api_key = self.user_controls["Groq_API_key"]
            selected_model = self.user_controls["llm_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
            #if not groq_api_key and not os.environ.get("GROQ_API_KEY", ''):
                st.warning("Please enter a valid Groq API Key. Don't have one? Get it from https://console.groq.com/keys")
                #st.stop()

            llm = ChatGroq(api_key=groq_api_key, model=selected_model)
            return llm
        except Exception as e:
            st.error(f"Error initializing Groq LLM: {e}")
            return None