# Metadata Extractor

This Python library scans any SQL-compatible database and extracts its full schema — including tables, columns, primary keys, foreign keys, and DDLs — in a structured JSON format.


## Project Structure

    metadata_extractor/
    ├── create_sample_db.py # Creates sample SQLite DB
    ├── run_extractor.py # Script to run schema extractor
    ├── sample.db # Example SQLite DB (optional)
    ├── requirements.txt # Project dependencies
    ├── metadata_extractor/
    │ ├── init.py
    │ └── extractor.py # Core schema extraction logic
    ├── tests/
    │ ├── init.py
    │ └── test_extractor.py # Pytest unit test


## How to Set Up

1. **Clone the repo**

    git clone https://github.com/Sneha-Quantrail/metadata_extractor.git

    cd metadata_extractor

2. **Create a Virtual Environment**

    python -m venv venv

3. **Activate it**

    .\venv\Scripts\Activate.ps1


4. **Install dependencies**

    pip install -r requirements.txt


5. **(Optional) Create a sample database for testing**

    python create_sample_db.py

6. **Run the extractor to view schema**

    python run_extractor.py


# Run Unit Tests

    pytest

This will run tests/test_extractor.py, which uses an in-memory SQLite database to validate that schema extraction works correctly.

# Sample Output

[
  {
    "table": "orders",
    "DDL": "CREATE TABLE orders (...)",
    "primary_key": ["id"],
    "foreign_keys": ["user_id -> users.id"],
    "associated_tables": ["users"]
  },
  {
    "table": "users",
    "DDL": "CREATE TABLE users (...)",
    "primary_key": ["id"],
    "foreign_keys": [],
    "associated_tables": []
  }
]


# Notes

create_sample_db.py and run_extractor.py are provided as demo scripts for local testing. These are not mandatory in production but useful for local validation.
