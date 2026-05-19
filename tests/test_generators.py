import pytest
from typing import Any, Generator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Fixture для тестовых данных
@pytest.fixture
def sample_transactions() -> list[dict[str, Any]]:
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод в USD"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод в EUR"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата в USD"},
        {"operationAmount": {"currency": {"code": "RUB"}}, "description": "Пополнение в RUB"},
        {"description": "Транзакция без operationAmount"}, # Кейс с отсутствием operationAmount
        {"operationAmount": {}, "description": "Транзакция с пустым operationAmount"}, # Кейс с пустым operationAmount
        {"operationAmount": {"currency": {}}, "description": "Транзакция с пустым currency"} # Кейс с пустым currency
    ]

def test_filter_by_currency_usd(sample_transactions: list[dict[str, Any]]):
    """Тест фильтрации по валюте USD."""
    filtered_generator = filter_by_currency(sample_transactions, "USD")
    filtered_list = list(filtered_generator)

    assert len(filtered_list) == 2
    assert filtered_list[0] == {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод в USD"}
    assert filtered_list[1] == {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата в USD"}

def test_filter_by_currency_eur(sample_transactions: list[dict[str, Any]]):
    """Тест фильтрации по валюте EUR."""
    filtered_generator = filter_by_currency(sample_transactions, "EUR")
    filtered_list = list(filtered_generator)

    assert len(filtered_list) == 1
    assert filtered_list[0] == {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод в EUR"}

def test_filter_by_currency_rub(sample_transactions: list[dict[str, Any]]):
    """Тест фильтрации по валюте RUB."""
    filtered_generator = filter_by_currency(sample_transactions, "RUB")
    filtered_list = list(filtered_generator)

    assert len(filtered_list) == 1
    assert filtered_list[0] == {"operationAmount": {"currency": {"code": "RUB"}}, "description": "Пополнение в RUB"}

def test_filter_by_currency_nonexistent(sample_transactions: list[dict[str, Any]]):
    """Тест фильтрации по несуществующей валюте."""
    filtered_generator = filter_by_currency(sample_transactions, "GBP")
    filtered_list = list(filtered_generator)

    assert len(filtered_list) == 0

def test_filter_by_currency_empty_list():
    """Тест фильтрации на пустом списке транзакций."""
    filtered_generator = filter_by_currency([], "USD")
    filtered_list = list(filtered_generator)

    assert len(filtered_list) == 0

def test_filter_by_currency_malformed_data(sample_transactions: list[dict[str, Any]]):
    """Тест обработки некорректных данных в транзакциях."""
    # Добавляем транзакции с потенциально некорректным форматом
    malformed_transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "OK"},
        {"operationAmount": {"currency": {}}, "description": "Нет кода"}, # Нет 'code'
        {"operationAmount": {}, "description": "Нет currency"}, # Нет 'currency'
        {"description": "Нет operationAmount"}, # Нет 'operationAmount'
        {"operationAmount": {"currency": {"other_key": "value"}}, "description": "Другой ключ"} # Не тот ключ
    ]
    filtered_generator = filter_by_currency(malformed_transactions, "USD")
    filtered_list = list(filtered_generator)

    assert len(filtered_list) == 1
    assert filtered_list[0] == {"operationAmount": {"currency": {"code": "USD"}}, "description": "OK"}

@pytest.fixture
def sample_transactions_for_desc() -> list[dict[str, Any]]:
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод в USD"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод в EUR"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата в USD"},
        {"operationAmount": {"currency": {"code": "RUB"}}, "description": "Пополнение в RUB"},
        {"operationAmount": {"currency": {"code": "USD"}}}, # Транзакция без описания
        {} # Пустая транзакция
    ]

def test_transaction_descriptions_basic(sample_transactions_for_desc: list[dict[str, Any]]):
    """Тест получения описаний транзакций."""
    descriptions_generator = transaction_descriptions(sample_transactions_for_desc)
    descriptions_list = list(descriptions_generator)

    assert len(descriptions_list) == 6
    assert descriptions_list == [
        "Перевод в USD",
        "Перевод в EUR",
        "Оплата в USD",
        "Пополнение в RUB",
        "Нет описания", # Ожидаемое значение для транзакции без description
        "Нет описания"  # Ожидаемое значение для пустой транзакции
    ]

def test_transaction_descriptions_empty_list():
    """Тест получения описаний на пустом списке транзакций."""
    descriptions_generator = transaction_descriptions([])
    descriptions_list = list(descriptions_generator)

    assert len(descriptions_list) == 0
    assert descriptions_list == []

def test_card_number_generator_range():
    """Тест генератора номеров карт в стандартном диапазоне."""
    generator = card_number_generator(1, 3)
    card_numbers = list(generator)

    assert len(card_numbers) == 3
    assert card_numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]

def test_card_number_generator_single_number():
    """Тест генератора при одном числе в диапазоне."""
    generator = card_number_generator(1234567890123456, 1234567890123456)
    card_numbers = list(generator)

    assert len(card_numbers) == 1
    assert card_numbers[0] == "1234 5678 9012 3456"

def test_card_number_generator_empty_range():
    """Тест генератора при пустом диапазоне (start > stop)."""
    generator = card_number_generator(10, 5)
    card_numbers = list(generator)

    assert len(card_numbers) == 0
    assert card_numbers == []

def test_card_number_generator_padding():
    """Тест генератора на числах, требующих дополнения нулями."""
    generator = card_number_generator(1, 2)
    card_numbers = list(generator)

    assert len(card_numbers) == 2
    assert card_numbers[0] == "0000 0000 0000 0001"
    assert card_numbers[1] == "0000 0000 0000 0002"

    # Тест для чисел, приближенных к 16-значному формату
    generator_large = card_number_generator(1234567890123, 1234567890124) # 13 цифр
    card_numbers_large = list(generator_large)
    assert len(card_numbers_large) == 2
    assert card_numbers_large[0] == "0001 2345 6789 0123"
    assert card_numbers_large[1] == "0001 2345 6789 0124"

def test_card_number_generator_max_value():
    """Тест генератора с максимальным 16-значным числом."""
    max_int_16_digits = 9999999999999999
    generator = card_number_generator(max_int_16_digits, max_int_16_digits)
    card_numbers = list(generator)

    assert len(card_numbers) == 1
    assert card_numbers[0] == "9999 9999 9999 9999"


