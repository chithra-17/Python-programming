import pandas as pd 
df1 = pd.DataFrame({
    "Name": ["A", "B"],
    "Salary": [30000, 40000]
})

df2 = pd.DataFrame({
    "Name": ["C", "D"],
    "Salary": [50000, 60000]
})

print(pd.concat(
    [df1,df2],
    ignore_index=True,
    axis=0
))

df3 = pd.DataFrame({
    "Department": ["IT", "HR"]
})

print(pd.concat(
    [df1,df3],
    ignore_index=True,
    axis=1
    ))


left = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun"]
}, index=[101, 102, 103])

right = pd.DataFrame({
    "Salary": [50000, 45000, 60000]
}, index=[101, 102, 103])

print(left.join(right))

sales = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Gender": ["M", "F", "M", "F", "M", "F"],
    "Salary": [50000, 60000, 40000, 45000, 55000, 65000]
})

df4=pd.pivot_table(
    sales,
    index="Department",
    columns="Gender",
    values="Salary"
)
print(df4)
df5=pd.pivot_table(
    sales,
    index="Department",
    columns="Gender",
    values="Salary",
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)
print(df5)

df6=pd.pivot_table(
    sales,
    index="Department",
    columns="Gender",
    values="Salary",
    aggfunc="max",
    margins=True,
    margins_name="maximum"
)
print(df6)


