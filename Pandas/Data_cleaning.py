#Duplicates
import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45,  45],
    "Salary":[20000, 50000, 28000, 10000, 25000, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru","Bengaluru"]
}

df=pd.DataFrame(Data)
print(df.duplicated())
print(df.drop_duplicates())
df["city"]=df["city"].replace("bengaluru","Banglore")
print(df["city"])
print(df.duplicated(subset="Name"))
df["city"]=df["city"].replace({"bengaluru":"Banglore",
                              "Bengaluru":"Banglore"})
print(df["city"])

df=df.rename(columns={"city":"City"})
print(df.columns)
print(df.index)
df=df.rename(index={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"})
print(df)
print(df.index)

