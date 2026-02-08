# Customer Shopping Behavior Analysis

## 📌 Project Overview
This end-to-end data analytics project analyzes customer shopping behavior to uncover insights
into spending patterns, subscription behavior, product performance, and customer segments.
The goal is to help the business make data-driven decisions to improve revenue, customer
engagement, and loyalty.

The project follows a complete analytics workflow using **Python, PostgreSQL, SQL, and Power BI**.


## 🎯 Business Problem
A retail company wants to better understand how customers behave across:
- Demographics (age, gender)
- Product categories
- Subscription status
- Discounts and shipping preferences

**Key business question:**
> How can customer shopping data be used to identify trends, improve customer engagement,
and optimize marketing and product strategies?


## 🛠 Tools & Technologies
- **Python** (Pandas, OS, SQLAlchemy)
- **PostgreSQL**
- **SQL**
- **Power BI**
- **Git & GitHub**


## 🧹 Data Preparation (Python)
- Loaded raw customer shopping data using Pandas
- Checked structure and summary statistics
- Handled missing values in **Review Rating** using median imputation
- Standardized column names to **snake_case**
- Feature engineering:
  - Created `age_group` column using quantile-based binning
  - Created `purchase_frequency_days` from purchase frequency labels
- Removed redundant column (`promo_code_used`)
- Saved cleaned dataset for downstream analysis


## 🗄 Database Integration (PostgreSQL)
- Loaded cleaned data into PostgreSQL using SQLAlchemy
- Created a structured `customer` table
- Enabled SQL-based business analysis on transactional data


## 📊 SQL Analysis (Business Questions Answered)
Key insights were generated using SQL queries, including:

1. Total revenue by gender
2. Customers using discounts but spending above average
3. Top 5 products by average review rating
4. Average purchase amount by shipping type
5. Subscriber vs non-subscriber spending comparison
6. Products with highest discount dependency
7. Customer segmentation (New, Returning, Loyal)
8. Top 3 most purchased products within each category
9. Relationship between repeat buyers and subscriptions
10. Revenue contribution by age group

All queries are documented in `analysis_queries.sql`.


## 📈 Power BI Dashboard
An interactive **Customer Behavior Dashboard** was built to visualize insights, including:
- Total customers, average purchase amount, and review rating KPIs
- Subscription status distribution
- Revenue and sales by category
- Revenue and sales by age group
- Interactive slicers for gender, category, subscription status, and shipping type

The dashboard enables stakeholders to explore trends dynamically and make informed decisions.


## 💡 Key Insights
- Non-subscribers generate higher total revenue due to volume, but subscribers show consistent spending
- Certain products rely heavily on discounts to drive sales
- Middle-aged and young adult customers contribute the highest revenue
- Loyal customers form the largest customer segment
- Express shipping customers have slightly higher average purchase values


## 📌 Business Recommendations
- Promote subscription benefits to convert repeat buyers
- Introduce loyalty programs to retain high-value customers
- Optimize discount strategies for margin control
- Focus marketing efforts on high-revenue age groups
- Highlight top-rated and best-selling products in campaigns


## 🚀 Conclusion
This project demonstrates a full **end-to-end data analytics workflow**, from raw data cleaning
to database analysis and business-focused visualization. It showcases practical skills in
Python, SQL, PostgreSQL, and Power BI for real-world analytics use cases.
