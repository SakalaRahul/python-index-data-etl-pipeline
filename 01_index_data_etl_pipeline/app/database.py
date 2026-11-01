from sqlalchemy import create_engine, String, Date, Float, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from app.config import settings

engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase): pass

class EquityPrice(Base):
    __tablename__ = "equity_prices"
    __table_args__ = (UniqueConstraint("trade_date", "symbol", name="uq_price_date_symbol"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    trade_date: Mapped[object] = mapped_column(Date, index=True)
    symbol: Mapped[str] = mapped_column(String(20), index=True)
    close: Mapped[float] = mapped_column(Float)
    shares_outstanding: Mapped[float] = mapped_column(Float)

class IndexSnapshot(Base):
    __tablename__ = "index_snapshots"
    trade_date: Mapped[object] = mapped_column(Date, primary_key=True)
    total_market_cap: Mapped[float] = mapped_column(Float)
    index_value: Mapped[float] = mapped_column(Float)

def initialize_database():
    Base.metadata.create_all(engine)
