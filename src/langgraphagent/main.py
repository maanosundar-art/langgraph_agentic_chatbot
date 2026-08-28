import streamlit as st
from src.langgraphagent.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_apent_app():
    """
    load and run the LangGraph Agent Streamlit app with streamlit UI.
    this iniates the UI, handle user inputs and returns the user controls to the main app.
    """

    # Load the Streamlit UI
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()

    if not user_controls:
        st.error("User controls not found. Please check the configuration.")
        return
    user_message = st.chat_input("Type your message here...")
    