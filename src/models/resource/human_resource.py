from .resource import Resource
class HumanResource(Resource):
    def __init__(self, name, price):
        super().__init__(name, price, unit_of_measure='hour')

    def get_cost(self, hours):
        return super().get_cost(quantity=hours)
