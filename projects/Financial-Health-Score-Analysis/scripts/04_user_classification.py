import pandas as pd

# Load the dataset that already contains engineered financial features
df = pd.read_csv("data/financial_features.csv")

# The score combines three financial indicators:
# 1. Savings Ratio (positive factor)
# 2. Debt Burden (negative factor)
# 3. Spending Ratio (negative factor)

# Formula:
# (Savings_Ratio * 40) + ((1 - Debt_Burden) * 30) + ((1 - Spending_Ratio) * 30)
df["Health_Score"] = (
    df["Savings_Ratio"] * 40 +
    (1 - df["Debt_Burden"]) * 30 +
    (1 - df["Spending_Ratio"]) * 30
)

# Round the health score to 2 decimal places for readability
df["Health_Score"] = df["Health_Score"].round(2)

# Users are grouped into financial risk categories
def classify(score):
    if score >= 80:
        return "Financially Healthy"
    elif score >= 60:
        return "Moderate"
    elif score >= 40:
        return "Risky"
    else:
        return "Vulnerable"


# Apply classification to each user
df["Category"] = df["Health_Score"].apply(classify)


# Save the final processed dataset
# This dataset will be used for SQL analysis and Power BI dashboard
df.to_csv("data/financial_health_processed.csv", index=False)

# Confirmation message
print("User classification completed")