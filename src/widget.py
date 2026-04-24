from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимает строку с типом и номером карты или счета, возврощает замоскированный результат"""

    name, number = data.rsplit(" ", 1)
    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{name} {masked_number}"
