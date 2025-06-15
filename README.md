📦 Project: ETL Pipeline with SQLite and Snowflake

🔍 Overview

This project is a complete ETL (Extract, Transform, Load) pipeline built in Python, designed to:

Extract data from a local SQLite database
Apply basic data transformations
Load the transformed data into a Snowflake cloud data warehouse
Run a simple analysis query on Snowflake
It serves as a clean, modular example of how to integrate local data sources with cloud-based data warehouses using Python.

⚙️ Technologies & Libraries

Python 3.12+
SQLite (local database)
Pandas (data manipulation)
SQLAlchemy (for connecting to SQLite)
Snowflake Connector for Python
Snowflake Pandas Tools (write_pandas)
🧩 Project Structure

sqlite_to_snowflake/
├── analysis/
│   └── queries.py              # Executes SQL analysis in Snowflake
├── config/
│   └── snowflake_config.py     # Connection parameters
├── database/
│   └── vendas.db               # Local SQLite database
├── etl/
│   ├── extract_sqlite.py       # Extracts data from SQLite
│   ├── transform.py            # Cleans and transforms data
│   └── load_snowflake.py       # Loads data into Snowflake
├── main.py                     # Full ETL pipeline script
└── requirements.txt            # Project dependencies
🛠️ Features

1. Extraction
Reads the vendas table from a local SQLite .db file using SQLAlchemy.

2. Transformation
Cleans the data and calculates a new column:

valor_total = quantidade * preco_unitario
3. Load
Creates or replaces the vendas table in Snowflake and uploads the transformed data using write_pandas.

4. Analysis
Performs a Snowflake SQL query to summarize sales by product, ordered by total value.

📈 Example Output

✅ Upload complete: 3 rows loaded.
('Notebook', 6000.0)
('Teclado', 600.0)
('Mouse', 500.0)