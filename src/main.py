from util.token import DataAnalyzer

if __name__ == "__main__":
    file_path = "src/fine_tuning/train_json/yukkuri-marisa.jsonl"
    analyzer = DataAnalyzer()
    data = analyzer.load_data(file_path)
    analyzer.format_error_checks(data)

    