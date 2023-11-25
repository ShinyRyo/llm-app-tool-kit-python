from src.fine_tuning.data_format_generator import ChatTemplate
from src.fine_tuning.data_format_generator import TrainingJsonFormatter
from src.util.token import DataAnalyzer
import pytest
import os
import json


class TestDataFormatGenerator:
    @pytest.fixture
    def csv_content(self, tmpdir):
        data = """role,content
system,value2
user,value4
assistant,value6
"""
        csv_path = tmpdir.join("test.csv")
        csv_path.write(data)
        return str(csv_path)

    def test_read_csv_content(self, csv_content):
        chat_template = ChatTemplate(csv_path=csv_content)
        assert chat_template.templates == [
            {"role": "system", "content": "value2"},
            {"role": "user", "content": "value4"},
            {"role": "assistant", "content": "value6"},
        ]

    def test_create_instance_dataset(self, tmpdir, csv_content):
        # 出力ディレクトリの作成
        output_dir = tmpdir.mkdir("output")

        # TrainingJsonFormatterインスタンスの作成
        formatter = TrainingJsonFormatter(
            input_csv=csv_content, output_dir=str(output_dir)
        )
        print(formatter.input_csv)

        # データセットの生成
        dataset = formatter.create_format()

        # 生成されたデータセットの検証
        assert isinstance(dataset, list)
        assert len(dataset) > 0
        for data in dataset:
            assert "messages" in data
            assert len(data["messages"]) == 3  # 3つのメッセージが含まれていることを確認

        # ファイルへの保存
        formatter.saved_train_file()

        # 保存されたファイルを読み込んで検証
        saved_file_path = os.path.join(
            str(output_dir), formatter.file_name + ".jsonl"
        )
        assert os.path.exists(saved_file_path)

        with open(saved_file_path, "r", encoding="utf-8") as f:
            for line in f:
                message = json.loads(line)
                assert "messages" in message

        # DataAnalyzerのformat_error_checksを用いたフォーマットチェック
        analyzer = DataAnalyzer()
        try:
            analyzer.format_error_checks(dataset)
        except analyzer.FormatError as e:
            pytest.fail(f"FormatError raised: {e}")
