import pandas as pd

REQUIRED = {"trade_date", "symbol", "close", "shares_outstanding"}

class DataQualityError(ValueError):
    pass

def validate_prices(frame: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(frame.columns)
    if missing:
        raise DataQualityError(f"Missing required columns: {sorted(missing)}")
    df = frame[list(REQUIRED)].copy()
    if df.empty:
        raise DataQualityError("Input contains no records")
    df["trade_date"] = pd.to_datetime(df["trade_date"], errors="coerce").dt.date
    df["symbol"] = df["symbol"].astype("string").str.strip().str.upper()
    for col in ("close", "shares_outstanding"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    if df[["trade_date", "symbol", "close", "shares_outstanding"]].isna().any().any():
        raise DataQualityError("Null or invalid values found in required fields")
    if (df["close"] <= 0).any() or (df["shares_outstanding"] <= 0).any():
        raise DataQualityError("Prices and shares outstanding must be positive")
    if df.duplicated(["trade_date", "symbol"]).any():
        raise DataQualityError("Duplicate symbol/date records found")
    return df.sort_values(["trade_date", "symbol"]).reset_index(drop=True)
