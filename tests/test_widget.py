import pytest
from src.widget import mask_account_card, get_data


def test_mask_account_card():
    # Мокаем вызовы функций из masks
    # Вы можете импортировать mock, если собираетесь использовать библиотеки mock для мока
    # from unittest.mock import patch

    # Проверка на счет
    assert mask_account_card("счет 12345678901234567890") == "счет **7890"

    # Проверка на карту
    assert mask_account_card("карта 1234567812345678") == "карта 1234 56** **** 5678"


def test_get_data():
    # Проверка преобразования даты
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"

    # Проверка на другие даты
    assert get_data("2023-12-31T23:59:59.999999") == "31.12.2023"
    assert get_data("2000-01-01T00:00:00.000000") == "01.01.2000"


