import pandas as pd

# Load the final processed dataset
df = pd.read_csv("data/financial_health_processed.csv")

# This analysis shows how much income users save on average within each financial health category.
print("Average Savings Ratio by Category:")
print(df.groupby("Category")["Savings_Ratio"].mean())


# Users with Health Score below 40 are considered financially vulnerable.
high_risk = df[df["Health_Score"] < 40]
print("\nNumber of High Risk Users:", len(high_risk))


# Users are segmented into income groups to analyze how savings behavior changes with income level.
df["Income_Group"] = pd.cut(
    df["Income"],
    bins=[0, 50000, 100000, 150000],
    labels=["Low Income", "Middle Income", "High Income"]
)

print("\nSavings Ratio by Income Group:")
print(df.groupby("Income_Group")["Savings_Ratio"].mean())


# This analysis evaluates how debt burden varies across different financial health categories.
print("\nAverage Debt Burden by Category:")
print(df.groupby("Category")["Debt_Burden"].mean())