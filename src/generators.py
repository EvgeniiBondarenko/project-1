from collections.abc import Generator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]], currency_code: str
) -> Generator[dict[str, Any], None, None]:
    """Функция-генератор, возвращающая транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[str, None, None]:
    """Функция-генератор, возвращающая описания транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        formatted: str = f"{number:016d}"
        yield " ".join([formatted[i : i + 4] for i in range(0, 16, 4)])

