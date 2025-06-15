from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector

def load_to_snowflake(df, conn_params, table_name):
    conn = snowflake.connector.connect(**conn_params)
    cs = conn.cursor()

    cs.execute(f'USE WAREHOUSE "{conn_params["warehouse"]}"')
    cs.execute(f'USE DATABASE "{conn_params["database"]}"')
    cs.execute(f'USE SCHEMA "{conn_params["schema"]}"')

    cs.execute(f"""
        CREATE OR REPLACE TABLE {table_name} (
            id INT,
            produto STRING,
            quantidade INT,
            preco_unitario FLOAT,
            valor_total FLOAT
        )
    """)
    cs.close()

    success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        table_name,
        database=conn_params['database'],
        schema=conn_params['schema'],
        overwrite=True
    )
    print(f"✅ Upload completo: {nrows} linhas carregadas.")
    conn.close()
