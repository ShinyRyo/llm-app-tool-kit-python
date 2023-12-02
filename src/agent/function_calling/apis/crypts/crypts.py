from pycoingecko import CoinGeckoAPI
from pydantic import BaseModel, Field
from typing import Type
from enum import Enum
from langchain.tools import BaseTool
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain import SerpAPIWrapper
from langchain.callbacks import FinalStreamingStdOutCallbackHandler
import json

cg = CoinGeckoAPI()

def get_cryptocurrency_price(crypts: list[str], vs_currencies: str):
    results = cg.get_price(ids=crypts, vs_currencies=vs_currencies)
    return json.dumps(results)

class GetCryptocurrencyPriceInput(BaseModel):
    crypts: list[str] = Field(description="https://www.coingecko.com/apiで使用する通貨idを入力してください")
    vs_currencies: str = Field(description="通貨の表現方法を入力してください")

class CryptocurrencyPriceTool(BaseTool):
    name = "get_cryptocurrency_price"
    description = "必要な他のサポート通貨での暗号通貨の現在の価格を取得します"

    def _run(self, crypts: list[str], vs_currencies: str):
        result = get_cryptocurrency_price(crypts, vs_currencies)
        return result

    def _arun(self, crypts: list[str], vs_currencies: str):
        raise NotImplementedError("This tool does not support async")


async def execute_agent(request: str, debug: bool = False):
    callback = FinalStreamingStdOutCallbackHandler()
    llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True, callbacks=[callback])
    tools = [CryptocurrencyPriceTool()]
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=debug)
    for response in agent.run(request):
        yield response


