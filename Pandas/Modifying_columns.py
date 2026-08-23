import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, 10000, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru"]
}
df=pd.DataFrame(Data)
#Creating new column
df["Bonus"]=df["Salary"]+5000
print(df["Bonus"])
print(df)
#Creating Column Using MUltiple Columns
df["Bonus2"]=df["Salary"]+df["Bonus"]
print(df["Bonus2"])
df=df.drop(columns="Bonus2")
print(df)
#Adding new column using insert
df=df.insert(1,"Bonus2",[3000,4000,5000,6000,7000])
print(df)