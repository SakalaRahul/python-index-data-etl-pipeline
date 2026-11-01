CREATE TABLE IF NOT EXISTS equity_prices (
  id BIGSERIAL PRIMARY KEY,
  trade_date DATE NOT NULL,
  symbol VARCHAR(20) NOT NULL,
  close DOUBLE PRECISION NOT NULL CHECK (close > 0),
  shares_outstanding DOUBLE PRECISION NOT NULL CHECK (shares_outstanding > 0),
  CONSTRAINT uq_price_date_symbol UNIQUE (trade_date, symbol)
);
CREATE INDEX IF NOT EXISTS ix_equity_prices_trade_date ON equity_prices(trade_date);
CREATE TABLE IF NOT EXISTS index_snapshots (
  trade_date DATE PRIMARY KEY,
  total_market_cap DOUBLE PRECISION NOT NULL,
  index_value DOUBLE PRECISION NOT NULL
);
