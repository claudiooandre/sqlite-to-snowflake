# ETL Pipeline: SQLite → Python → Snowflake

This project demonstrates a complete **ETL (Extract, Transform, Load)** workflow using **Python**, **SQLite**, and **Snowflake**.

It extracts sales data from a local SQLite database, transforms it, uploads it to Snowflake, and runs a basic sales analysis.

---

## Tech Stack

- **Python 3+**
- **SQLite** (local source database)
- **Pandas** (data manipulation)
- **SQLAlchemy** (SQLite connection)
- **Snowflake Connector for Python**
- **write_pandas** (uploading DataFrames to Snowflake)

---

## Project Structure

```
sqlite_to_snowflake/
├── analysis/
│   └── queries.py              # SQL analysis queries on Snowflake
├── config/
│   └── snowflake_config.py     # Connection parameters
├── database/
│   └── vendas.db               # Local SQLite database
├── etl/
│   ├── extract_sqlite.py       # Extract data from SQLite
│   ├── transform.py            # Clean and transform the data
│   └── load_snowflake.py       # Upload to Snowflake
├── main.py                     # Executes the full ETL + analysis
```

---

## Pipeline Steps

### 1. Extract  
Pulls data from a local SQLite database.

```python
SELECT * FROM vendas
```

### 2. Transform  
Adds a new column: `valor_total = quantidade * preco_uni`

### 3. Load  
Uploads the cleaned DataFrame to a Snowflake table named `"vendas"` using `write_pandas`.

### 4. Analyze  
Executes:

```sql
SELECT "produto", SUM("valor_total") AS total_vendas
FROM "vendas"
GROUP BY "produto"
ORDER BY total_vendas DESC;
```

---

## Example Output

```bash
✅ Upload complete: 3 rows loaded.
('Portatil', 6000.0)
('Teclado', 600.0)
('Mouse', 500.0)
```

---

## Configuration

Edit your `config/snowflake_config.py` file with your Snowflake credentials:

```python
conn_params = {
    "user": "your_username",
    "password": "your_password",
    "account": "your_account_region",
    "warehouse": "your_warehouse",
    "database": "your_database",
    "schema": "your_schema"
}
```

