# Metadata Extractor

This Python library scans any SQL-compatible database and extracts its full schema — including tables, columns, primary keys, foreign keys, and DDLs — in a structured JSON format.


## Project Structure

metadata_extractor/
├── metadata_extractor/
│ └── extractor.py # Main library: schema extractor
├── tests/
│ └── test_extractor.py # Unit tests using pytest
├── examples/
│ ├── create_sample_db.py # Creates a sample SQLite database
│ └── run_extractor.py # Demo script to run schema extractor
├── requirements.txt # Required dependencies
└── README.md # Project overview (this file)


## How to Set Up

1. **Clone the repo**

    git clone https://github.com/Sneha-Quantrail/metadata_extractor.git
    cd metadata_extractor

2. **Install dependencies**

    pip install -r requirements.txt

3. **(Optional) Create a sample database for testing**

    python examples/create_sample_db.py

4. **Run the extractor to view schema**

    python examples/run_extractor.py


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

The examples/ folder contains demo scripts for testing and local development. These are not required in production but are helpful for understanding and validating the library.

You can extend the extractor to support PostgreSQL, MySQL, etc., by changing the db_url in the scripts.
