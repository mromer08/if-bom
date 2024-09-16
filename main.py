from src.utils import load_sheets_from_json, load_supplies_from_json

if __name__ == "__main__":
    # Load the sheet data
    sheets = load_sheets_from_json("data/sheets.json")
    installation_supplies = load_supplies_from_json("data/installation_supplies.json")
    production_supplies = load_supplies_from_json("data/production_supplies.json")
    
    # Print all the sheets
    print("Imported Sheets (Materials):")
    for sheet in sheets:
        print(sheet)
    
    # Print all the supplies
    print("\nImported INSTALLATION Supplies:")
    for supply in installation_supplies:
        print(supply)

        # Print all the supplies
    print("\nImported PRODUCTION Supplies:")
    for supply in production_supplies:
        print(supply)
