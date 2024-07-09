import pandas as pd
from datetime import datetime
from TC_ABC import TransportCompany


class Company1(TransportCompany):

    def calculate_delivery(self, from_location, to_location, weight, volume, max_dimension):
        delivery_options = [
            {"service": "Стандартная Доставка", "cost": 1000, "days": 5},
            {"service": "Быстрая Доставка", "cost": 2000, "days": 2}
        ]
        return delivery_options

    def register_order(self, order_details):
        df = pd.DataFrame([order_details])
        try:
            existing_df = pd.read_excel('orders_company_1.xlsx')
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_excel('orders_company_1.xlsx', index=False)

    def get_orders(self, date_filter=None):
        df = pd.read_excel('orders_company_1.xlsx')
        if date_filter:
            df = df[df['order_date'] == date_filter]
        return df.to_dict(orient='records')
