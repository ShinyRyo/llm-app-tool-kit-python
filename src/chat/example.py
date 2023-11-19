import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def completion_chat(input_message: str) -> str:
    completion = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:onikarubi::8L52AziK",
        messages=[
            {
                "role": "system",
                "content": "あなたは次のような人物になりきって回答をしてください。魔理沙:やや強気で物知りな女性。文法上違和感のない限りかならず「だぜ」を語尾につけてしゃべる。敬語やですます口調は一切使わず、小学校2年生でも理解できるように説明してくれる。",
            },
            {"role": "user", "content": input_message},
        ],
    )

    return completion["choices"][0]["message"]["content"]
