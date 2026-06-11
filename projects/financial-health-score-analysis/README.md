# Financial Health Score Analysis
##  Project Overview

This end-to-end data analytics project evaluates the financial behavior of users by analyzing income, expenses, savings, and debt obligations. A Financial Health Score model is developed to measure financial stability and classify users into different financial risk categories.

The project simulates financial transaction data and applies analytics techniques to generate insights into savings behavior, spending patterns, and debt burden.

The project follows a complete analytics workflow using Python, PostgreSQL, SQL, and Power BI.

###  Project Objectives

    - Evaluate financial stability of users using behavioral financial metrics
    - Identify financially vulnerable users
    - Analyze the relationship between income, savings, and debt
    - Classify users into financial risk categories
    - Visualize financial behavior through an interactive dashboard

##  Business Problem

Many individuals earn income but still struggle with financial stability due to:

    - excessive spending
    - low savings
    - high debt payments

Financial institutions and fintech platforms need analytical tools to evaluate financial behavior and identify customers who may be financially vulnerable.
    
By understanding these patterns, companies can:
    - design better financial products
    - provide financial advisory services
    - detect financial risk early
    - improve financial wellbeing of users

## Key Business Questions

    1. How financially stable are users overall?
    2. What proportion of users fall into financially risky categories?
    3. How does income influence savings behavior?
    4. Which users have the highest debt burden?
    5. What financial patterns indicate potential financial vulnerability?

##  Tools & Technologies

    - Python (Pandas, NumPy)
    - Matplotlib & Seaborn
    - PostgreSQL
    - SQL
    - Power BI
    - Git & GitHub

##  Data Preparation (Python)
Data Generation
    A synthetic dataset of 1,000 users was generated using Python to simulate financial behavior.

    The dataset includes:

        - User_ID
        - Income
        - Expense
        - Savings
        - Debt_Payment
        - Transaction_Count

Feature Engineering
    Several financial indicators were created:
        - Savings Ratio
            Savings / Income
        - Debt Burden
            Debt_Payment / Income
        - Spending Ratio
            Expense / Income

    These indicators help evaluate how users manage their income.

Financial Health Score Model

A Financial Health Score was developed to quantify financial stability.

    Health Score =
    (Savings_Ratio × 40)
    + ((1 − Debt_Burden) × 30)
    + ((1 − Spending_Ratio) × 30)

    This scoring model ensures:

        - Higher savings increase financial health
        - Higher debt reduces financial health
        - Higher spending reduces financial health
    The score ranges from 0 to 100.

##  User Classification
Users were segmented into financial categories based on their health score.

    Score Range	Category
    80 – 100	Financially Healthy
    60 – 79 	Moderate
    40 – 59	    Risky
    Below 40	Vulnerable

In the simulated dataset used for this project, users fell into Moderate, Risky, and Vulnerable categories, with no users reaching the Financially Healthy threshold.

##  Database Integration (PostgreSQL)
    The processed dataset was loaded into PostgreSQL using SQLAlchemy.
    Database table: financial_health
    This allowed structured SQL analysis and efficient data querying.

##  SQL Business Analysis
Several SQL queries were written to extract financial insights.

Key analyses included:
    - Total number of users
    - Average financial health score
    - Financial category distribution
    - Savings ratio analysis
    - Debt burden analysis
    - Identification of financially vulnerable users
    - High-income user financial behavior

All SQL queries are documented in: analysis_queries.sql

##  Power BI Dashboard
An interactive analytics dashboard was created in Power BI.

KPI Indicators
    - Total Users
    - Average Health Score
    - Average Savings Ratio
    - Average Debt Burden

Visualizations
    - Financial Health Score Distribution
    - Financial Category Segmentation
    - Income vs Savings Behavior
    - Savings Ratio by Category
    - Debt Burden by Category
    - Users by Income Group

The dashboard provides a comprehensive view of financial behavior patterns.

##  Key Business Insights

    - 51.8% of users fall into the Risky financial category.
    - Moderate users save the highest proportion of income (~60%).
    - Vulnerable users have the highest debt burden (~18.8%).
    - Higher income groups generally demonstrate stronger savings behavior.
    - Financial stability strongly depends on the balance between savings and debt.

##  Business Recommendations

    - Encourage savings programs for moderate users to move them toward financial stability.
    - Provide financial advisory services for vulnerable users with high debt burden.
    - Offer targeted financial products for high-income users with strong savings potential.
    - Implement financial education initiatives to improve financial behavior.

##  Future Improvements
    - Incorporate real financial datasets
    - Develop machine learning models for financial risk prediction
    - Introduce time-based financial behavior tracking
    - Build automated financial scoring pipelines
    - Deploy dashboard using Power BI Service

##  Conclusion
This project demonstrates a complete end-to-end data analytics workflow:
    - Data generation & feature engineering using Python
    - Financial scoring model development
    - SQL-based financial analysis
    - Database integration using PostgreSQL
    - Interactive business dashboard using Power BI

The project highlights how financial analytics can help evaluate financial stability and identify financially vulnerable users.

Author

Tejas Mahajan
Aspiring Data Analyst
