from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX"""

    # Очищаем номер от нецифровых символов
    digits = "".join(filter(str.isdigit, str(card_number)))
    # Проверяем длину
    if len(digits) != 16:
        raise ValueError(f"Номер карты должен содержать 16 цифр. Получено: {len(digits)}")
    # Формируем маскировачный номер
    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Маскирует номер счета в формате **XXXX"""

    # Очищаем номер от нецифровых символов
    digits = "".join(filter(str.isdigit, str(account_number)))

    # Проверяем длину
    if len(digits) != 20:
        raise ValueError(f"Номер счета должен содержать 20 цифр.")

    # Возвращаем маскированный номер в формате **XXXX
    return f"**{digits[-4:]}"
