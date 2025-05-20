import os
from sqlalchemy import create_engine, inspect, MetaData, Table
import pandas as pd

def get_db_engine(db_path):
    return create_engine(f"sqlite:///{db_path}")

def extract_schema(engine):
    inspector = inspect(engine)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    schema = {}

    for table_name in inspector.get_table_names():
        table = Table(table_name, metadata, autoload_with=engine)
        columns = {col.name: str(col.type) for col in table.columns}
        primary_keys = [col.name for col in table.primary_key.columns]
        foreign_keys = {fk.column.name: fk.column.table.name for fk in table.foreign_keys}

        schema[table_name] = {
            "columns": columns,
            "primary_keys": primary_keys,
            "foreign_keys": foreign_keys
        }
    return schema

def execute_sql(sql_query, engine):
    try:
        df = pd.read_sql(sql_query, engine)
        return df.to_json()
    except Exception as e:
        return f"SQL Error: {e}"