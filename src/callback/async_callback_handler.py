from typing import Any
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.schema.output import LLMResult


class AsyncCallbackHandler(AsyncIteratorCallbackHandler):
    final_answer: bool = False

    async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        if token != "":
            self.queue.put_nowait(token)

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        pass
