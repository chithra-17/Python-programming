import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran", "Meena", "Rahul", "Anu"],
    "Age": [24, 27, 23, 29, 26, 31, 25, 28],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "HR"],
    "Salary": [35000, 45000, 30000, 55000, 42000, 60000, 48000, 50000],
    "City": ["Bangalore", "Chennai", "Bangalore", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi"]
})
#Display first five rows
print(df.head())
#Display last 3 rows
print(df.tail(3))
#Find the number of rows and columns
print(df.shape)
#Display all columns
print(df.columns)
#Display the datatypes
print(df.dtypes)
#Display the statistical summary
print(df.describe())

#Part B
#select only the name of the column
print(df["Name"])
#select Name, Salary, Dapartment
print(df[["Name", "Salary", "Department"]])
#Using loc, Select rows 0 to 3 and only name and Salary column
print(df.loc[0:3,["Name","Salary"]])
#Using iloc, Select the first 4 rows and first 3 columns
print(df.iloc[0:4,0:3])


#part C
# Find Employees Whose Salary is grater than 45000
print(df.loc[df["Salary"]>45000,["Name", "Salary"]])
#Find Employees Whose dwpartment is IT
print(df.loc[df["Department"]=="IT",["Name","Department"]])
#Find the employee Whose Age is Greater than 25 and Slary is Greater than 40000
print(df.loc[(df["Age"]>25) & (df["Salary"]>40000),["Name","Age","Salary"]])
#Find the Employee who are from either Banglore and Delhi
print(df.loc[(df["City"]=="Bangalore") | (df["City"]=="Delhi"),["Name","City"]])

#Part D
# Sort the Dataframe by salary from hieghest to lowest
data=df.sort_values(by="Salary",ascending=False).reset_index(drop=True)
print(data)

#Cleaning
df.loc[2, "Salary"] = None
df.loc[5, "City"] = None

df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print(df)
print(df.isna().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)
df["City"]=df["City"].fillna("Unknown")
print(df)
df.info()
print(df.describe())