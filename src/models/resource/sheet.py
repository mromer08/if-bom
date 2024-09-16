from .resource import Resource
from .sheet_type import SheetType

class Sheet(Resource):
    def __init__(self, name, sheet_type, price_per_square_meter, width, length, thickness):
        super().__init__(name, price_per_square_meter, unit_of_measure='square_meter')
        self.sheet_type = sheet_type      # Instance of SheetType enum
        self.width = width               # Width in meters
        self.length = length             # Length in meters
        self.thickness = thickness       # Thickness in meters

    def get_area(self):
        return self.width * self.length

    def get_volume(self):
        return self.get_area() * self.thickness

    def get_cost(self, area=None):
        if area is None:
            area = self.get_area()
        return super().get_cost(quantity=area)

    def __repr__(self):
        return (f"{self.name} ({self.sheet_type}, {self.width}m x {self.length}m x {self.thickness}m) "
                f"- ${self.price} per {self.unit_of_measure}")
