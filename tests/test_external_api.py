import pytest
from src.external_api import convert_to_rubles

def test_convert_to_rubles_success(mocker):
    """Тест на успешное преобразование валюты с API."""
    # Mock the API response
    mock_get = mocker.patch('src.external_api.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 1000}

    transaction = {'amount': 100, 'currency': 'USD'}
    result = convert_to_rubles(transaction)
    assert result == 1000.0

def test_convert_to_rubles_failure(mocker):
    """Тест на обработку ошибки при конвертации валюты."""
    # Mock the API response for failure scenario
    mock_get = mocker.patch('src.external_api.requests.get')
    mock_get.return_value.status_code = 400
    mock_get.return_value.json.return_value = {}

    transaction = {'amount': 100, 'currency': 'USD'}
    with pytest.raises(ValueError, match="Не удалось получить данные о валюте"):
        convert_to_rubles(transaction)

def test_convert_to_rubles_rub():
    """Тест на преобразование уже в рублях."""
    transaction = {'amount': 100, 'currency': 'RUB'}  # Тщательно определяем переменную
    result = convert_to_rubles(transaction)
    assert result == 100.0


