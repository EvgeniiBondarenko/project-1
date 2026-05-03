from optparse import Option
from typing import Optional

from mypy.state import state


def filter_by_state(transactions: List[Dict[str, str]], state:: Optional[str] = 'EXECUTED') -> List[Dict[str, str]]:
    """Фильтация через цикл цикл for"""
    result = []
    for item in transactions:
        if item.get('state') == state:
            result.append(item)
    return result

