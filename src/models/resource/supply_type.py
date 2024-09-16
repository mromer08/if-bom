from enum import Enum

class SupplyType(Enum):
    PRODUCTION = "Production"
    INSTALLATION = "Installation"

    def __str__(self):
        return self.value
