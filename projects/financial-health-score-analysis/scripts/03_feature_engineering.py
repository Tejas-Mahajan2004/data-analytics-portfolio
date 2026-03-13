import pandas as pd

# Load the raw financial dataset
df = pd.read_csv("data/financial_data.csv")

# Calculate Savings Ratio
# Measures how much of a user's income is saved
# Formula: Savings / Income
df["Savings_Ratio"] = df["Savings"] / df["Income"]

# Calculate Debt Burden
# Measures how much income goes toward debt payments
# Formula: Debt_Payment / Income
df["Debt_Burden"] = df["Debt_Payment"] / df["Income"]

# Calculate Spending Ratio
# Measures how much income is spent
# Formula: Expense / Income
df["Spending_Ratio"] = df["Expense"] / df["Income"]

# Save the dataset with new financial metrics
df.to_csv("data/financial_features.csv", index=False)

# Print confirmation message
print("Feature engineering completed")