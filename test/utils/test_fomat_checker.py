from src.util.token import DataAnalyzer
import pytest
import os

file_path = "src/fine_tuning/train_json/yukkuri-marisa.jsonl"


@pytest.fixture
def dummy_dataset():
    return [
        {
            "messages": [
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi there!"},
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "How are you?"},
                {"role": "assistant", "content": "I'm good, thanks for asking!"},
            ]
        },
    ]


def test_load_data(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "dummy.json"
    p.write_text('{"messages": [{"role": "user", "content": "Hello"}]}')

    analyzer = DataAnalyzer()
    dataset = analyzer.load_data(p)

    assert len(dataset) == 1
    assert dataset[0]["messages"][0]["role"] == "user"


def test_format_error_checks(dummy_dataset):
    analyzer = DataAnalyzer()
    try:
        analyzer.format_error_checks(dummy_dataset)
    except analyzer.FormatError:
        pytest.fail("FormatError was raised unexpectedly!")


def test_num_tokens_from_messages(dummy_dataset):
    analyzer = DataAnalyzer()
    messages = dummy_dataset[0]["messages"]
    num_tokens = analyzer.num_tokens_from_messages(messages)
    assert num_tokens > 0


def test_format_error_checks_with_error(dummy_dataset):
    analyzer = DataAnalyzer()
    # エラーを引き起こすようなデータセットを作成
    erroneous_dataset = dummy_dataset.copy()
    erroneous_dataset.append(
        {"messages": [{"role": "unknown", "content": "This should cause an error"}]}
    )

    with pytest.raises(analyzer.FormatError):
        analyzer.format_error_checks(erroneous_dataset)


def test_print_distribution(capfd, dummy_dataset):
    analyzer = DataAnalyzer()
    values = [1, 2, 3, 4, 5]
    analyzer.print_distribution(values, "test_values")

    out, err = capfd.readouterr()
    assert "Distribution of test_values" in out
    assert "min / max: 1, 5" in out


def test_cost_estimates(dummy_dataset):
    analyzer = DataAnalyzer()
    convo_lens = [4000, 3000, 5000]  # 例えば会話長のリスト
    analyzer.cost_estimates(dummy_dataset, convo_lens)


def test_load_data_and_format_error_checks(tmp_path):
    # テスト用のデータファイルを作成
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "dummy.json"
    p.write_text(
        '{"messages": [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi!"}]}'
    )

    analyzer = DataAnalyzer()
    dataset = analyzer.load_data(p)

    # ロードされたデータセットに対してformat_error_checksを実行
    try:
        analyzer.format_error_checks(dataset)
    except analyzer.FormatError:
        pytest.fail("FormatError was raised unexpectedly!")


def test_load_data_and_token_analysis(tmp_path, capfd):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "dummy.json"
    p.write_text(
        '{"messages": [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi!"}]}'
    )

    analyzer = DataAnalyzer()
    dataset = analyzer.load_data(p)
    messages = dataset[0]["messages"]
    num_tokens = analyzer.num_tokens_from_messages(messages)

    assert num_tokens > 0

    analyzer.print_distribution([num_tokens], "num_tokens")
    out, err = capfd.readouterr()
    assert "Distribution of num_tokens" in out
