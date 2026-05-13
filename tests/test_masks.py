import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Тестовые случаи для функции get_mask_card_number
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    assert get_mask_card_number("    1234-5678-1234-5678    ") == "1234 56** **** 5678"

    # Проверка на ошибку с неправильной длиной
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("1234")  # Короче 16

    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("12345678123456789")  # Дольше 16


def test_get_mask_account():
    # Тестовые случаи для функции get_mask_account
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account("    12345678901234567890    ") == "**7890"

    # Проверка на ошибку с неправильной длиной
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр"):
        get_mask_account("123456")  # Короче 20

    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр"):
        get_mask_account("123456789012345678901")  # Дольше 20

