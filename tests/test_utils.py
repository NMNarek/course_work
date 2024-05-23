from src.classes import Operation
from src.utils import get_executed_operations, sort_operations, get_operation_instances


def test_get_executed_operations():
    data = [
        {"state": "EXECUTED"}, {"state": "EXECUTED"}, {},
        {"state": "EXECUTED"}
    ]

    executed_operations = [
        {"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "EXECUTED"}
    ]

    assert get_executed_operations(data) == executed_operations
    assert len(get_executed_operations(data)) == 3


def test_get_operation_instances(list_with_dicts):
    received_instances_operations = get_operation_instances(list_with_dicts)
    assert len(received_instances_operations) == len(list_with_dicts)
    assert isinstance(received_instances_operations, list)


def test_sort_operations(operations):
    sorted_operations = sort_operations(operations)
    assert isinstance(sorted_operations, list)
    assert len(sorted_operations) > 0
    assert isinstance(sorted_operations[0], Operation)

    assert sorted_operations[0].date == "2024-07-12T20:41:47.882230"
