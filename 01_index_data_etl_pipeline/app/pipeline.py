from pathlib import Path
import pandas as pd
from app.validation import validate_prices
from app.calculation import calculate_index
from app.database import initialize_database
from app.repository import save_prices_and_snapshots

def run_pipeline(input_path: str, output_dir: str = "output"):
    raw = pd.read_csv(input_path)
    clean = validate_prices(raw)
    snapshots = calculate_index(clean)
    initialize_database()
    save_prices_and_snapshots(clean, snapshots)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    clean.to_csv(out / "validated_prices.csv", index=False)
    snapshots.to_csv(out / "index_snapshots.csv", index=False)
    return snapshots
