# 📦 Metadata Extractor

This Python library scans any SQL-compatible database and extracts its full schema — including tables, columns, primary keys, foreign keys, and DDLs — in a structured JSON format.


## 📁 Project Structure

Quantrail-Data/
└── metadata_extractor/
    ├── metadata_extractor/              ← Main package
    │   ├── __init__.py                  
    │   ├── extractor.py                 ← Main schema extractor library
    │
    ├── tests/                           ← Unit tests
    │   ├── __init__.py                  
    │   └── test_extractor.py            ← Contains the test case
    │
    ├── examples/                        ← Example scripts (Optional)
    │   ├── __init__.py                  
    │   ├── run_extractor.py             ← Demo script
    │   └── create_sample_db.py          ← For generating sample SQLite DB
    │
    ├── requirements.txt                ← List of required packages
    ├── README.md                       ← Project documentation


Quantrail-Data/
└── metadata_extractor/
    ├── metadata_extractor/              ← 📦 Main package
    │   ├── __init__.py                  ← Makes it a package
    │   ├── extractor.py                 ← Your main schema extractor library
    │
    ├── tests/                           ← 🧪 Unit tests
    │   ├── __init__.py                  ← Optional, but good practice
    │   └── test_extractor.py           ← Contains the test case
    │
    ├── examples/                        ← 🧾 Example scripts (optional)
    │   ├── __init__.py                  ← (optional)
    │   ├── run_extractor.py            ← Demo script
    │   └── create_sample_db.py         ← For generating sample SQLite DB
    │
    ├── requirements.txt                ← List of required packages
    ├── README.md                       ← Project documentation
    ├── .gitignore                      ← To ignore venv/, __pycache__/, etc.
  


## ✅ Features

- Supports any SQLAlchemy-compatible database (e.g., SQLite, PostgreSQL, MySQL)
- Extracts:
  - Table names
  - DDL statements (e.g., `CREATE TABLE ...`)
  - Primary keys
  - Foreign key relationships
  - Associated tables
- Outputs schema as clean, structured JSON
- Includes unit tests using `pytest`


## 🛠️ How to Set Up

1. **Clone the repo**

    git clone https://github.com/Sneha-Quantrail/metadata_extractor.git
    cd metadata_extractor

2. **Install dependencies**

    pip install -r requirements.txt

3. **(Optional) Create a sample database for testing**

    python examples/create_sample_db.py

4. **Run the extractor to view schema**

    python examples/run_extractor.py
   

## 🧪 Unit Testing

This project includes unit testing using pytest.
The test validates:

✅ Database connection using SQLite

✅ Schema extraction for tables, primary keys, and foreign key relationships

✅ Output structure format (list of schema dictionaries)

✅ Association mapping between related tables

✅ Cleanup of test database file (Windows-safe)


## 🧪 Run Unit Tests

    pytest

This will run tests/test_extractor.py, which uses an in-memory SQLite database to validate that schema extraction works correctly.


## Sample Output

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


## Notes

The examples/ folder contains demo scripts for testing and local development. These are not required in production but are helpful for understanding and validating the library.

You can extend the extractor to support PostgreSQL, MySQL, etc., by changing the db_url in the scripts.
