import sqlite3
from TC_ABC import TransportCompany


class Company2(TransportCompany):

    def __init__(self):
        self.db_file = 'orders_company_2.db'
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS orders
                       (from_location TEXT, to_location TEXT, weight REAL, volume REAL,
                        max_dimension REAL, recipient_name TEXT, contact_phone TEXT, 
                        order_date TEXT, service TEXT, cost REAL, days INTEGER)''')
        conn.commit()
        conn.close()

    def calculate_delivery(self, from_location, to_location, weight, volume, max_dimension):
        delivery_options = [
            {"service": "Стандартная Доставка", "cost": 800, "days": 7},
            {"service": "Премиум Доставка", "cost": 2500, "days": 1}
        ]
        return delivery_options

    def register_order(self, order_details):
        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            cur.execute('''INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        tuple(order_details.values()))
            conn.commit()
            conn.close()
        except sqlite3.DatabaseError as e:
            print(f"Ошибка при работе с базой данных: {e}")

    def get_orders(self, date_filter=None):
        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            if date_filter:
                cur.execute('''SELECT * FROM orders WHERE order_date=?''', (date_filter,))
            else:
                cur.execute('''SELECT * FROM orders''')
            rows = cur.fetchall()
            conn.close()

            # Преобразование кортежей в словари
            columns = ["from_location", "to_location", "weight", "volume", "max_dimension", "recipient_name",
                       "contact_phone", "order_date", "service", "cost", "days"]
            orders = [dict(zip(columns, row)) for row in rows]
            return orders
        except sqlite3.DatabaseError as e:
            print(f"Ошибка при работе с базой данных: {e}")
            return []
