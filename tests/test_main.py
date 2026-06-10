import pytest
from unittest.mock import patch, MagicMock
from src.main import main


# Пример тестовых данных
test_data = [
    {'description': 'Открытие вклада', 'amount': 40542, 'currency': 'руб.', 'date': '2019-12-08', 'account': 'Счет 1234'},
    {'description': 'Перевод с карты на карту', 'amount': 130, 'currency': 'USD', 'date': '2019-11-12', 'account': 'Счет 5678'},
    {'description': 'Перевод со счета на счет', 'amount': 8200, 'currency': 'EUR', 'date': '2018-06-03', 'account': 'Счет 9101'},
]

# Mock функции для чтения файлов
def mock_load_transactions(filename):
    return test_data

def mock_read_financial_operations_from_csv(filename):
    return test_data

def mock_read_financial_operations_from_excel(filename):
    return test_data


@patch('src.main.load_transactions', side_effect=mock_load_transactions)
@patch('src.main.read_financial_operations_from_csv', side_effect=mock_read_financial_operations_from_csv)
@patch('src.main.read_financial_operations_from_excel', side_effect=mock_read_financial_operations_from_excel)
@patch('builtins.input', side_effect=[
    '1',                 # Выбор JSON
    'fakefile.json',    # Имя файла
    'EXECUTED',         # Статус
    'да',               # Сортировка по дате
    'по возрастанию',   # Возврат по возрастанию
    'да',               # Выводить только рублевые транзакции
    'да',               # Фильтр по слову в описании
    'Открытие'          # Слово для фильтрации
])
@patch('builtins.print')
def test_main(mock_print, mock_input, mock_csv, mock_excel):
    main()

    # Проверка вывода
    mock_print.assert_any_call("Всего банковских операций в выборке: 1")
    mock_print.assert_any_call("08.12.2019 Открытие вклада")
    mock_print.assert_any_call("Счет 1234")
    mock_print.assert_any_call("Сумма: 40542 руб.\n")

    # Проверка, что фильтрация по статусу сработала
    assert len(mock_csv.call_args) == 1  # Проверяем, что вызывался вызов на чтение CSV
    assert len(mock_excel.call_args) == 0  # Проверяем, что Excel не вызывался




