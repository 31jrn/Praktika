import json
from datetime import datetime
from Company_1 import Company1
from Company_2 import Company2
from Company_3 import Company3


def main():
    companies = {
        "1": Company1(),
        "2": Company2(),
        "3": Company3()
    }

    while True:
        print("\nВыберите действие:")
        print("1. Рассчитать доставку")
        print("2. Зарегистрировать заказ")
        print("3. Получить список заказов")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            company_choice = input("Выберите компанию (1, 2, 3): ")
            if company_choice not in companies:
                print("Неверный выбор компании.")
                continue

            from_location = input("Откуда: ")
            to_location = input("Куда: ")
            weight = float(input("Вес: "))
            volume = float(input("Объем: "))
            max_dimension = float(input("Максимальный габарит: "))

            delivery_options = companies[company_choice].calculate_delivery(from_location, to_location, weight, volume,
                                                                            max_dimension)
            print("\nВарианты доставки:")
            for idx, option in enumerate(delivery_options):
                print(
                    f"{idx + 1}. Услуга: {option['service']}, Стоимость: {option['cost']}, Срок доставки: {option['days']} дней")

            selected_option = int(input("Выберите вариант доставки (номер): ")) - 1
            if selected_option < 0 or selected_option >= len(delivery_options):
                print("Неверный выбор варианта доставки.")
                continue

            chosen_delivery = delivery_options[selected_option]
            print(f"Вы выбрали: {chosen_delivery['service']}")

            order_details = {
                "from_location": from_location,
                "to_location": to_location,
                "weight": weight,
                "volume": volume,
                "max_dimension": max_dimension,
                "recipient_name": input("ФИО получателя: "),
                "contact_phone": input("Контактный телефон: "),
                "order_date": datetime.now().strftime("%d-%m-%Y"),
                "service": chosen_delivery["service"],
                "cost": chosen_delivery["cost"],
                "days": chosen_delivery["days"]
            }

            companies[company_choice].register_order(order_details)
            print("Заказ зарегистрирован.")

        elif choice == "2":
            company_choice = input("Выберите компанию (1, 2, 3): ")
            if company_choice not in companies:
                print("Неверный выбор компании.")
                continue

            from_location = input("Откуда: ")
            to_location = input("Куда: ")
            weight = float(input("Вес: "))
            volume = float(input("Объем: "))
            max_dimension = float(input("Максимальный габарит: "))

            delivery_options = companies[company_choice].calculate_delivery(from_location, to_location, weight, volume,
                                                                            max_dimension)
            print("\nВарианты доставки:")
            for idx, option in enumerate(delivery_options):
                print(
                    f"{idx + 1}. Услуга: {option['service']}, Стоимость: {option['cost']}, Срок доставки: {option['days']} дней")

            selected_option = int(input("Выберите вариант доставки (номер): ")) - 1
            if selected_option < 0 or selected_option >= len(delivery_options):
                print("Неверный выбор варианта доставки.")
                continue

            chosen_delivery = delivery_options[selected_option]
            print(f"Вы выбрали: {chosen_delivery['service']}")

            order_details = {
                "from_location": from_location,
                "to_location": to_location,
                "weight": weight,
                "volume": volume,
                "max_dimension": max_dimension,
                "recipient_name": input("ФИО получателя: "),
                "contact_phone": input("Контактный телефон: "),
                "order_date": datetime.now().strftime("%d-%m-%Y"),
                "service": chosen_delivery["service"],
                "cost": chosen_delivery["cost"],
                "days": chosen_delivery["days"]
            }

            companies[company_choice].register_order(order_details)
            print("Заказ зарегистрирован.")

        elif choice == "3":
            company_choice = input("Выберите компанию (1, 2, 3): ")
            if company_choice not in companies:
                print("Неверный выбор компании.")
                continue

            date_filter = input("Введите дату для фильтрации (дд-мм-гггг) или оставьте пустым для всех заказов: ")
            date_filter = date_filter if date_filter else None

            orders = companies[company_choice].get_orders(date_filter)
            if orders:
                try:
                    orders.sort(key=lambda x: datetime.strptime(x['order_date'], "%d-%m-%Y"))
                except ValueError as e:
                    print(f"Ошибка при сортировке заказов: {e}")
                    continue
            print("\nСписок заказов:")
            for order in orders:
                print(json.dumps(order, ensure_ascii=False, indent=4))

        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()
