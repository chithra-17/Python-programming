import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, 10000, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru"]
}
df=pd.DataFrame(Data)
#print(df)
print(df["Name"])
print(df[["Name","Salary"]])

#Selecting columns using .loc
print(df.loc[:,"Name"])
#df.loc[rows, column]
#df.loc[row_label, column_label]
#index values are label too

#Selecting one row with .loc
print(df.loc[0])

#selecting a Specific cell with .loc
print(df.loc[0,"Name"])

#selecting Multiple Columns with .loc
print(df.loc[:,["Name","Salary"]])

#Selecting Specific Rows and Columns
print(df.loc[1:3,["Name","Salary"]])


