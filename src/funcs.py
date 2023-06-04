import json

def get_data_from_json(file_name):
    """
    Open json-file and get data
    :param file_name: Имя файла из которого получаются данные
    :return: Список словарей с данными
    """
    with open(file_name, encoding='utf-8') as f:
        data = json.load(f)

    return data


def get_executed_operations(operations_list: list[dict]) -> list[dict]:
    """
    Отфильтровывает операции, оставляя в возвращаемом списке только успешные
    :param operations_list: Список словарей со всеми операциями
    :return: Список словарей с успешными операциями
    """
    executed_operations = []
    for operation in operations_list:
        if 'state' in operation.keys():
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
        else:
            continue

    return executed_operations



def sort_operations(operations_list: list[dict]) -> list[dict]:
    """
    Сортирует операции по дате
    :param operations_list: Список операций
    :return: Список операций отсортированный по дате
    """
    sorted_operations = sorted(operations_list, key=lambda x: x['date'], reverse=True)
    return sorted_operations

def format_date(date: str) -> str:
    """
    Форматирует дату операции
    :param date: Дата и время операции
    :return: Дата операции в заданном формате
    """
    pass


def mask_from_amount(from_amount: str) -> str:
    """
    Маскирует номер счета отправителя
    :param from_amount: Счет отправителя
    :return: Замаскированный счет отправителя
    """
    pass


def mask_to_amount(to_amount: str) -> str:
    """
     Маскирует номер счета получателя
    :param to_amount: Счет получателя
    :return: Замаскированный счет получателя
    """
    pass


def get_message(operation: dict) -> str:
    """
    На основе данных из словаря генерирует сообщение об операции
    :param operation: Словарь с данными по операции
    :return: Сообщение пользователю
    """
    pass
