import openai
import os
import tiktoken
import json
import csv

class ChatTemplate:
    def __init__(self, csv_path) -> None:
        self.csv_path = csv_path
        self._templates = self._read_chat_templates()

    def _read_chat_templates(self) -> list[dict[str, str]]:
        template_list = []
        with open(self.csv_path) as csv_file:
            templates = csv.DictReader(csv_file)

            return [template for template in templates]

    @property
    def templates(self) -> list[dict[str, str]]:
        if len(self._templates) < 1:
            raise IndexError('templatesの中身が空です')

        return self._templates


def create_training_data(csv_path, output_dir: str = None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    chat_template = ChatTemplate(csv_path)
    data = []

    for i in range(1, len(chat_template.templates), 2):
        data.append({'messages': [
            chat_template.templates[0],
            chat_template.templates[i],
            chat_template.templates[i + 1]
        ]})

    json_file_path = os.path.join(output_dir, 'train_json/train.jsonl')

    with open(json_file_path, 'w', encoding='utf-8') as f:
        for item in data:
            json_line = json.dumps(item, ensure_ascii=False)
            f.write(json_line + '\n')



