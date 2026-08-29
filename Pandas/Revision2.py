import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran", "Meena", "Rahul", "Anu"],
    "Age": [24, 27, 23, 29, 26, 31, 25, 28],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "HR"],
    "Salary": [35000, 45000, 30000, 55000, 42000, 60000, 48000, 50000],
    "City": ["Bangalore", "Chennai", "Bangalore", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi"]
})
# Create a new column called Bonus containing 10% of salary
df["Bonus"]=df["Salary"]* 0.10
#Create a Column called Anual Salary
df["Anaual_Salary"]=df["Salary"]*12
#Create a Column called Salary_After_Bonus
df["Salary_After_Bonus"]=df["Salary"]+df["Bonus"]
print(df)

#part b
#use apply() and lambda to increase every salary by 5%
df["Updated_Salary"]=df["Salary"].apply([lambda x:x*1.05])
#Use Aplly() to convert every name into upprcase
df["Upper_Name"]=df["Name"].apply([lambda x:x.upper()])
print(df)


#Part c
#String Operation
#Convert names to lowercase
df["Lower_Name"]=df["Name"].str.lower()
#Find the lenth of the each name
print(df["Name"].str.len())
#Find names that contain the letter "a"
print(df["Name"].str.contains("a"))
#Replace "a" with "@" in the names
print(df["Name"].str.replace("a","@"))

#part D
#find the total salary
print(df["Salary"].sum())
#average
print(df["Salary"].mean())
#highest
print(df["Salary"].max())
#lowest
print(df["Salary"].min())
#median
print(df["Salary"].median())
#num of unique
print(df["Salary"].nunique())
#find how many employees belong to each department
print(df["Department"].value_counts())

#part E
#find the average salary for each department
print(df.groupby("Department")["Salary"].mean())
#find the total salary in each department
print(df.groupby("Department")["Salary"].sum())
#maximum
print(df.groupby("Department")["Salary"].max())
#min
print(df.groupby("Department")["Salary"].min())
#num of employees in each Deaprt
print(df.groupby("Department")["Name"].count())

#part f
#22
print(df.groupby("Department")["Salary"].agg(
    Avg_sal="mean",
    min_sal="min",
    max_sal="max"
))
#23
print(df.groupby("Department").agg(
    Average_age=("Age","mean"),
    Total_sal=("Salary","sum")
))

