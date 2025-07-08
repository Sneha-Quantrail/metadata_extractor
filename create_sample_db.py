from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db")

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
