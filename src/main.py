from util.token import DataAnalyzer
from fine_tuning.fine_tuning import upload_training_file, fine_tuning_execute

if __name__ == "__main__":
    file_path = "src/fine_tuning/train_json/yukkuri-marisa.jsonl"
    analyzer = DataAnalyzer()
    data = analyzer.load_data(file_path)
    analyzer.format_error_checks(data)
    file = upload_training_file()
    fine_tuning_execute(file.id)
