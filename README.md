
# 👥 Employee Attrition Analytics: End-to-End Project

## 🎯 Project Objective
 
Employee attrition is costly: hiring, training and lost productivity add up quickly. This project answers five business questions:
 
1. 📉 What is the overall attrition rate?
2. 🏢 Which departments and job roles lose the most employees?
3. ⏳ At what career stage do employees leave?
4. 💰 Does pay affect attrition?
5. ⏰ Which work factors (overtime, travel, stock options, work-life balance) are linked to attrition?
---
 
## 🗂️ Dataset
 
- **Source:** IBM HR Analytics Employee Attrition dataset
- **Size:** 1,470 employees, 35 columns
- **Target column:** `Attrition` (Yes / No)
- **Contains:** demographics, job role, department, income, overtime, satisfaction ratings, tenure and promotion history
---
 
## 🛠️ Tools & Technologies
 
| Tool | Purpose |
|---|---|
| 🐍 **Python** (Pandas, SQLAlchemy) | Data cleaning, feature engineering, database loading |
| 🐘 **PostgreSQL** | Storing the data and running business queries |
| 📊 **Power BI** | Interactive 3-page dashboard |
| 🧾 **SQL** | Analysis queries (GROUP BY, CASE WHEN, window functions) |
 
---
 
## 🔄 Project Workflow
 
```
Raw CSV  ➜  Python cleaning  ➜  Cleaned CSV  ➜  PostgreSQL  ➜  SQL analysis  ➜  Power BI dashboard  ➜  Insights
```
 
1. 📥 Load the raw CSV with Pandas
2. 🧹 Clean the data and create new columns
3. 💾 Save the cleaned CSV
4. 🗄️ Load it into a PostgreSQL table
5. 🔎 Answer business questions with SQL
6. 📈 Build the Power BI dashboard
7. 💡 Write insights and recommendations
---
 
## 🧹 Data Cleaning & Feature Engineering
 
**Cleaning steps**
- Standardized column names to `snake_case` (for example `MonthlyIncome` → `monthly_income`)
- Removed duplicate rows
- Removed columns with the same value for every employee (`EmployeeCount`, `Over18`, `StandardHours`)
- Converted `employee_number` to text, because an ID is a label and not a number
- Checked missing values and duplicates (both 0)
**New columns created**
 
| Column | Logic |
|---|---|
| `attrition_flag` | Yes = 1, No = 0 |
| `age_group` | 18-25, 26-35, 36-45, 46-55, 55+ |
| `income_group` | Low, Medium, High, Very High (based on monthly income) |
| `tenure_group` | 0-2 yrs, 3-5 yrs, 6-10 yrs, 10+ yrs (based on years at company) |
 
**Result:** 1,470 rows and 36 columns, ready for analysis.
 
---
 
## 🗄️ SQL Analysis
 
The cleaned data is stored in the PostgreSQL table `employee_attrition`. The queries are in [`sql/analysis_queries.sql`](sql/analysis_queries.sql).
 
**Example: attrition rate by department**
 
```sql
SELECT department,
       COUNT(*) AS total_employees,
       SUM(attrition_flag) AS employees_left,
       ROUND(AVG(attrition_flag) * 100, 1) AS attrition_rate_pct
FROM employee_attrition
GROUP BY department
ORDER BY attrition_rate_pct DESC;
```
 
**Questions covered**
- Overall attrition rate
- Attrition by department, job role, job level and marital status
- Attrition by age group, income group and tenure group
- Impact of overtime, business travel, stock options and work-life balance
- Overtime combined with income group
- Leavers vs stayers: average income and satisfaction
- Job role ranking with a window function (`RANK() OVER`)
- A list of current employees who match the highest-risk profile
---
 
## 📊 Power BI Dashboard
 
The dashboard has **3 pages** with slicers for department, gender and job role.
 
| Page | What it shows |
|---|---|
| 1️⃣ **Overview** | KPI cards (total employees, employees left, attrition rate, average income), attrition by department and age group, stayed vs left |
| 2️⃣ **Who Is Leaving** | Attrition by tenure, job role, job level and marital status; income of leavers vs stayers |
| 3️⃣ **Attrition Drivers** | Overtime, income group, work-life balance and risk categories, with insights and recommendations |
 
📸 **Screenshots**
 
