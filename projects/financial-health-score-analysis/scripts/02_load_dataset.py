import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the financial dataset from the data folder
df = pd.read_csv("data/financial_data.csv")

# Display first 5 rows of the dataset
df.head()

# Show dataset information - Includes column names, data types, and non-null counts
df.info()

# Generate descriptive statistics - Provides summary metrics such as mean, min, max, and standard deviation
df.describe()