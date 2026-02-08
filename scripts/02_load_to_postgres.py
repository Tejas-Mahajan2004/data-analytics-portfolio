import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# --------- Project root ---------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# --------- Load CSV THAT ACTUALLY EXISTS ---------
csv_path = os.path.join(
    BASE_DIR,
    'data',
    'clean',
    'customer_shopping_cleaned.csv'
)

df = pd.read_csv(csv_path)

# --------- PostgreSQL connection ---------
username = "postgres"
password = quote_plus("SQL@sql")    # same as pgAdmin
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# --------- Load to PostgreSQL ---------
table_name = "customer"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print(f" Data successfully loaded into PostgreSQL table '{table_name}'")
