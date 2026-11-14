-- Q1 Where is attrition happening the most?
SELECT department,
       COUNT(*) AS total_emp,
       SUM(attrition_flag) AS employees_left,
       ROUND(100.0 * SUM(attrition_flag) / COUNT(*), 1) AS attrition_rate_pct,
       ROUND(AVG(monthly_income), 0) AS avg_salary,
       ROUND(AVG(job_satisfaction), 2) AS avg_satisfaction
FROM n  
GROUP BY department
ORDER BY attrition_rate_pct DESC;

-- Q2 At what career stage do people leave?
SELECT tenure_group,
       COUNT(*) AS total_employees,
       SUM(attrition_flag) AS employees_left,
       COUNT(*) - SUM(attrition_flag) AS employees_stayed,
       ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 1) AS attrition_rate_pct
FROM employee_attrition
GROUP BY tenure_group
ORDER BY attrition_rate_pct DESC;

-- Q3 Which job roles have the highest attrition risk?
SELECT job_role,
       COUNT(*) AS total_employees,
       SUM(attrition_flag) AS employees_left,
       ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 1) AS attrition_rate_pct
FROM employee_attrition
GROUP BY job_role
ORDER BY attrition_rate_pct DESC;

-- Q4 Does salary predict attrition?
SELECT income_group,
       COUNT(*) AS total_employees,
       SUM(attrition_flag) AS employees_left,
       ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 1) AS attrition_rate_pct,
       ROUND(AVG(monthly_income), 0) AS avg_monthly_income
FROM employee_attrition
GROUP BY income_group
ORDER BY attrition_rate_pct;

-- Q5 Does overtime affect attrition?
SELECT over_time,
       COUNT(*) AS total_employees,
       SUM(attrition_flag) AS employees_left,
       ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 1) AS attrition_rate_pct
FROM employee_attrition
GROUP BY over_time;

-- Q6 Does work-life balance affect retention?
SELECT work_life_balance,
       COUNT(*) AS total_employees,
       SUM(attrition_flag) AS employees_left,
       ROUND(SUM(attrition_flag) * 100.0 / COUNT(*), 1) AS attrition_rate_pct
FROM employee_attrition
GROUP BY work_life_balance
ORDER BY work_life_balance;