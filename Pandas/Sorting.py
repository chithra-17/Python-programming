import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, 10000, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru"]
}
df=pd.DataFrame(Data)
df2=df["Salary"].sort_values()
print(df2)
print(df["Salary"].sort_values(ascending=False))
print(df["Salary"].sort_values(ascending=False).reset_index())
print(df["Salary"].sort_values(ascending=False).reset_index(drop=True))
df["Rank"]=df["Salary"].rank(ascending=False)
print(df[["Name","Salary","Rank"]])
