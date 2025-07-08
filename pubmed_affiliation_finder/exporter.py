# pubmed_affiliation_finder/exporter.py

import pandas as pd
from typing import List, Dict

def export_to_csv(data: List[Dict], filename: str):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(df)} records to {filename}")

def print_to_console(data: List[Dict]):
    df = pd.DataFrame(data)
    print(df.to_markdown())
