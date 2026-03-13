#Frequency of numbers

num=[1,2,2,2,3,3,4,5,6,7,7]
count={}

for i in num:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)