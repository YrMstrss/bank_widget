from src.funcs import get_data_from_json


def test_get_data_from_json(file, data):
    assert get_data_from_json(file) == data
