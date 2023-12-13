from src.agent.function_calling.base_function_agent import BaseFunctionAgent
from langchain.chat_models import ChatOpenAI
from src.agent.function_calling.apis.crypts.crypts import CryptocurrencyPriceTool
from src.agent.function_calling.apis.yfinance.yfinance import YahooFinanceTool

def test_execute_tools():
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo-1106",
        streaming=True,
    )

    tools = [YahooFinanceTool(), CryptocurrencyPriceTool()]

    agent = BaseFunctionAgent(
        llm=llm,
        tools=[tool for tool in tools],
    )

    executor = agent.get_executor(debug=True)

    result = executor.run("現在のマイクロソフトの株価はNvidiaと比較してどうですか？")
    print(result)