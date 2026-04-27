from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимает строку с типом и номером карты или счета, возврощает замоскированный результат"""

    name, number = data.rsplit(" ", 1)
    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{name} {masked_number}"


def get_data(data_string: str) -> str:
    """принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" """
    return f"{data_string[8:10]}.{data_string[5:7]}.{data_string[0:4]}"
