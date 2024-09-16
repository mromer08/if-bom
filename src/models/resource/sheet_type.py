from enum import Enum

class SheetType(Enum):
    WOOD = "Wood"
    MELAMINE = "Melamine"
    QUARTZ = "Quartz"
    MDF = "MDF"
    HIGH_GLOSS_MDF = "High Gloss MDF"
    PAPERBOARD = "Paperboard"

    def __str__(self):
        return self.value
