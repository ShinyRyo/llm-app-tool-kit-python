import json
import os
import requests
from bs4 import BeautifulSoup, ResultSet, Tag

class WebScraper:
    def __init__(self, url: str):
        self.url = url
        self.soup = None

    def get_soup(self) -> bool:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return True
        except requests.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return False

    @staticmethod
    def clean_text(text: str) -> str:
        text = text.replace('\n', '').replace('\r', '')
        return ''.join(c for c in text if not '\ud800' <= c <= '\udfff')

    @staticmethod
    def save_data_to_jsonl(data: list, file_path: str) -> bool:
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                for word in data:
                    json.dump(word, f, ensure_ascii=False)
                    f.write('\n')
            return True
        except IOError as e:
            print(f"Error saving data to {file_path}: {e}")
            return False

