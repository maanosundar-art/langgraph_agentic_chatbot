from src.langgraphagent.state.state import State

class BasicChatBot:
    """
    BasicChatBot class to handle the basic chatbot functionality.
    """
    def __init__(self, model):
        self.model = model

    def process(self, state: State) ->dict:
        """
        Processes the input state and returns the output.
        """
        return {"messages":self.model.invoke(state["messages"])}