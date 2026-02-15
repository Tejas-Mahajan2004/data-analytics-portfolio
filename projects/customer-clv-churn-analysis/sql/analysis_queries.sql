-- Q1. Total Customers

-- Insight: The dataset contains 5,878 unique customers.
-- Business Impact: Defines the full customer base used for revenue and churn analysis.
SELECT COUNT(*) AS total_customers
FROM customer_rfm;


-- Q2. Total Revenue Generated

-- Insight: Total lifetime revenue = 17.74 Million.
-- Business Impact: Serves as baseline revenue metric for segment and churn evaluation.
SELECT ROUND(SUM(monetary)::numeric, 2) AS total_revenue
FROM customer_rfm;


-- Q3. Revenue Contribution by Segment

-- Insight: Champions contribute 47% of total revenue,
-- despite being a small portion of customers.
-- Business Impact: Revenue is highly concentrated → retention of Champions is critical.
SELECT 
    segment,
    ROUND(SUM(monetary)::numeric, 2) AS total_revenue,
    ROUND(
        (100.0 * SUM(monetary) /
        (SELECT SUM(monetary) FROM customer_rfm)
        )::numeric, 2
    ) AS revenue_percent
FROM customer_rfm
GROUP BY segment
ORDER BY total_revenue DESC;


-- Q4. Customer Distribution by Segment

-- Insight: 62% customers fall under 'Others' segment,
-- while Champions represent only ~8%.
-- Business Impact: Small elite segment drives disproportionate revenue.
SELECT 
    segment,
    COUNT(*) AS total_customers,
    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM customer_rfm), 2
    ) AS customer_percent
FROM customer_rfm
GROUP BY segment
ORDER BY total_customers DESC;


-- Q5. Churn Rate by Segment

-- Insight: The At Risk segment exhibits 100% churn, indicating that customers classified in this group are already lost.

-- Business Impact: Mid-value segments require proactive retention strategies
-- to prevent further revenue erosion.
SELECT 
    segment,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percent
FROM customer_rfm
GROUP BY segment
ORDER BY churn_rate_percent DESC;


-- Q6. Total Revenue At Risk

-- Insight: 3.47 Million revenue associated with churned customers.
-- Business Impact: Nearly 20% of total revenue is exposed to churn,
-- highlighting the urgency for predictive churn prevention.
SELECT 
    ROUND(SUM(monetary)::numeric, 2) AS revenue_at_risk
FROM customer_rfm
WHERE churn = 1;


-- Q7. Revenue At Risk by Segment

-- Insight: Majority of revenue loss from 'Others' segment (2.34M).
-- Business Impact: Engagement strategy needed for mid-value customers.
SELECT 
    segment,
    ROUND(SUM(monetary)::numeric, 2) AS revenue_at_risk
FROM customer_rfm
WHERE churn = 1
GROUP BY segment
ORDER BY revenue_at_risk DESC;


-- Q8. Top 10 High-Value Customers

-- Insight: Top customers mainly from Champions segment.
-- Business Impact: Strong dependency on elite customers.
-- High-touch engagement and loyalty programs are essential.
SELECT 
    customer_id,
    segment,
    ROUND(clv::numeric, 2) AS clv
FROM customer_rfm
ORDER BY clv DESC
LIMIT 10;


-- Q9. Top 10 High-Value Churned Customers

-- Insight: High-value churned customers belong mostly to At Risk.
-- Business Impact: Early churn detection and targeted intervention
-- strategies are critical to reduce high-value customer loss.
SELECT 
    customer_id,
    segment,
    ROUND(clv::numeric, 2) AS clv
FROM customer_rfm
WHERE churn = 1
ORDER BY clv DESC
LIMIT 10;


-- Q10. Pareto Analysis (80/20 Rule)

-- Insight: 23% of customers generate 80% of revenue.
-- Business Impact: Revenue is highly concentrated among a small percentage of customers,
-- creating dependency risk if high-value customers churn.

WITH revenue_rank AS (
    SELECT 
        customer_id,
        monetary,
        SUM(monetary) OVER (ORDER BY monetary DESC) AS cumulative_revenue,
        SUM(monetary) OVER () AS total_revenue
    FROM customer_rfm
)
SELECT 
    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM customer_rfm), 2
    ) AS top_customer_percent
FROM revenue_rank
WHERE cumulative_revenue <= 0.8 * total_revenue;


-- Q11. Average CLV by Segment

-- Insight: Champions have highest average CLV.
-- Business Impact: They are most valuable long-term customers.
SELECT 
    segment,
    ROUND(AVG(clv)::numeric, 2) AS avg_clv
FROM customer_rfm
GROUP BY segment
ORDER BY avg_clv DESC;


-- Q12. Customers Above Average CLV

-- Insight: Majority of above-average CLV customers belong to Champions.
-- Some At Risk customers also show high CLV → urgent retention opportunity.
SELECT 
    customer_id,
    segment,
    ROUND(clv::numeric, 2) AS clv
FROM customer_rfm
WHERE clv > (SELECT AVG(clv) FROM customer_rfm)
ORDER BY clv DESC;
