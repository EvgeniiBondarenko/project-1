import pytest
from unittest.mock import mock_open
from src.utils import load_transactions

def test_load_transactions_empty_file(mocker):
    """Тест на загрузку пустого файла."""
    mocker.patch("builtins.open", mock_open(read_data='[]'))
    result = load_transactions("fake_path.json")
    assert result == []

def test_load_transactions_invalid_json(mocker):
    """Тест на загрузку невалидного JSON."""
    mocker.patch("builtins.open", mock_open(read_data='not a json'))
    result = load_transactions("fake_path.json")
    assert result == []

def test_load_transactions_file_not_found(mocker):
    """Тест на случай отсутствия файла."""
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    result = load_transactions("fake_path.json")
    assert result == []

def test_load_transactions_success(mocker):
    """Тест на успешную загрузку данных из JSON."""
    mocker.patch("builtins.open", mock_open(read_data='[{"amount": 100, "currency": "USD"}]'))
    result = load_transactions("fake_path.json")
    assert result == [{"amount": 100, "currency": "USD"}]

