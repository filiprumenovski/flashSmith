import csv

def load_and_validate_csv(path: str):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = ["Deck", "Subdeck", "Type", "Front", "Back"]
        for field in required:
            if field not in reader.fieldnames:
                raise ValueError(f"Missing required column: {field}")
        for row in reader:
            rows.append(row)
    return rows
