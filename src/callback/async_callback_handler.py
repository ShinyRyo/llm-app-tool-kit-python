from typing import Any
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.schema.output import LLMResult
from langchain.agents.openai_functions_multi_agent.base import OpenAIMultiFunctionsAgent


class AsyncOpenAIFunctionAgentCallbackHandler(AsyncIteratorCallbackHandler):
    final_answer: bool = False

    async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        self.queue.put_nowait(token)

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        pass
