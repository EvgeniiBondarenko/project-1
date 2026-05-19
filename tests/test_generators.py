import pytest
from typing import Any

# Импортируем тестируемые функции
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency_finds_matches() -> None:
    """Корректно фильтрует по валюте."""
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2

def test_filter_by_currency_no_matches() -> None:
    """Нет транзакций в заданной валюте — пустой результат."""
    transactions = [
        {"operationAmount": {"currency": {"code": "EUR"}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []

def test_filter_by_currency_empty_list() -> None:
    """Пустой список на входе — пустой результат, без ошибок."""
    result = list(filter_by_currency([], "USD"))
    assert result == []

# ============================================================
# transaction_descriptions
# ============================================================

def test_transaction_descriptions_returns_descriptions() -> None:
    """Возвращает описание каждой транзакции."""
    transactions = [
        {"description": "Перевод"},
        {"description": "Оплата"},
    ]
    result = list(transaction_descriptions(transactions))
    assert result == ["Перевод", "Оплата"]

def test_transaction_descriptions_empty_list() -> None:
    """Пустой список — пустой результат."""
    result = list(transaction_descriptions([]))
    assert result == []

# ============================================================
# card_number_generator
# ============================================================

def test_card_number_generates_correct_format() -> None:
    """Номера карт в формате XXXX XXXX XXXX XXXX."""
    result = list(card_number_generator(1, 2))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
    ]

def test_card_number_start_equals_stop() -> None:
    """Один номер при start == stop."""
    result = list(card_number_generator(5, 5))
    assert result == ["0000 0000 0000 0005"]

def test_card_number_stop_less_than_start() -> None:
    """Пустой результат, если stop < start."""
    result = list(card_number_generator(10, 5))
    assert result == []
