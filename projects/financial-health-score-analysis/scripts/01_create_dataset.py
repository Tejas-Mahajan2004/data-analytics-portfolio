import pandas as pd
import numpy as np

# Set random seed for reproducibility
# This ensures the same random data is generated every time the script runs
np.random.seed(42)

# Define number of rows (users) in the dataset
rows = 1000

# Generate unique User IDs (U1000, U1001, U1002, ...)
user_ids = [f"U{1000+i}" for i in range(rows)]

# Generate random income values between ₹30,000 and ₹150,000
income = np.random.randint(30000, 150000, rows)

# Create empty lists to store expenses and savings
expenses = []
savings = []

# Generate random debt payment values between ₹0 and ₹20,000
debt_payment = np.random.randint(0, 20000, rows)

# Generate random transaction counts between 20 and 150
transaction_count = np.random.randint(20, 150, rows)

# Generate expense and savings values based on income
# Expenses are randomly selected between 35% and 90% of income
# Savings are calculated as remaining income after expenses
for inc in income:
    exp = np.random.randint(int(inc*0.35), int(inc*0.9))
    expenses.append(exp)
    savings.append(inc - exp)

# Create DataFrame with generated financial data
df = pd.DataFrame({
    "User_ID": user_ids,
    "Income": income,
    "Expense": expenses,
    "Savings": savings,
    "Debt_Payment": debt_payment,
    "Transaction_Count": transaction_count
})

# Save dataset as CSV file
df.to_csv("financial_data.csv", index=False)

# Print confirmation message
print("Dataset created successfully!")

# Display first 5 rows of the dataset
print(df.head())