from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class State(TypedDict):
    """
    State class to hold the state of the application.
    Represents the structure of the state used in graph
    """
    messages: Annotated[list[BaseMessage], add_messages]  # List of messages in the state