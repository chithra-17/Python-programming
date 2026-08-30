import pandas as pd

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
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
    left_on="Employee_ID",
    right_on="Emp_ID",
))