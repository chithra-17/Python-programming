import pandas as pd
Data={
    "Name":["ravi ", "priya", "arjun", "sneha", "kiran"],
    "Age":[ 25, 28 , 30, 23, 45],
    "Salary":[20000, 50000, 28000, 10000, 25000],
    "city":["mysuru", "bengaluru", "Hassa", "shivamogga", "Bengaluru"]
}
df=pd.DataFrame(Data)
#Selecting Rows and columns using .iloc
#Integer - location based selection
#df.iloc[row_position,column_position]

#Selecting one cell using .iloc
print(df.iloc[2,2])



