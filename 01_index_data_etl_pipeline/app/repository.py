from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy import select
from app.database import EquityPrice, IndexSnapshot, SessionLocal

def save_prices_and_snapshots(prices, snapshots):
    # Portable ORM transaction. Existing date/symbol rows are updated safely.
    with SessionLocal.begin() as session:
        for row in prices.to_dict("records"):
            existing = session.scalar(select(EquityPrice).where(
                EquityPrice.trade_date == row["trade_date"],
                EquityPrice.symbol == row["symbol"]))
            if existing:
                existing.close = float(row["close"])
                existing.shares_outstanding = float(row["shares_outstanding"])
            else:
                session.add(EquityPrice(**row))
        for row in snapshots.to_dict("records"):
            existing = session.get(IndexSnapshot, row["trade_date"])
            if existing:
                existing.total_market_cap = float(row["total_market_cap"])
                existing.index_value = float(row["index_value"])
            else:
                session.add(IndexSnapshot(**row))
