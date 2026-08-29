import streamlit as st
from src.langgraphagent.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagent.LLM.groqllm import GroqLLM
from src.langgraphagent.graph.graph_builder import GraphBuilder
from src.langgraphagent.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agent_app():
    """
    load and run the LangGraph Agent Streamlit app with streamlit UI.
    this initiates the UI, handle user inputs and returns the user controls to the main app.
    """

    # Load the Streamlit UI
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_streamlit_ui()

    if not user_controls:
        st.error("User controls not found. Please check the configuration.")
        return
    user_message = st.chat_input("Type your message here...")

    if user_message:
        try:
            # configure the llm's
            obj_groq_llm = GroqLLM(user_controls=user_controls)
            model = obj_groq_llm.get_groq_llm()
            if not model:
                st.error("Failed to initialize the Groq LLM. Please check your API key and model selection.")
                return
            #initialize use case
            usecase = user_controls.get("usecase_option")
            if not usecase:
                st.error("Use case option not found. Please select a valid use case.")
                return


            ## Graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error:graph set failed-{e}")
                return

        except Exception as e:
            st.error(f"Error:graph set failed-{e}")
            return


