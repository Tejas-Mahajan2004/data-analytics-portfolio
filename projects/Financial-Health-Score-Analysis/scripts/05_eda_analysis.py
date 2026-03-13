import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the final processed dataset containing financial metrics and health score
df = pd.read_csv("data/financial_health_processed.csv")

# Display first few rows to understand the structure of the dataset
print(df.head())

# Generate descriptive statistics for numerical columns - Includes mean, min, max, and standard deviation
print(df.describe())


# This histogram shows how financial health scores are distributed across all users in the dataset.
sns.histplot(df["Health_Score"], bins=20)
plt.title("Financial Health Score Distribution")
plt.show()


# Scatter plot to observe whether higher income users tend to save more money.

sns.scatterplot(x="Income", y="Savings", data=df)
plt.title("Income vs Savings")
plt.show()

# Shows how many users fall into each financial health category.

sns.countplot(x="Category", data=df)
plt.title("Financial Category Distribution")
plt.show()


# Displays correlation between numerical financial variables.
# Helps identify relationships between income, savings, debt burden, spending ratio, and health score.

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Financial Metrics Correlation")
plt.show()