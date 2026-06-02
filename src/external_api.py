import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/"
API_KEY = os.getenv("API_KEY")


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли.

    Аргументы:
        transaction: Словарь с данными о транзакции, содержащий 'amount' и 'currency'.

    Возвращает:
        Сумму транзакции в рублях.

    Исключения:
        ValueError: если не удается получить данные о валюте.
    """

    amount: float = transaction["amount"]  # Указываем, что amount - это float
    currency: str = transaction["currency"]  # Указываем, что currency - это string

    if currency == "RUB":
        return amount  # Здесь amount уже в рублях

    # Запрос на конвертацию валюты
    response = requests.get(f"{API_URL}convert?from={currency}&to=RUB&amount={amount}&apikey={API_KEY}")

    if response.status_code == 200:
        response_data = response.json()
        return float(response_data.get("result", 0))  # Возвращаем конвертированную сумму

    raise ValueError("Не удалось получить данные о валюте.")  # Если запрос завершился неудачей
