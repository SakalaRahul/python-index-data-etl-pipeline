import pandas as pd
import pytest
from app.validation import validate_prices, DataQualityError
from app.calculation import calculate_index

def test_validation_normalizes_symbol():
    df = pd.DataFrame([{"trade_date":"2026-01-01","symbol":" abcd ",
                        "close":10,"shares_outstanding":100}])
    result = validate_prices(df)
    assert result.loc[0, "symbol"] == "ABCD"

def test_rejects_duplicate_symbol_date():
    row = {"trade_date":"2026-01-01","symbol":"ABC","close":10,"shares_outstanding":100}
    with pytest.raises(DataQualityError):
        validate_prices(pd.DataFrame([row, row]))

def test_index_base_and_weighted_total():
    df = validate_prices(pd.DataFrame([
        {"trade_date":"2026-01-01","symbol":"A","close":10,"shares_outstanding":100},
        {"trade_date":"2026-01-02","symbol":"A","close":20,"shares_outstanding":100},
    ]))
    out = calculate_index(df)
    assert out.iloc[0]["index_value"] == 1000
    assert out.iloc[1]["index_value"] == 2000
