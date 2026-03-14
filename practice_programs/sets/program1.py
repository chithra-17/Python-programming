#1.Remove Duplicates
#Input: [1,2,2,3,4,4]
#Output: [1,2,3,4]

num=[1,2,2,3,4,5,]
print(list(set(num)))

#2.Find common Elements
#a = [1,2,3,4]
#b = [3,4,5,6]
#Output: [3,4]


a=[1,2,3,4]
b=[3,4,5,6]
#set(a) created not stored
#set(b) created not stored
result=set(a) & set( b) #list tempararily converted to set. it doesnt convert a variable value from list to set
print(list(result)) # here result havong set output so we need to convert to list

#3.Check Duplicates Exists
#Input: [1,2,3,3,4]
#Output: True

List=[1,2,3,3,4]
sets=set(List)

if len(List) != len(sets):
    print(True)
else:
    print(False)

# Sets do not maintain order, so sometimes output order may change.
#ex:
#[1,2,3,4,5]
#or
#[2,1,3,5,4]
# so in order to maintain we can use loop for this.