import pytest
from unittest import mock
from src.finance_reader import read_financial_operations_from_csv, read_financial_operations_from_excel
from typing import List, Dict, Any


@pytest.fixture
def mock_csv_file() -> str:
    return 'htmlcov/transactions.csv'


@pytest.fixture
def mock_excel_file() -> str:
    return 'htmlcov/transactions_excel.xlsx'


def test_read_financial_operations_from_csv(mock_csv_file: str) -> None:
    # Пример данных CSV
    mock_open = mock.mock_open(read_data='date,amount,description\n'
                                         '2023-03-01,1000,Salary\n'
                                         '2023-03-02,200,Groceries\n')

    with mock.patch('builtins.open', mock_open):
        result: List[Dict[str, Any]] = read_financial_operations_from_csv(mock_csv_file)
        assert len(result) == 2
        assert result[0] == {'date': '2023-03-01', 'amount': '1000', 'description': 'Salary'}
        assert result[1] == {'date': '2023-03-02', 'amount': '200', 'description': 'Groceries'}


def test_read_financial_operations_from_excel(mock_excel_file: str) -> None:
    # Создаем mock для pandas.read_excel
    with mock.patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value.to_dict.return_value = [
            {'date': '2023-03-01', 'amount': 1000, 'description': 'Salary'},
            {'date': '2023-03-02', 'amount': 200, 'description': 'Groceries'}
        ]

        result: List[Dict[str, Any]] = read_financial_operations_from_excel(mock_excel_file)
        assert len(result) == 2
        assert result[0] == {'date': '2023-03-01', 'amount': 1000, 'description': 'Salary'}
        assert result[1] == {'date': '2023-03-02', 'amount': 200, 'description': 'Groceries'}

