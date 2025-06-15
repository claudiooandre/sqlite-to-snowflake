from config.snowflake_config import conn_params
from etl.extract_sqlite import extract_from_sqlite
from etl.transform import clean_data
from etl.load_snowflake import load_to_snowflake
from analysis.queries import run_analysis

sqlite_db_path = 'database/vendas.db'

df = extract_from_sqlite(sqlite_db_path, 'vendas')
df_clean = clean_data(df)
load_to_snowflake(df_clean, conn_params, 'vendas')
run_analysis(conn_params)