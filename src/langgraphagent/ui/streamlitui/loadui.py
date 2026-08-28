import streamlit as st
import os
from src.langgraphagent.ui.uniconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls ={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=">7<" + self.config.get_page_title(), layout="wide")
        st.header(">7<" + self.config.get_page_title())

        with st.sidebar:
            from_model = st.selectbox("Select LLM Model", self.config.get_from_model())
            usecase_option = st.selectbox("Select Use Case", self.config.get_usecase_options())
            self.user_controls["from_model"] = from_model
            if self.user_controls["from_model"] == "Groq":
                self.user_controls["llm_model"] = st.selectbox("Select LLM Model", self.config.get_llm_model())
                self.user_controls["Groq_API_key"] = st.session_state["Groq_API_key"]=st.text_input("Enter Groq API Key", type="password")
                # validate Groq API key
                if not self.user_controls["Groq_API_key"]:
                    st.warning("Please enter a valid Groq API Key. Don't have one? Get it from https://console.groq.com/keys")
                    st.stop
            self.user_controls["usecase_option"] = usecase_option
        return self.user_controls