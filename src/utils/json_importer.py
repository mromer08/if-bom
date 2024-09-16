import json
from src.models.resource.sheet import Sheet
from src.models.resource.sheet_type import SheetType
from src.models.resource.supply import Supply
from src.models.resource.supply_type import SupplyType

def load_sheets_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        sheets = []
        for sheet_data in data["sheets"]:
            sheet = Sheet(
                name=sheet_data["name"],
                sheet_type=SheetType[sheet_data["sheet_type"].replace(" ", "_").upper()],
                price_per_square_meter=sheet_data["price_per_square_meter"],
                width=sheet_data["width"] / 1000,  # Convert mm to meters
                length=sheet_data["length"] / 1000,  # Convert mm to meters
                thickness=sheet_data["thickness"] / 1000  # Convert mm to meters
            )
            sheets.append(sheet)
        return sheets

def load_supplies_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        supplies = []
        for supply_data in data["supplies"]:
            supply = Supply(
                name=supply_data["name"],
                price=supply_data["price"],
                supply_type=SupplyType[supply_data["supply_type"].replace(" ", "_").upper()]
            )
            supplies.append(supply)
        return supplies
