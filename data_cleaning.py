import pandas as pd
from sqlalchemy import create_engine, text
from getpass import getpass
from urllib.parse import quote_plus

# --- 1. DATA CLEANING ---
df = pd.read_csv(r"D:\Employee_Attrition_Analysis\data\raw\employee_attrition.csv")
print("Original Shape:", df.shape)

df.columns = (
    df.columns.str.strip()
    .str.replace(r"([a-z0-9])([A-Z])", r"\1_\2", regex=True)
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

df = df.drop_duplicates()
df = df.drop(columns=[c for c in df.columns if df[c].nunique() == 1])
df["employee_number"] = df["employee_number"].astype(str)

df["attrition_flag"] = df["attrition"].map({"Yes": 1, "No": 0})
df["age_group"] = pd.cut(df["age"], [0, 25, 35, 45, 55, 100],
                         labels=["18-25", "26-35", "36-45", "46-55", "55+"]).astype(str)
df["income_group"] = pd.cut(df["monthly_income"], [0, 3000, 6000, 10000, float("inf")],
                            labels=["Low", "Medium", "High", "Very High"]).astype(str)
df["tenure_group"] = pd.cut(df["years_at_company"], [-1, 2, 5, 10, float("inf")],
                            labels=["0-2 yrs", "3-5 yrs", "6-10 yrs", "10+ yrs"]).astype(str)

print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Records:", df.duplicated().sum())
print(df["attrition_flag"].value_counts())

out_path = r"D:\Employee_Attrition_Analysis\data\processed\employee_attrition_cleaned.csv"
df.to_csv(out_path, index=False)
print("Final Shape:", df.shape, "| Saved at:", out_path)


# --- 2. DATABASE INGESTION ---
pwd = quote_plus(getpass("Enter PostgreSQL password: "))
engine = create_engine(f"postgresql+psycopg2://postgres:{pwd}@localhost:5432/employee_attrition_db")

with engine.connect() as conn:
    try:
        count = conn.execute(text("SELECT COUNT(*) FROM employee_attrition")).scalar()
    except Exception:
        conn.rollback()
        count = 0

    if count == 0:
        df.to_sql("employee_attrition", engine, if_exists="append", index=False, chunksize=500)
        count = conn.execute(text("SELECT COUNT(*) FROM employee_attrition")).scalar()

    print("Total records in PostgreSQL:", count)  

