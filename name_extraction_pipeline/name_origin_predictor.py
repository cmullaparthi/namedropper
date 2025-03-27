"""
name_origin_predictor.py

Simple name-to-origin model backed by a CSV dataset (based on name-prism-like logic).
"""

import csv
from pathlib import Path

DATA = {}

def load_data():
    global DATA
    path = Path(__file__).parent / "data" / "name_origin_lookup.csv"
    if not path.exists():
        return
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            DATA[row["name"].lower()] = (row["lang"], float(row["confidence"]))

def predict_origin(name: str) -> tuple[str, float]:
    if not DATA:
        load_data()
    tokens = name.lower().split()
    if not tokens:
        return "xx", 0.0
    return DATA.get(tokens[0], ("xx", 0.3))
