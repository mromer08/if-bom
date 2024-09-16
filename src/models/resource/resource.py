class Resource:
    def __init__(self, name, price, unit_of_measure):
        self.name = name
        self.price = price
        self.unit_of_measure = unit_of_measure

    def get_cost(self, quantity=1):
        return self.price * quantity

    def __repr__(self):
        return f"{self.name} ({self.unit_of_measure}) - ${self.price}"
