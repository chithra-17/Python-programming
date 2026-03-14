#Count even number in Tuple

t=(1,2,3,4,5,6)
count=0
for i in t:
    if i%2==0:
        count +=1
print(count)