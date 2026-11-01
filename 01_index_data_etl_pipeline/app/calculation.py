import pandas as pd

def calculate_index(prices: pd.DataFrame, base_value: float = 1000.0) -> pd.DataFrame:
    if base_value <= 0:
        raise ValueError("base_value must be positive")
    df = prices.copy()
    df["market_cap"] = df["close"] * df["shares_outstanding"]
    totals = df.groupby("trade_date", as_index=False)["market_cap"].sum()
    totals = totals.rename(columns={"market_cap": "total_market_cap"})
    totals["index_value"] = base_value * totals["total_market_cap"] / totals["total_market_cap"].iloc[0]
    return totals
