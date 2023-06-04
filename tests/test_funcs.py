from src.funcs import get_data_from_json, get_executed_operations


def test_get_data_from_json(file, data):
    assert get_data_from_json(file) == data

def test_get_executed_operations(data,executed_data):
    assert get_executed_operations(data) == executed_data