<!-- Add your screenshots to the dashboard/ folder and update the file names below -->
![Executive Overview](https://github.com/Prasanna-21-ringole/EMPLOYEES-ATTRITION-ANALYSIS-/blob/ef8a3605ee180fe186aec90401372492546db753/EXECUTIVE%20OVERVIEW.png)

![Who Is Leaving](https://github.com/Prasanna-21-ringole/EMPLOYEES-ATTRITION-ANALYSIS-/blob/ef8a3605ee180fe186aec90401372492546db753/Who%20Is%20Leaving.png)

![Attrition Drivers](https://github.com/Prasanna-21-ringole/EMPLOYEES-ATTRITION-ANALYSIS-/blob/ef8a3605ee180fe186aec90401372492546db753/Attrition%20Drivers.png)
 
---
 
## 🔍 Key Insights
 
- 📉 **237 of 1,470 employees left**, an overall attrition rate of **16.1%**.
- 🧑 **Young employees leave the most:** ages 18-25 have a **35.8%** attrition rate, against 9.2% for ages 36-45.
- 🆕 **The first 2 years are the riskiest:** employees with 0-2 years at the company leave at **29.8%** and make up about **43%** of all leavers.
- 🛒 **Sales Representatives** have the highest attrition by role at **39.8%**.
- 🪜 **Entry-level employees** (Job Level 1) leave at **26.3%**, against 4.7% at Level 4.
- ⏰ **Overtime is the strongest driver:** **30.5%** attrition with overtime against 10.4% without it.
- 💸 **Low pay plus overtime is the highest-risk combination:** low-income employees doing overtime leave at **56.1%**.
- ✈️ **Frequent business travel** goes with **24.9%** attrition, against 8.0% for employees who don't travel.
- 📈 **No stock options:** these employees leave at **24.4%**, against 9.4% for stock option level 1.
- 💵 Leavers earn less on average (**4,787** per month) than stayers (**6,833**).
---
 
## ✅ Recommendations
 
1. 💰 **Review pay for low-income roles,** since they have the highest attrition.
2. ⏰ **Reduce overtime,** especially for low-paid employees.
3. 🎓 **Build an onboarding and retention program** for the first 2 years.
4. 🛒 **Review pay and career paths** for Sales Representatives and entry-level roles.
5. 📈 **Consider stock options or other benefits** for employees who have none.
6. ✈️ **Review how often employees are asked to travel.**
7. 📅 **Track attrition monthly** by income group and tenure to measure whether the actions work.
---
 
## 📁 Repository Structure
 
```
Employee_Attrition_Analysis/
│
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned CSV from the Python script
│
├── scripts/
│   └── attrition_cleaning.py # Data cleaning + PostgreSQL loading
│
├── sql/
│   └── analysis_queries.sql  # Business questions and queries
│
├── dashboard/
│   ├── Employee_Attrition_Dashboard.pbix
│   └── page screenshots (.png)
│
└── README.md
```
 
---
 
## 🚀 How to Run
 
**1. Install the libraries**
 
```bash
pip install pandas sqlalchemy psycopg2-binary
```
 
**2. Create the database in PostgreSQL**
 
```sql
CREATE DATABASE employee_attrition_db;
```
 
**3. Update the file paths** at the top of `scripts/attrition_cleaning.py` so they point to your raw CSV and your output folder.
 
**4. Run the script**
 
```bash
python scripts/attrition_cleaning.py
```
 
The script cleans the data, saves the cleaned CSV, asks for your PostgreSQL password (hidden as you type) and loads the table `employee_attrition`. If the table already has data, the load is skipped so rows are not duplicated.
 
**5. Run the SQL queries** from `sql/analysis_queries.sql` in pgAdmin's Query Tool.
 
**6. Open the dashboard:** open the `.pbix` file in Power BI Desktop and refresh the data if needed.
 
> 🔒 The password is entered when the script runs and is never stored in the code. Do not commit passwords to the repository.
 
---
 
## ⚠️ Limitations
 
- These findings show **associations, not proof of cause.** For example, overtime is linked to higher attrition, but this analysis can't prove that overtime is the reason.
- Some groups are small (for example Sales Representatives and the lowest work-life balance rating), so those rates should be read with care.
- The dataset is a single snapshot. It does not show how attrition changes over time.
---
 
## 👤 Author
 
**Your Name**
- 💼 LinkedIn: [your-linkedin-link](https://www.linkedin.com/)
- 🐙 GitHub: [your-github-link](https://github.com/)
- 📧 Email: your.email@example.com
⭐ If you found this project useful, please star the repository.
