from abc import ABC, abstractmethod


class TransportCompany(ABC):

    @abstractmethod
    def calculate_delivery(self, from_location, to_location, weight, volume, max_dimension):
        pass

    @abstractmethod
    def register_order(self, order_details):
        pass

    @abstractmethod
    def get_orders(self, date_filter=None):
        pass
