import pandas as pd
import os

# 1. Load Data
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "raw", "online_retail_II.xlsx")

    print("Loading dataset...")
    df_2009 = pd.read_excel(file_path, sheet_name=0)
    df_2010 = pd.read_excel(file_path, sheet_name=1)

    df = pd.concat([df_2009, df_2010])
    print("Dataset Loaded Successfully!")
    return df

# 2. Clean Data
def clean_data(df):

    # Remove missing customer IDs
    df = df.dropna(subset=["Customer ID"])

    # Remove returns (negative quantity)
    df = df[df["Quantity"] > 0]

    # Remove zero price transactions
    df = df[df["Price"] > 0]

    # Convert to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Create total revenue column
    df["TotalAmount"] = df["Quantity"] * df["Price"]

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    print("Final Cleaned Shape:", df.shape)
    return df


# 3. Create RFM Table
def create_rfm(df):

    snapshot_date = df["invoicedate"].max() + pd.Timedelta(days=1)
    print("Snapshot Date:", snapshot_date)

    rfm = df.groupby("customer_id").agg({
        "invoicedate": lambda x: (snapshot_date - x.max()).days,
        "invoice": "nunique",
        "totalamount": "sum"
    }).reset_index()

    rfm.columns = ["customer_id", "recency", "frequency", "monetary"]

    print("Total Customers:", rfm.shape[0])
    return rfm


# 4. RFM Scoring & Segmentation
def segment_customers(rfm):

    rfm["r_score"] = pd.qcut(rfm["recency"], 5, labels=[5,4,3,2,1])
    rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
    rfm["m_score"] = pd.qcut(rfm["monetary"], 5, labels=[1,2,3,4,5])

    rfm["rfm_score"] = (
        rfm["r_score"].astype(str) +
        rfm["f_score"].astype(str) +
        rfm["m_score"].astype(str)
    )

    def segment(row):
        if row["rfm_score"] == "555":
            return "Champions"
        elif row["r_score"] >= 4 and row["f_score"] >= 4:
            return "Loyal Customers"
        elif row["r_score"] <= 2 and row["f_score"] >= 4:
            return "At Risk"
        elif row["r_score"] == 5:
            return "New Customers"
        else:
            return "Others"

    rfm["segment"] = rfm.apply(segment, axis=1)

    print("Segmentation Completed!")
    return rfm


# 5. Business Metrics
def calculate_metrics(rfm):

    rfm["avg_order_value"] = rfm["monetary"] / rfm["frequency"]

    # Simple CLV
    rfm["clv"] = rfm["monetary"]

    # Define churn
    rfm["churn"] = rfm["recency"].apply(lambda x: 1 if x > 90 else 0)

    revenue_at_risk = rfm[rfm["churn"] == 1]["monetary"].sum()

    print("Revenue At Risk:", round(revenue_at_risk, 2))

    return rfm


# 6. Save Files
def save_files(df, rfm):

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Create clean folder if not exists
    clean_folder = os.path.join(BASE_DIR, "data", "clean")
    os.makedirs(clean_folder, exist_ok=True)

    # Save cleaned transactions
    cleaned_path = os.path.join(clean_folder, "cleaned_transactions.csv")
    df.to_csv(cleaned_path, index=False)

    # Save RFM table
    rfm_path = os.path.join(clean_folder, "rfm_customer_table.csv")
    rfm.to_csv(rfm_path, index=False)

    print("Files saved successfully in data/clean folder!")


# 7. Main Execution
if __name__ == "__main__":

    df = load_data()
    df = clean_data(df)
    rfm = create_rfm(df)
    rfm = segment_customers(rfm)
    rfm = calculate_metrics(rfm)
    save_files(df, rfm)

    print("\nProject Execution Completed Successfully!")
