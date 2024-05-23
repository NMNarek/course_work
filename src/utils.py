import json
from pathlib import Path

from src.classes import Operation


def load_operations(path: Path) -> list[dict]:
    """
    получаем список со словарями
    :param path:
    :return: json.load(operations)
    """
    with open(path, encoding='utf-8') as operations:
        return json.load(operations)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    """
    фильтруем список со словарями
    :param operations:
    :return:
    """
    return [
        operation for operation in operations
        if operation.get("state") == "EXECUTED" and operation
    ]


def get_operation_instances(operations: list[dict]) -> list[Operation]:
    """
    раскладываем все операции в экземпляры классов
    :param operations:
    :return:
    """
    operations_instances = []
    for operation in operations:
        operation_instance = Operation(
            state=operation["state"],
            from_=operation.get("from", ""),
            date=operation["date"],
            amount=operation["operationAmount"]["amount"],
            currency_name=operation["operationAmount"]["currency"]["name"],
            description=operation["description"],
            to=operation["to"]
        )
        operations_instances.append(operation_instance)
    return operations_instances


def sort_operations(operations: list[Operation]) -> list[Operation]:
    """
    сортируем наши операции методами сравнения
    :param operations:
    :return:
    """
    return sorted(operations, reverse=True)



