from enum import Enum

class CabinetType(Enum):
    BASE_CABINET = "Base Cabinet"
    WALL_CABINET = "Wall Cabinet"
    CLOSET_MODULE = "Closet Module"
    FLOATING_CABINET = "Floating Cabinet"
    THICKENED_VOLUME = "Thickened Volume"

    def __str__(self):
        return self.value
