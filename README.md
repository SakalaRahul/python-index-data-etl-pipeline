# Python Index Data ETL Pipeline

A Python-based financial data engineering project that processes equity market data, performs data quality validation, calculates market-capitalization-weighted index values, and stores the processed results in PostgreSQL.

The project demonstrates concepts used in financial data processing, ETL pipelines, database management, cloud storage integration, and automated testing.

## Project Overview

Financial index calculations require accurate market data, reliable data validation, and consistent processing.

This project automates the following workflow:

1. Reads equity price data from CSV files.
2. Validates incoming financial records.
3. Cleans and normalizes the data.
4. Calculates market capitalization for each equity.
5. Calculates market-cap-weighted index values.
6. Stores processed data and index snapshots in PostgreSQL.
7. Generates validated CSV files and index reports.

## Architecture

```text
              Equity Market Data
                       |
                       v
                CSV Input Files
                       |
                       v
              Data Ingestion Layer
                       |
                       v
             Data Validation Layer
                       |
                       v
              Data Processing
                (Python/Pandas)
                       |
                       v
             Index Calculation
                       |
                       v
                PostgreSQL
                       |
                       v
              Output Generation
                       |
              +--------+--------+
              |                 |
              v                 v
        Validated CSV      Index Snapshots
```

**Optional AWS integration:**

```text
Amazon S3 --> AWS Lambda --> ETL Pipeline
                  |
                  v
             Processed Output
                  |
                  v
              Amazon S3
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Pandas | Data processing and transformation |
| PostgreSQL | Relational database storage |
| SQLAlchemy | Database connectivity and ORM |
| AWS S3 | Cloud object storage integration |
| AWS Lambda | Serverless pipeline entry point |
| Boto3 | AWS service integration |
| Docker | PostgreSQL container setup |
| Pytest | Automated unit testing |
| Git & GitHub | Version control |

## Key Features

### 1. Data Ingestion
- Reads financial market data from CSV files.
- Supports structured equity price records.
- Prepares input data for downstream processing.

### 2. Data Validation
- Checks required columns.
- Identifies missing and invalid values.
- Validates positive stock prices and outstanding shares.
- Detects duplicate stock records for the same trading date.
- Normalizes stock symbols.

### 3. Index Calculation

Calculates market capitalization using:

```text
Market Capitalization = Stock Price × Shares Outstanding
```

Calculates the index value using:

```text
Index Value = Base Index Value ×
              Current Total Market Capitalization /
              Initial Total Market Capitalization
```

The initial index value is configured as 1000.

### 4. Database Management
- Stores equity price records in PostgreSQL.
- Stores calculated index snapshots.
- Uses SQLAlchemy for database operations.
- Updates existing records when the same trading date and symbol are processed again.

### 5. AWS Integration
- Supports downloading input files from Amazon S3.
- Supports uploading processed output files to S3.
- Includes an AWS Lambda handler for serverless execution.

### 6. Testing and Logging
- Includes unit tests using Pytest.
- Tests data validation and index calculations.
- Provides structured JSON logging configuration.

## Project Structure

```text
python-index-data-etl-pipeline/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── logging_config.py
│   ├── validation.py
│   ├── calculation.py
│   ├── database.py
│   ├── repository.py
│   ├── pipeline.py
│   ├── s3_io.py
│   ├── lambda_handler.py
│   └── cli.py
│
├── data/
│   └── sample_prices.csv
│
├── sql/
│   └── 001_initial_schema.sql
│
├── tests/
│   └── test_pipeline_logic.py
│
├── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
```

## Getting Started

### Prerequisites

Install the following:

- Python 3.11 or later
- Docker Desktop
- PostgreSQL (optional if using the provided Docker setup)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/python-index-data-etl-pipeline.git
cd python-index-data-etl-pipeline
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Copy `.env.example` to `.env`.

Configure the database connection:

```env
DATABASE_URL=postgresql+psycopg://index_user:index_pass@localhost:5432/indexdb
AWS_REGION=ap-south-1
S3_BUCKET=
S3_INPUT_KEY=
LOG_LEVEL=INFO
```

### Step 5: Start PostgreSQL

```bash
docker compose up -d db
```

### Step 6: Execute the ETL Pipeline

```bash
python -m app.cli run --input data/sample_prices.csv --output output
```

### Step 7: Run Automated Tests

```bash
pytest -q
```

## Output

After successful execution, the pipeline generates:

```text
output/
├── validated_prices.csv
└── index_snapshots.csv
```

- `validated_prices.csv`: Cleaned and validated equity market data.
- `index_snapshots.csv`: Calculated market capitalization and index values for each trading date.

## Future Enhancements

- Integrate real-time financial market data APIs.
- Add advanced index rebalancing and corporate-action processing.
- Introduce Apache Airflow for scheduled workflows.
- Implement database migrations using Alembic.
- Add monitoring and alerting.
- Implement AWS Secrets Manager for secure credential management.
- Add CI/CD deployment workflows.

## Disclaimer

This is an educational portfolio project using synthetic sample market data. It is not connected to live financial markets and does not provide investment advice.

## Author

**Sakala Rahul**

- GitHub: https://github.com/SakalaRahul
- LinkedIn: https://linkedin.com/in/24rahul
