from langchain.chat_models import ChatOpenAI

class BaseStreamChatOpenAI:
    model_name: str

    def __init__(self) -> None:
        pass