import pytest
from src.process_bank import process_bank_operations, process_bank_search

def test_process_bank_operations():
    data = [
        {"description": "Заправка автомобиля"},
        {"description": "Покупка продуктов"},
        {"description": "Передача средств"},
        {"description": "Заправка моторного масла"},
        {"description": "Оплата коммунальных услуг"},
    ]

    categories = ["Заправка", "Покупка", "Оплата"]

    expected_result = {
        "Заправка": 2,
        "Покупка": 1,
        "Оплата": 1,
    }

    result = process_bank_operations(data, categories)

    assert result == expected_result


def test_process_bank_search():
    data = [
        {"description": "Заправка автомобиля"},
        {"description": "Покупка продуктов"},
        {"description": "Передача средств"},
        {"description": "Заправка моторного масла"},
        {"description": "Оплата коммунальных услуг"},
    ]

    search_term = "заправка"

    expected_result = [
        {"description": "Заправка автомобиля"},
        {"description": "Заправка моторного масла"},
    ]

    result = process_bank_search(data, search_term)

    assert result == expected_result


def test_process_bank_search_no_results():
    data = [
        {"description": "Заправка автомобиля"},
        {"description": "Покупка продуктов"},
        {"description": "Передача средств"},
        {"description": "Заправка моторного масла"},
        {"description": "Оплата коммунальных услуг"},
    ]

    search_term = "платеж"

    expected_result = []

    result = process_bank_search(data, search_term)

    assert result == expected_result


if __name__ == "__main__":
    pytest.main()


