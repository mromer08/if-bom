from .resource import Resource
from .supply_type import SupplyType

class Supply(Resource):
    def __init__(self, name, price, supply_type):
        super().__init__(name, price, unit_of_measure='unit')
        self.supply_type = supply_type

    def get_cost(self, quantity=1):
        return super().get_cost(quantity)

    def __repr__(self):
        return f"{self.name} ({self.supply_type}, {self.unit_of_measure}) - ${self.price} per unit"
