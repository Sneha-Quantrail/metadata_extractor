from sqlalchemy import create_engine, inspect, text

def extract_schema(db_url):
    """
    Connects to the database using SQLAlchemy and extracts schema metadata.

    Parameters:
        db_url (str): SQLAlchemy-compatible database URL

    Returns:
        list: A list of dictionaries, each representing a table schema
    """
    engine = create_engine(db_url)
    metadata = []

    with engine.connect() as connection:
        inspector = inspect(connection)

        for table_name in inspector.get_table_names():
            ddl = connection.execute(
                text(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}'")
            ).fetchone()

            primary_keys = inspector.get_pk_constraint(table_name)['constrained_columns']
            foreign_keys_info = inspector.get_foreign_keys(table_name)
            foreign_keys = [
                f"{fk['constrained_columns'][0]} -> {fk['referred_table']}.{fk['referred_columns'][0]}"
                for fk in foreign_keys_info
            ]
            associated_tables = list({fk['referred_table'] for fk in foreign_keys_info})

            metadata.append({
                "table": table_name,
                "DDL": ddl[0] if ddl else None,
                "primary_key": primary_keys,
                "foreign_keys": foreign_keys,
                "associated_tables": associated_tables
            })

    return metadata
