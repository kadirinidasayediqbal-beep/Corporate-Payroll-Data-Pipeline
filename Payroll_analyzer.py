import pandas as pd

# 1. Create the dataset (Mirroring our exact MySQL records!)
data = {
    'employee_id':[1 ,2 ,3 ,4 ,5 ,6],
    'employee_name':['Amit Sharma', 'Neha Patil', 'Rahul Verma', 'Priya Nair', 'Vikram Malhotra', 'Senha Farnandes'],
    'base_salary':[45000, 65000, 32000, 50000, 72000, 28000],
    'gender':['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'department':['IT', 'HR', 'IT', 'Finance', 'Finance', 'HR']
}

# 2. Load data into Pandas DataFrame (Think of this like a SQL Table)
df = pd.DataFrame (data)
print("---Raw Corporate Roster---")
print(df)
print('\n' + "="*40 + "\n")

# 3. BUSINESS ANALYSIS EXERCISE : Group by Department
# Standard dictionary aggregation syntax
dept_summary = df.groupby('department').agg({
    'base_salary': ['sum', 'mean'],
    'employee_id': 'count'
}).reset_index()

# Flatten out the column names so they look clean
dept_summary.columns = ['department', 'total_budget', 'average_salary', 'employee_count']

print("--- Departmental Insights Report ---")
print(dept_summary)

# 4. Export the findings to a clean CSV file for business stakeholders
dept_summary.to_csv ('department_insights.csv', index=False)
print("\n[SUCCESS] Report exported to 'department_inshights.csv'!")
