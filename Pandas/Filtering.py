#Filtering
import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, 10000, 25000],
    "city":["mysuru", "bengaluru", "Hassan", "shivamogga", "Bengaluru"]
}
df=pd.DataFrame(Data)
print(df["Salary"]>30000)

#df2=df["Salary"]>30000 if we want to store the data
#print(df2)

#isin()
print(df["city"].isin(["mysuru","bengaluru"]))

#between
print(df["Salary"].between(20000,40000))

#info
print(df.info())

#describe()
print(df.describe())

#specific column only needed to print
print(df[df["Salary"]>30000][["Name","Salary"]])

