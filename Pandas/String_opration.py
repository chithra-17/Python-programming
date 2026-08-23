import pandas as pd
Data={
    "Name":[" ravi ", " priya", "arjun", " sneha", "kiran "],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, 10000, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru"]
}

df=pd.DataFrame(Data)
df["Name"]=df["Name"].str.upper()
print(df["Name"])
df["Name"]=df["Name"].str.lower()
print(df["Name"])
df["Name"]=df["Name"].str.title()
print(df["Name"])
df["Name"]=df["Name"].str.strip()
print(df["Name"])
df["Name"]=df["Name"].str.len()
print(df["Name"])
df["Salary"]=df["Salary"].rank()
print(df["Salary"])
df["Salary"]=df["Salary"].rank(ascending=False)
print(df["Salary"])







