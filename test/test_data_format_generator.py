import pytest
from src.fine_tuning.data_format_generator import ChatTemplate, create_training_data  # your_moduleは実際のモジュール名に置き換えてください
import os
import json

@pytest.fixture
def csv_content(tmpdir):
    data = '''role,content
system,hogehogehoge
user,hugehugehuge
assistant,hagehagehage
'''
    csv_path = tmpdir.join("test.csv")
    csv_path.write(data)
    return str(csv_path)

def test_read_chat_templates(csv_content):
    chat_template = ChatTemplate(csv_content)
    for tmp in chat_template.templates:
        if tmp['role'] =='system':
            assert tmp['content'] == 'hogehogehoge'

        elif tmp['role'] == 'user':
            assert tmp['content'] == 'hugehugehuge'

        else:
            assert tmp['content'] == 'hagehagehage'

def test_create_training_data(csv_content):
    create_training_data(csv_content)
    assert os.path.exists(csv_content)
