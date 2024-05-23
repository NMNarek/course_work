from config import OPERATION_PATH
from src.utils import load_operations


def main():
    operations = load_operations(OPERATION_PATH)


if __name__ == '__main__':
    main()