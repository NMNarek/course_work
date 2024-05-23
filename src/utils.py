import json
from pathlib import Path


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
