#Find Max num in tuple

t=(5,8,2,10,3)
max=t[0]
for i in t:
    if i>max:
        max=i
    
print(max)