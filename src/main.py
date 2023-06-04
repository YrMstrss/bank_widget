from src.funcs import get_data_from_json, get_executed_operations, sort_operations, get_message

data = get_data_from_json('operations.json')
executed_operations = get_executed_operations(data)
sorted_operations = sort_operations(executed_operations)[:5]

for operation in sorted_operations:
    print(get_message(operation))
