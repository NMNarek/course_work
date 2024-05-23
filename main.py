from config import OPERATION_PATH, COUNT_OF_OPERATIONS
from src.utils import load_operations, get_executed_operations, get_operation_instances, sort_operations


def main():
    operations = load_operations(OPERATION_PATH)
    operations = get_executed_operations(operations)
    operation_instances = get_operation_instances(operations)
    sorted_operations = sort_operations(operation_instances)
    for operation in sorted_operations[:COUNT_OF_OPERATIONS]:
        print()
        print(operation)


if __name__ == '__main__':
    main()
