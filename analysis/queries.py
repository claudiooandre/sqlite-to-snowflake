import snowflake.connector

def run_analysis(conn_params):
    conn = snowflake.connector.connect(**conn_params)
    cs = conn.cursor()

    cs.execute(f'USE WAREHOUSE "{conn_params["warehouse"]}"')
    cs.execute(f'USE DATABASE "{conn_params["database"]}"')
    cs.execute(f'USE SCHEMA "{conn_params["schema"]}"')

    cs.execute('''
        SELECT "produto", SUM("valor_total") AS total_vendas
        FROM "vendas"
        GROUP BY "produto"
        ORDER BY total_vendas DESC
    ''')
    rows = cs.fetchall()
    for row in rows:
        print(row)

    cs.close()
    conn.close()
