import json
import logging
import os
from typing import Any, Dict, List

# Создаем папку logs
os.makedirs("logs", exist_ok=True)

# Настройка логирования
logging.basicConfig(
    filename="logs/utils.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Транзакции успешно загружены из %s", file_path)
                return data
            else:
                logger.warning("Данные в файле %s не являются списком", file_path)
    except FileNotFoundError:
        logger.error("Файл не найден: %s", file_path)
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON в файле: %s", file_path)
    return []
