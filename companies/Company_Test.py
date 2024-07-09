from datetime import datetime
from TC_ABC import TransportCompany


class CompanyTest(TransportCompany):

    def calculate_delivery(self, from_location, to_location, weight, volume, max_dimension):
        delivery_options = [
            {"service": "Эконом Доставка", "cost": 700, "days": 14},
            {"service": "Экспресс Доставка", "cost": 4100, "days": 1}
        ]
        return delivery_options

    def register_order(self, order_details):
        with open('orders_company_test.txt', 'a') as file:
            file.write(str(order_details) + '\n')

    def get_orders(self, date_filter=None):
        orders = []
        with open('orders_company_test.txt', 'r') as file:
            for line in file:
                order = eval(line.strip())
                if not date_filter or order['order_date'] == date_filter:
                    orders.append(order)
        return orders