# Customer Lifetime Value & Churn Risk Analysis
## 📌 Project Overview

This end-to-end data analytics project analyzes transactional retail data to identify high-value customers, detect churn risk, and evaluate revenue concentration using RFM (Recency, Frequency, Monetary) segmentation.

### 🎯 Project Objectives

    - Maximize Customer Lifetime Value (CLV)
    - Reduce revenue loss due to churn
    - Identify revenue concentration risk
    - Implement data-driven retention strategies

The project follows a complete analytics workflow using Python, PostgreSQL, SQL, and Power BI.

## 🎯 Business Problem

In competitive e-commerce environments, companies struggle to:

    - Identify their most valuable customers
    - Detect customers likely to churn
    - Understand revenue concentration risk
    - Prioritize retention strategies effectively

Revenue is often highly concentrated among a small segment of customers. Losing these high-value customers can significantly impact total revenue.

## Key Business Questions:

    1. Who are the most valuable customers?
    2. What percentage of revenue comes from elite segments?
    3. How much revenue is at risk due to churn?
    4. Is the business overly dependent on a small group of customers?
    5. Which segments require immediate retention strategies?

## 🛠 Tools & Technologies

    Python (Pandas, OS, SQLAlchemy)
    PostgreSQL
    SQL
    Power BI
    Git & GitHub


## 🧹 Data Preparation (Python)
Data Loading
    - Combined 2009 and 2010 retail transaction sheets
    - Loaded data using Pandas

Data Cleaning
    - Removed negative quantities (returns)
    - Removed missing Customer IDs
    - Removed zero-price transactions
    - Converted InvoiceDate to datetime
    - Created TotalAmount column
    - Standardized column names to snake_case

Feature Engineering

Created RFM metrics:
    - Recency → Days since last purchase
    - Frequency → Number of invoices
    - Monetary → Total revenue per customer

RFM Scoring
    - Applied quintile-based scoring for R, F, and M
    - Combined into rfm_score
    - Created customer segments:
            Champions
            Loyal Customers
            At Risk
            New Customers
            Others

Business Metrics
    - Average Order Value
    - CLV (Monetary-based)
    - Churn flag (Recency > 90 days)
    - Revenue at risk

## 🗄 Database Integration (PostgreSQL)
    - Loaded RFM dataset into PostgreSQL using SQLAlchemy
    - Created structured table: customer_rfm
    - Enabled SQL-based business analysis
    - Performed advanced aggregations and window functions

## 📊 SQL Business Analysis

The following insights were generated using SQL queries:

Key Findings:
    - Total Customers: 5,878
    - Total Revenue: ₹17.74 Million
    - Revenue Concentration:
        47% of revenue comes from Champions
        23% of customers generate 80% of revenue (Pareto principle)
    - Revenue at Risk: ₹3.47 Million
    - Churn Insights:
        At Risk segment → 100% churn
        Others → 71% churn
        Champions → 0% churn

All SQL queries are documented in analysis_queries.sql.

## 📈 Power BI Dashboard

An executive-level dashboard was built including:

KPI Cards
    - Total Customers
    - Total Revenue
    - Churn Rate %
    - Revenue at Risk

Visualizations
    - Revenue Contribution by Segment (Donut Chart)
    - Customer Distribution by Segment (Bar Chart)
    - Revenue at Risk by Segment (Column Chart)
    - Churn Rate by Segment
    - Top High-Value Customers Table
    - Interactive Segment Filter

The dashboard provides clear visibility into revenue concentration and churn risk.

## 💡 Key Business Insights
    - Revenue is highly concentrated among a small percentage of customers.
    - Nearly 20% of total revenue is exposed to churn.
    - Champions represent a small portion of customers but drive almost half of revenue.
    - At Risk and Others segments require proactive retention strategies.
    - Business dependency on elite customers creates financial vulnerability.

## 📌 Business Recommendations
    - Implement loyalty programs for Champions.
    - Target At Risk customers with personalized campaigns.
    - Monitor revenue concentration monthly.
    - Introduce predictive churn modeling in the next phase.
    - Expand mid-value customer engagement to reduce dependency risk.

## 🚀 Future Improvements
    - Machine Learning-based churn prediction model
    - Advanced probabilistic CLV modeling
    - Deploy dashboard using Power BI Service
    - Automate ETL pipeline using Airflow
    - Real-time customer monitoring

🏆 Conclusion
This project demonstrates a complete end-to-end data analytics workflow:
    - Data cleaning & feature engineering in Python
    - Database integration with PostgreSQL
    - Advanced business analysis using SQL
    - Executive dashboard creation in Power BI