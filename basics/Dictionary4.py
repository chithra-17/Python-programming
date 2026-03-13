#maximun frequent element

num=[1,2,2,2,3,3,4,5,6,7,7]
count={}
max_value=0
max_key=None

for i in num:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
# this part is without shortcut{       
#for key,value in count.items():
#   if value>max_value:
#      max_value=value
#     max_key=key
#print(max_key)
#     }

#max(count) == it gives largest key
#max(count.value())== it give largest value

# this one is with shortcut
print(max(count,key=count.get)) # it gives key with largest value
