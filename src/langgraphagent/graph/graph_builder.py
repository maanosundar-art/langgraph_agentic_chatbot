from src.langgraphagent.state.state import State
from langgraph.graph import StateGraph,START, END
from src.langgraphagent.nodes.basic_bot import BasicChatBot

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_graph(self):
        """
        Builds a basic chatbot graph using the provided LLM model.
        """
        self.basic_chatbot = BasicChatBot(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase:str):
        """
        sets up the graph for the selected use case
        """
        if usecase == "BASIC CHATBOT":
            self.basic_chatbot_graph()

        return self.graph_builder.compile()
    
