import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстуры для тестирования
@pytest.fixture
def transaction_data():
    return [
        {"id": 1, "date": "2023-10-02", "state": "EXECUTED"},
        {"id": 2, "date": "2023-10-03", "state": "PENDING"},
        {"id": 3, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 4, "date": "2023-10-04", "state": "EXECUTED"},
        {"id": 5, "date": "2023-10-01", "state": "PENDING"},
    ]


@pytest.fixture
def transaction_data_with_duplicates():
    return [
        {"id": 1, "date": "2023-10-03", "state": "EXECUTED"},
        {"id": 2, "date": "2023-10-03", "state": "PENDING"},
        {"id": 3, "date": "2023-10-03", "state": "EXECUTED"},
        {"id": 4, "date": "2023-10-02", "state": "EXECUTED"},
    ]


@pytest.fixture
def transaction_data_with_invalid_dates():
    return [
        {"id": 1, "date": "invalid_date", "state": "EXECUTED"},
        {"id": 2, "date": "2023-10-03", "state": "PENDING"},
        {"id": 3, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 4, "date": "2023-10-04", "state": "EXECUTED"},
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 3),      # Ожидаем 3 EXECUTED
    ("PENDING", 2),       # Ожидаем 2 PENDING
    ("NONEXISTENT", 0),   # Ожидаем 0
])
def test_filter_by_state(transaction_data, state, expected_count):
    results = filter_by_state(transaction_data, state)
    assert len(results) == expected_count
    if expected_count > 0:
        for item in results:
            assert item['state'] == state


def test_filter_by_state_no_matches(transaction_data):
    results = filter_by_state(transaction_data, "NONEXISTENT")
    assert results == []


# Тесты для sort_by_date
def test_sort_by_date_desc(transaction_data):
    sorted_transactions = sort_by_date(transaction_data)
    assert sorted_transactions[0]['date'] == "2023-10-04"
    assert sorted_transactions[-1]['date'] == "2023-10-01"


def test_sort_by_date_asc(transaction_data):
    sorted_transactions_ascending = sort_by_date(transaction_data, descending=False)
    assert sorted_transactions_ascending[0]['date'] == "2023-10-01"
    assert sorted_transactions_ascending[-1]['date'] == "2023-10-04"


def test_sort_by_date_with_duplicates(transaction_data_with_duplicates):
    sorted_transactions = sort_by_date(transaction_data_with_duplicates)
    assert sorted_transactions[0]['date'] == "2023-10-03"  # Наивысшая дата
    assert sorted_transactions[1]['date'] == "2023-10-03"  # Вторая дата с дубликатом
    assert sorted_transactions[-1]['date'] == "2023-10-02" # Наименьшая