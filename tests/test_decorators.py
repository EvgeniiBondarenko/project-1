import pytest
import logging
from src.decorators import log


# Пример декорируемых функций
@log()
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b  # Будет деление на ноль


@log()
def raise_error():
    raise ValueError("This is a test error")


def test_add(caplog):
    with caplog.at_level(logging.INFO):
        result = add(2, 3)

    # Проверка результата
    assert result == 5

    # Проверка логов
    assert "Starting add with args: (2, 3), kwargs: {}" in caplog.text
    assert "add ok, result: 5" in caplog.text


def test_divide(caplog):
    with caplog.at_level(logging.INFO):
        result = divide(10, 2)

    # Проверка результата
    assert result == 5.0

    # Проверка логов
    assert "Starting divide with args: (10, 2), kwargs: {}" in caplog.text
    assert "divide ok, result: 5.0" in caplog.text


def test_divide_by_zero(caplog):
    with caplog.at_level(logging.INFO):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    # Проверка логов
    assert "Starting divide with args: (10, 0), kwargs: {}" in caplog.text
    assert "divide error: division by zero. Inputs: (10, 0), {}" in caplog.text


def test_raise_error(caplog):
    with caplog.at_level(logging.INFO):
        with pytest.raises(ValueError, match="This is a test error"):
            raise_error()

    # Проверка логов
    assert "Starting raise_error with args: (), kwargs: {}" in caplog.text
    assert "raise_error error: This is a test error. Inputs: (), {}" in caplog.text



