import csv
from typing import Any, Dict, List, cast

import pandas as pd


def read_financial_operations_from_csv(file_path: str = "htmlcov/transactions.csv") -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV файла.

    :param file_path: Путь к CSV файлу (по умолчанию: 'htmlcov/transactions.csv')
    :return: Список словарей с транзакциями
    """
    transactions: List[Dict[str, Any]] = []  # Объявляем список словарей
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)  # row уже является словарем
    return transactions


def read_financial_operations_from_excel(file_path: str = "htmlcov/transactions_excel.xlsx") -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel файла.

    :param file_path: Путь к Excel файлу (по умолчанию: 'htmlcov/transactions_excel.xlsx')
    :return: Список словарей с транзакциями
    """
    df = pd.read_excel(file_path)

    # Приведение типов
    transactions = cast(List[Dict[str, Any]], df.to_dict(orient="records"))  # Явное приведение к правильному типу
    return transactions
