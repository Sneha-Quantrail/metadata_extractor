# import pytest
# from metadata_extractor.extractor import extract_schema
# from sqlalchemy import create_engine, text

# @pytest.fixture(scope="module")
# def sqlite_test_db():
#     # Setup in-memory SQLite DB
#     engine = create_engine("sqlite:///:memory:")
#     with engine.begin() as conn:
#         conn.execute(text("""
#             CREATE TABLE users (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT
#             );
#         """))
#         conn.execute(text("""
#             CREATE TABLE orders (
#                 id INTEGER PRIMARY KEY,
#                 user_id INTEGER,
#                 total REAL,
#                 FOREIGN KEY(user_id) REFERENCES users(id)
#             );
#         """))
#     return "sqlite:///:memory:"

# def test_extract_schema_sqlite():
#     # For testing purpose, recreate schema each time
#     db_url = "sqlite:///:memory:"
#     engine = create_engine(db_url)
#     with engine.begin() as conn:
#         conn.execute(text("""
#             CREATE TABLE users (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT
#             );
#         """))
#         conn.execute(text("""
#             CREATE TABLE orders (
#                 id INTEGER PRIMARY KEY,
#                 user_id INTEGER,
#                 total REAL,
#                 FOREIGN KEY(user_id) REFERENCES users(id)
#             );
#         """))

#     schema = extract_schema(db_url)
#     assert isinstance(schema, list)
#     assert len(schema) == 2
#     assert any(item['table'] == 'users' for item in schema)
#     assert any(item['table'] == 'orders' for item in schema)


import os
import time
import tempfile
from metadata_extractor.extractor import extract_schema
from sqlalchemy import create_engine, text

def test_extract_schema_sqlite():
    # Path to temporary SQLite DB
    tmp_path = os.path.join(tempfile.gettempdir(), "test_schema.db")

    # ✅ Clean up if file already exists (from previous test run)
    if os.path.exists(tmp_path):
        try:
            os.remove(tmp_path)
        except PermissionError:
            print("⚠️ Could not delete existing DB. It may still be in use.")
            return  # Skip test to avoid false fail

    db_url = f"sqlite:///{tmp_path}"

    # Create the database and schema
    engine = create_engine(db_url)
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT
            );
        """))
        conn.execute(text("""
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                total REAL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        """))

    # Extract schema using your library
    schema = extract_schema(db_url)

    # ✅ Assertions
    assert isinstance(schema, list)
    assert len(schema) == 2

    table_names = [table["table"] for table in schema]
    assert "users" in table_names
    assert "orders" in table_names

    orders_table = next(table for table in schema if table["table"] == "orders")
    assert "user_id -> users.id" in orders_table["foreign_keys"]
    assert "users" in orders_table["associated_tables"]

    # ✅ Clean up (wait briefly to avoid Windows lock)
    engine.dispose()
    time.sleep(0.5)
    try:
        os.remove(tmp_path)
    except PermissionError:
        print(f"⚠️ Warning: Couldn't delete {tmp_path}, file still in use.")
