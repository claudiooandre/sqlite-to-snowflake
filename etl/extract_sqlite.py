import pandas as pd
from sqlalchemy import create_engine

def extract_from_sqlite(db_path, table_name):
    engine = create_engine(f"sqlite:///{db_path}")
    with engine.connect() as conn:
        df = pd.read_sql_table(table_name, conn)
    return df