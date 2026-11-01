# Index Data ETL Pipeline

An advanced, locally runnable market-data pipeline that ingests equity price CSV files,
validates and normalizes them, calculates a market-cap-weighted index, persists results
to PostgreSQL, and can optionally read/write objects in Amazon S3.

## Architecture
`CSV/S3 source -> validation -> normalization -> index calculation -> PostgreSQL -> JSON/CSV output`

## Features
- Strict schema and data-quality validation (missing fields, invalid prices, duplicate symbols).
- Market-cap-weighted index calculation using adjusted close and shares outstanding.
- PostgreSQL persistence with SQLAlchemy and parameterized ORM operations.
- Idempotent upserts keyed by `(symbol, trade_date)` and index snapshots keyed by date.
- Structured logging, configurable settings, unit tests, Docker Compose.
- Optional S3 ingestion/output and an AWS Lambda entry point.

## Quick start (local)
1. Install Python 3.11+ and Docker.
2. `python -m venv .venv`
3. Activate the environment, then `pip install -r requirements.txt`
4. `docker compose up -d db`
5. `cp .env.example .env`
6. `python -m app.cli run --input data/sample_prices.csv --output output`
7. `pytest -q`

The sample CSV is deliberately small and synthetic. It is not investment advice or live market data.

## CSV columns
`trade_date,symbol,close,shares_outstanding`
- `trade_date`: ISO date (`YYYY-MM-DD`)
- `close`: positive numeric closing price
- `shares_outstanding`: positive number of shares

## AWS (optional)
Set `AWS_REGION`, `S3_BUCKET`, and `S3_INPUT_KEY` in the Lambda environment. Package and deploy
using your organization's approved AWS deployment process. The Lambda handler is in
`app/lambda_handler.py`. For production, use Secrets Manager for DB credentials, IAM least
privilege, VPC connectivity where needed, retries/DLQ, alarms, and a controlled deployment pipeline.

## Important
This is a portfolio reference implementation. Before presenting it as your own work, run it,
understand every module, add your own improvements, and be prepared to explain design decisions.
