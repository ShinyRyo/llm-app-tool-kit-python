from src.fine_tuning.fine_tuning import get_train_csv_file
import os

def test_get_train_csv_file():
    csv_file = get_train_csv_file('yukkuri-marisa.csv')
    csv_file_disabled = get_train_csv_file('marisa.csv')
    assert os.path.exists(csv_file) == True
    assert os.path.exists(csv_file_disabled) == False


