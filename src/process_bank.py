import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_operations(data: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчет количества банковских операций по категориям.

    :param data: Список словарей с данными о банковских операциях.
    :param categories: Список категорий, по которым необходимо произвести подсчет.
    :return: Словарь с количеством операций по категориям.
    """
    count: Counter = Counter()  # Здесь мы добавили тип аннотации для переменной count
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                count[category] += 1
    return dict(count)


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Поиск банковских операций по описанию.

    :param data: Список словарей с данными о банковских операциях.
    :param search: Строка для поиска в описании операций.
    :return: Список словарей, содержащих только найденные операции.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [operation for operation in data if pattern.search(operation.get("description", ""))]
