from src.fine_tuning.data_format_generator import create_training_data, ChatTemplate
import pytest
import os
import json

class TestDataFormatGenerator:
    @pytest.fixture
    def csv_content(self, tmpdir):
        data = '''role,content
value1,value2
value3,value4
value5,value6
'''
        csv_path = tmpdir.join("test.csv")
        csv_path.write(data)
        return str(csv_path)

    def test_read_csv_content(self, csv_content):
        chat_template = ChatTemplate(csv_path=csv_content)
        assert chat_template.templates == [{'role': 'value1', 'content': 'value2'}, {'role': 'value3', 'content': 'value4'}, {'role': 'value5', 'content': 'value6'}]

    def test_create_instance_dataset(self):
        pass

