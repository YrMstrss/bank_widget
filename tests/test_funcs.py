from src.funcs import get_data_from_json, get_executed_operations, sort_operations, format_date, mask_amount, get_message


def test_get_data_from_json(file, data):
    assert get_data_from_json(file) == data

def test_get_executed_operations(data,executed_data):
    assert get_executed_operations(data) == executed_data


def test_sort_operations(executed_data, sorted_data):
    assert sort_operations(executed_data) == sorted_data


def test_format_date():
    assert format_date('2019-12-08T22:46:21.935582') == '08.12.2019'


def test_mask_from_amount():
    assert mask_amount('Visa Platinum 1246377376343588') == 'Visa Platinum 1246 37** **** 3588'
    assert mask_amount('Maestro 3928549031574026') == 'Maestro 3928 54** **** 4026'
    assert mask_amount('Счет 27248529432547658655') == 'Счет **8655'
    assert mask_amount('Visa Classic 4195191172583802') == 'Visa Classic 4195 19** **** 3802'

def test_get_message(operation, message):
    assert get_message(operation) == message
