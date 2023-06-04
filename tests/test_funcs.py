from src.funcs import get_data_from_json, get_executed_operations, sort_operations, format_date


def test_get_data_from_json(file, data):
    assert get_data_from_json(file) == data

def test_get_executed_operations(data,executed_data):
    assert get_executed_operations(data) == executed_data


def test_sort_operations(executed_data, sorted_data):
    assert sort_operations(executed_data) == sorted_data


def test_format_date():
    assert format_date('2019-12-08T22:46:21.935582') == '08.12.2019'
