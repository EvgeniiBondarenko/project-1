from typing import Dict, List, Optional


def filter_by_state(transactions: List[Dict[str, str]], state: Optional[str] = "EXECUTED") -> List[Dict[str, str]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    result = []
    for item in transactions:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(transactions: List[Dict[str, str]], descending: Optional[bool] = True) -> List[Dict[str, str]]:
    """Сортитует список словарей по дате и возвращает новый отсортированный список словарей"""
    return sorted(
        transactions, key=lambda item: item.get("date", ""), reverse=descending if descending is not None else False
    )