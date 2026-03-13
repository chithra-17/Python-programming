#Remove duplicate
num=[1,2,2,2,3,4,5,5,5,3]

temp=[]

for i in num:
    if i not in temp:
        temp.append(i)

print(temp)