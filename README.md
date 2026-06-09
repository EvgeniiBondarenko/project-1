# Проект разработки банковского приложения
## Модуль чтения финансовых операций

Описание и примеры использования:

### Функции
- `read_financial_operations_from_csv(file_path: str = 'htmlcov/transactions.csv') -> List[Dict[str, Any]]`
  - Читает CSV-файл с транзакциями.
  - Параметры:
    - `file_path` — путь к CSV-файлу. Значение по умолчанию: `htmlcov/transactions.csv`.
  - Возвращает: список словарей, где каждый словарь представляет одну транзакцию.
  - Реализация:
    - Используется модуль `csv` и `DictReader`.
    - Каждая строка CSV преобразуется в словарь и добавляется в результат.

- `read_financial_operations_from_excel(file_path: str = 'htmlcov/transactions_excel.xlsx') -> List[Dict[str, Any]]`
  - Читает Excel-файл с транзакциями.
  - Параметры:
    - `file_path` — путь к Excel-файлу. Значение по умолчанию: `htmlcov/transactions_excel.xlsx`.
  - Возвращает: список словарей, где каждый словарь представляет одну транзакцию.
  - Реализация:
    - Используется `pandas` и метод `read_excel`.
    - Приводятся типы через `cast` к `List[Dict[str, Any]]` с помощью `to_dict(orient='records')`.

### Форматы возвращаемых данных
- Результат — список словарей: `List[Dict[str, Any]]`.
- Каждый словарь содержит поля, соответствующие столбцам входного файла CSV/Excel.

### Пример использования
```python
from typing import List, Dict, Any

csv_path = 'htmlcov/transactions.csv'
excel_path = 'htmlcov/transactions_excel.xlsx'

from your_module import (
    read_financial_operations_from_csv,
    read_financial_operations_from_excel,
)

csv_transactions: List[Dict[str, Any]] = read_financial_operations_from_csv(csv_path)
excel_transactions: List[Dict[str, Any]] = read_financial_operations_from_excel(excel_path)

print(f"CSV транзакций: {len(csv_transactions)}")
print(f"Excel транзакций: {len(excel_transactions)}")
```

### Тесты
Рекомендуется использовать `pytest`.

- Установка:
  - `pip install pytest pandas openpyxl`

- Пример структуры тестов:
```
tests/
├── test_csv_reader.py
├── test_excel_reader.py
└── conftest.py
```

- Пример теста для CSV:
```python
# tests/test_csv_reader.py
from your_module import read_financial_operations_from_csv


def test_read_csv_default_path(tmp_path, monkeypatch):
    # Подменяем путь на временный тестовый файл
    csv_path = tmp_path / 'transactions.csv'
    csv_path.write_text('date,amount,description\n2026-01-01,100.0,test')
    data = read_financial_operations_from_csv(str(csv_path))
    assert isinstance(data, list)
    assert data[0]['date'] == '2026-01-01'
```

- Пример теста для Excel:
```python
# tests/test_excel_reader.py
from your_module import read_financial_operations_from_excel
import pandas as pd


def test_read_excel_default_path(tmp_path):
    excel_path = tmp_path / 'transactions_excel.xlsx'
    df = pd.DataFrame([
        {'date': '2026-01-02', 'amount': 50, 'description': 'test2'}
    ])
    df.to_excel(excel_path, index=False)
    data = read_financial_operations_from_excel(str(excel_path))
    assert isinstance(data, list)
    assert data[0]['date'] == '2026-01-02'
```

- Конфигурация окружения, вспомогательные фикстуры, обработка исключений — по необходимости.

### Логика и ограничения
- По умолчанию используются файлы `htmlcov/transactions.csv` и `htmlcov/transactions_excel.xlsx`.
- Для Excel требуется пакет `pandas` и `openpyxl` (или другой движок, поддерживаемый `read_excel`).
- Результат приведён к `List[Dict[str, Any]]`.
