import logging
import os
from typing import Union

# Создаем папку logs
os.makedirs("logs", exist_ok=True)

# Настройка логирования
logging.basicConfig(
    filename="logs/masks.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: Union[str, int, None]) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX"""
    if card_number is None:
        logger.error("Номер карты не может быть None.")
        raise ValueError("Номер карты не может быть None.")

    # Преобразуем в строку и очищаем номер от нецифровых символов
    digits = "".join(filter(str.isdigit, str(card_number)))

    # Проверяем длину
    if len(digits) != 16:
        logger.error("Номер карты должен содержать 16 цифр. Получено: %d", len(digits))
        raise ValueError(f"Номер карты должен содержать 16 цифр. Получено: {len(digits)}")

    # Формируем маскированный номер
    masked_card_number = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    logger.info("Маскированный номер карты: %s", masked_card_number)
    return masked_card_number


def get_mask_account(account_number: Union[str, int, None]) -> str:
    """Маскирует номер счета в формате **XXXX"""
    if account_number is None:
        logger.error("Номер счета не может быть None.")
        raise ValueError("Номер счета не может быть None.")

    # Преобразуем в строку и очищаем номер от нецифровых символов
    digits = "".join(filter(str.isdigit, str(account_number)))

    # Проверяем длину
    if len(digits) != 20:
        logger.error("Номер счета должен содержать 20 цифр. Получено: %d", len(digits))
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Возвращаем маскированный номер в формате **XXXX
    masked_account_number = f"**{digits[-4:]}"
    logger.info("Маскированный номер счета: %s", masked_account_number)
    return masked_account_number
