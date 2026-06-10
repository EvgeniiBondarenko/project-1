from src.finance_reader import read_financial_operations_from_csv, read_financial_operations_from_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_data, mask_account_card


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    filename = input("Введите имя файла: ")

    if choice == "1":
        transactions = load_transactions(filename)
    elif choice == "2":
        transactions = read_financial_operations_from_csv(filename)
    elif choice == "3":
        transactions = read_financial_operations_from_excel(filename)
    else:
        print("Неверный выбор.")
        return

    # Фильтрация по статусу
    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = ""

    while status not in statuses:
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )
        if status not in statuses:
            print(f"Статус операции '{status}' недоступен.")

    print(f"Операции отфильтрованы по статусу '{status}'")

    filtered_transactions = filter_by_state(transactions, status)

    # Сортировка
    sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower() == "да"
    if sort_by_date_choice:
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        reverse = order == "по убыванию"
        filtered_transactions = sort_by_date(filtered_transactions, descending=reverse)

    # Фильтрация по валюте
    only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower() == "да"
    if only_rub:
        filtered_transactions = [t for t in filtered_transactions if t.get("currency") == "руб."]

    # Фильтрация по описанию
    filter_by_description = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower() == "да"
    )
    if filter_by_description:
        search_term = input("Введите слово для фильтрации:\n").strip()
        filtered_transactions = [
            t for t in filtered_transactions if search_term.lower() in t.get("description", "").lower()
        ]

    # Печать итогового списка транзакций
    print("Распечатываю итоговый список транзакций...\n")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            date_str = get_data(transaction["date"])  # Форматируем дату
            masked_account = mask_account_card(transaction["account"]) if "account" in transaction else ""
            print(f"{date_str} {transaction['description']}")
            print(masked_account)
            print(f"Сумма: {transaction['amount']} {transaction['currency']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
