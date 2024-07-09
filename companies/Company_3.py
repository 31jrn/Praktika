from datetime import datetime
from TC_ABC import TransportCompany


class Company3(TransportCompany):

    def calculate_delivery(self, from_location, to_location, weight, volume, max_dimension):
        delivery_options = [
            {"service": "Эконом Доставка", "cost": 500, "days": 10},
            {"service": "Экспресс Доставка", "cost": 3000, "days": 1}
        ]
        return delivery_options

    def register_order(self, order_details):
        with open('orders_company_3.txt', 'a') as file:
            file.write(str(order_details) + '\n')

    def get_orders(self, date_filter=None):
        orders = []
        with open('orders_company_3.txt', 'r') as file:
            for line in file:
                order = eval(line.strip())
                if not date_filter or order['order_date'] == date_filter:
                    orders.append(order)
        return orders