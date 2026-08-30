import pandas as pd

employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104],
    "Name": ["Ravi", "Priya", "Arun", "Sneha"],
    "Department": ["IT", "HR", "IT", "Sales"]
})

salary = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 105],
    "Salary": [50000, 45000, 60000, 55000]
})

print(pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="inner"
))
print(pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="left"
))
print(pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="right"
))
print(pd.merge(
    employees,
    salary,
    on="Emp_ID",
    how="outer"
))
