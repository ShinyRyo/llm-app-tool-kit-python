from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import os
import pytest

@pytest.mark.skip(reason="This test is too slow")
def test_chat():
    messages = [
        SystemMessage(content=
            "あなたは次のような人物になりきって回答をしてください。魔理沙:やや強気で物知りな女性。文法上違和感のない限りかならず「だぜ」を語尾につけてしゃべる。敬語やですます口調は一切使わず、小学校2年生でも理解できるように説明してくれる。"
        ),
        HumanMessage(content="MongoDBの使い方を教えてください。"),
    ]

    chat = ChatOpenAI(model="ft:gpt-3.5-turbo-0613:onikarubi::8OKQ1Enq")

    message = chat.invoke(messages)
    print(message.content)
