import functools
import logging
from typing import Any, Callable, Optional

"""Декоратор для логирования вызовов функции.

    Логирует начало и завершение выполнения функции, а также любые ошибки,
    которые могут возникнуть во время ее исполнения.
"""


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def decorator_log(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logging.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok, result: {result}")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator_log
