import asyncio
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from pydantic import BaseModel
from agent.function_calling.base_function_agent import BaseFunctionAgent
from agent.function_calling.apis.crypts.crypts import CryptocurrencyPriceTool
from langchain.agents import AgentType, AgentExecutor
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferWindowMemory
from callback.async_callback_handler import AsyncOpenAIFunctionAgentCallbackHandler

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    content: str


async def create_generator(query: str):
    stream_it = AsyncOpenAIFunctionAgentCallbackHandler()
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        streaming=True,
        callbacks=[stream_it],
    )

    memory = ConversationBufferWindowMemory(
        memory_key="chat_history", k=5, return_messages=True, output_key="output"
    )

    agent = initialize_agent(
        tools=[CryptocurrencyPriceTool()],
        llm=llm,
        agent=AgentType.OPENAI_MULTI_FUNCTIONS,
        return_intermediate_steps=False,
        verbose=True,
    )

    task = asyncio.create_task(agent.arun(query))
    async for token in stream_it.aiter():
        yield token

    await task


@app.post("/stream_chat")
async def stream_chat(message: Message):
    gen = create_generator(message.content)
    return StreamingResponse(gen, media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0")
