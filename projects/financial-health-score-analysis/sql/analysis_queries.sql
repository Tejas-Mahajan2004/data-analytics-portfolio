-- Q1. Total Users
-- Insight: The dataset contains all users whose financial behavior was analyzed.
-- Business Impact: Defines the total customer base used for financial health evaluation.
SELECT COUNT(*) AS total_users
FROM financial_health;


-- Q2. Average Financial Health Score
-- Insight: Shows the overall financial stability of users in the dataset.
-- Business Impact: Helps financial institutions understand the general financial health of their user base.
SELECT ROUND(AVG("Health_Score")::numeric, 2) 
AS avg_health_score
FROM financial_health;


-- Q3. Distribution of Users by Financial Category
-- Insight: Shows how users are distributed across financial health groups.
-- Business Impact: Helps fintech companies identify the proportion of financially vulnerable users.
SELECT 
    "Category",
    COUNT(*) AS total_users,
    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM financial_health), 2
    ) AS percent_users
FROM financial_health
GROUP BY "Category"
ORDER BY total_users DESC;


-- Q4. Average Savings Ratio by Category
-- Insight: Financially healthy users save a larger percentage of their income.
-- Business Impact: Encouraging savings behavior can significantly improve financial stability.
SELECT 
    "Category",
    ROUND(AVG("Savings_Ratio")::numeric, 2) AS avg_savings_ratio
FROM financial_health
GROUP BY "Category"
ORDER BY avg_savings_ratio DESC;


-- Q5. Average Debt Burden by Category
-- Insight: Users with higher debt burden tend to fall into risky financial categories.
-- Business Impact: Debt management tools could help improve user financial stability.
SELECT 
    "Category",
    ROUND(AVG("Debt_Burden")::numeric, 2) AS avg_debt_burden
FROM financial_health
GROUP BY "Category"
ORDER BY avg_debt_burden DESC;


-- Q6. Average Income by Financial Category
-- Insight: Higher income groups generally show better financial health scores.
-- Business Impact: Income level is a key factor influencing financial stability.
SELECT 
    "Category",
    ROUND(AVG("Income")::numeric, 2) AS avg_income
FROM financial_health
GROUP BY "Category"
ORDER BY avg_income DESC;


-- Q7. Top 10 Financially Healthy Users
-- Insight: These users maintain strong financial discipline with high savings and low debt burden.
-- Business Impact: They are ideal candidates for premium financial products and investments.
SELECT 
    "User_ID",
    "Income",
    "Savings",
    ROUND("Health_Score"::numeric, 2) AS health_score
FROM financial_health
ORDER BY "Health_Score" DESC
LIMIT 10;


-- Q8. Financially Vulnerable Users
-- Insight: These users have the lowest financial health scores.
-- Business Impact: FinTech platforms could recommend budgeting tools or financial advisory services.
SELECT 
    "User_ID",
    "Income",
    "Debt_Payment",
    "Health_Score"
FROM financial_health
WHERE "Health_Score" < 40
ORDER BY "Health_Score";


-- Q9. Spending Ratio Analysis
-- Insight: High spending ratios significantly reduce financial health scores.
-- Business Impact: Spending control strategies could improve financial health.
SELECT 
    "Category",
    ROUND(AVG("Spending_Ratio")::numeric, 2) AS avg_spending_ratio
FROM financial_health
GROUP BY "Category"
ORDER BY avg_spending_ratio DESC;


-- Q10. High Debt Users
-- Insight: Users paying large portions of income toward debt are more financially vulnerable.
-- Business Impact: Debt restructuring or financial counseling may benefit these users.
SELECT 
    "User_ID",
    "Income",
    "Debt_Burden"
FROM financial_health
WHERE "Debt_Burden" > 0.4
ORDER BY "Debt_Burden" DESC;


-- Q11. Income vs Savings Analysis
-- Insight: Higher income users generally save more money.
-- Business Impact: Savings products could be targeted to high-income segments.
SELECT 
    ROUND(AVG("Income")::numeric,2) AS avg_income,
    ROUND(AVG("Savings")::numeric,2) AS avg_savings
FROM financial_health;


-- Q12. Users with Above-Average Financial Health Score
-- Insight: These users demonstrate strong financial stability.
-- Business Impact: They are ideal candidates for investment or wealth management products.
SELECT 
    "User_ID",
    "Income",
    ROUND("Health_Score"::numeric,2) AS health_score
FROM financial_health
WHERE "Health_Score" > (
    SELECT AVG("Health_Score")
    FROM financial_health
)
ORDER BY "Health_Score" DESC;