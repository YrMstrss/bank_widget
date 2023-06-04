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
    date_list = date.split('T')[0].split('-')
    return '.'.join(date_list[::-1])


def mask_amount(amount: str) -> str:
    """
    Маскирует номер счета
    :param amount: Номер счета
    :return: Замаскированный номер счета
    """
    if 'Счет' in amount:
        amount_list = amount.split(' ')
        return amount_list[0] + ' **' + amount_list[1][-4:]
    else:
        amount_list = amount.split(' ')
        masked_card_number = amount_list[-1][0:4] + ' ' + amount_list[-1][4:6] + '** **** ' + amount_list[-1][12:16]
        if len(amount_list) == 2:
            return amount_list[0] + ' ' + masked_card_number
        if len(amount_list) == 3:
            return amount_list[0] + ' ' + amount_list[1] + ' ' + masked_card_number



def get_message(operation: dict) -> str:
    """
    На основе данных из словаря генерирует сообщение об операции
    :param operation: Словарь с данными по операции
    :return: Сообщение пользователю
    """
    date = format_date(operation['date'])
    description = operation['description']
    if 'from' not in operation.keys():
        from_account = 'Счет отправителя неизвестен'
    else:
        from_account = mask_amount(operation['from'])
    to_account = mask_amount(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    first_line = date + ' ' + description + ' \n'
    second_line = from_account + ' -> ' + to_account + ' \n'
    third_line = amount + ' ' + currency + ' \n'

    return ''.join([first_line, second_line, third_line])
