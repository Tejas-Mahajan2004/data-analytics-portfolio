import pandas as pd
import os

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Correct absolute path to CSV
csv_path = os.path.join(
    BASE_DIR,
    'data',
    'raw',
    'customer_shopping_behavior.csv'
)

# Load data
df = pd.read_csv(csv_path)

print(df.head())
df.info()
print(df.describe())

# Fix missing Review Rating using median
df['Review Rating'] = df['Review Rating'].fillna(df['Review Rating'].median())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# name all the column names in snake case pattern
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

# create a colnumn age_group
labels = ['Young Adult', 'Adult', 'Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
print(df[['age','age_group']].head(10))

# create column purchase_frequency_days
frequency_mapping = {
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))

print((df['discount_applied'] == df['promo_code_used']).all())

df = df.drop('promo_code_used',axis=1)
print(df.columns)

# ---------- Save cleaned CSV (IMPORTANT STEP) ----------
processed_path = os.path.join(
    BASE_DIR,
    'data',
    'clean',
    'customer_shopping_cleaned.csv'
)

os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

print("\n Cleaned data saved to data/processed/customer_shopping_cleaned.csv")