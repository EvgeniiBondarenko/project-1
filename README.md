# Проект разработки банковского приложения

## Описание

Создание виджета банковских операций клиента. В проекте реализованы функции для фильтрации транзакций, сортировки по дате, генерации номеров карт и описания транзакций.

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/EvgeniiBondarenko/project-1/pull/1
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Модули

### Модуль генераторов (`generators`)

Предоставляет функции для работы со списками транзакций и генерации номеров карт.

#### `filter_by_currency(transactions, currency)`

Фильтрует транзакции по заданной валюте.

```python
from generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод"},
    {"operationAmount": {"currency": {"code": "RUB"}}, "description": "Оплата"},
]

usd_transactions = list(filter_by_currency(transactions, "USD"))
# [{"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод"}]
```

#### `transaction_descriptions(transactions)`

Возвращает описания транзакций одну за другой (генератор).

```python
from generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
print(next(descriptions))  # "Перевод"
print(next(descriptions))  # "Оплата"
```

#### `card_number_generator(start, stop)`

Генерирует номера карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне.

```python
from generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
```

### Модуль сортировки (`sorting`)

Содержит функцию `sort_by_date`, которая сортирует список транзакций по дате.

```python
from sorting import sort_by_date

transactions = [
    {"date": "2024-01-15", "amount": 100},
    {"date": "2023-12-01", "amount": 200},
    {"date": "2024-06-20", "amount": 150},
]

sorted_asc = sort_by_date(transactions, descending=False)
# [
#   {"date": "2023-12-01", "amount": 200},
#   {"date": "2024-01-15", "amount": 100},
#   {"date": "2024-06-20", "amount": 150},
# ]

sorted_desc = sort_by_date(transactions)
# [
#   {"date": "2024-06-20", "amount": 150},
#   {"date": "2024-01-15", "amount": 100},
#   {"date": "2023-12-01", "amount": 200},
# ]
```

## Тестирование

Проект покрыт тестами с использованием [pytest](https://docs.pytest.org/).

### Установка зависимостей для тестов

```bash
pip install -r requirements.txt
pip install pytest
```

### Запуск тестов

```bash
pytest
```

Для запуска тестов с выводом покрытия кода:

```bash
pytest --cov=
```

### Пример вывода

```
============================= test session starts ==============================
collected 12 items

tests/test_module1.py ..... [ 50%]
tests/test_module2.py ...... [100%]

=========================== 12 passed in 0.45s =============================
