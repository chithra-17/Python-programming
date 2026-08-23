import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, None, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru"]
}
df=pd.DataFrame(Data)

print(df.isna())
print(df.isnull())
print(df.isna().sum())
print(df.isna().mean()*100)
print(df.notna())
print(df.notnull())
print(df.dropna())
print(df.dropna(axis=1)) #column
print(df.dropna(axis=0)) #row
print(df.dropna(subset="Age")) #if you want to remove the row only Age value is missing
print(df.ffill()) #forward filling
print(df.bfill()) #backward filling
