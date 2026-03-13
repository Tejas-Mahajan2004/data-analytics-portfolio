import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Define Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Load Final Processed Dataset
data_path = os.path.join(BASE_DIR, "data", "financial_health_processed.csv")
print("Loading dataset...")
df = pd.read_csv(data_path)
print("Dataset loaded successfully!")


# PostgreSQL Connection Configuration
username = "postgres"
password = quote_plus("SQL@sql")   # Encodes special characters in password
host = "localhost"
port = "5432"
database = "financial_health_db"

# Create SQLAlchemy engine to connect Python with PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)
print("Connected to PostgreSQL!")


# Load Dataset into PostgreSQL Table
table_name = "financial_health"
df.to_sql(
    table_name,
    engine,
    if_exists="replace",   # Replaces table if it already exists
    index=False            # Prevents pandas index from being stored
)
print(f"Table '{table_name}' loaded successfully into PostgreSQL!")