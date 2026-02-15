import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# 1. Define Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 2. Load RFM CSV File
rfm_path = os.path.join(BASE_DIR, "data", "clean", "rfm_customer_table.csv")

print("Loading RFM file...")
rfm = pd.read_csv(rfm_path)
print("RFM File Loaded Successfully!")

# 3. PostgreSQL Connection Details
username = "postgres"
password = quote_plus("SQL@sql")  
host = "localhost"
port = "5432"
database = "customer_clv_db"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

print("Connected to PostgreSQL!")

# 4. Load Data into PostgreSQL
table_name = "customer_rfm"

rfm.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print(f"Table '{table_name}' loaded successfully into PostgreSQL!")
