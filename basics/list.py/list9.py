# reverse method
lst=list(map(int, input().split()))

lst.reverse()
print(lst)

#sorting ascending
lst2=[1,2,3,4,5,6]
lst2.sort()
print(lst2)

#sorting descending
lst2.sort(reverse=True)
print(lst2)

# remove duplicates
lst3=[1,4,4,4,4,6,7,8,8,8,9]
lst4=list(set(lst3))
print(lst4)

#count even num
lst5=[1,2,3,4,5,6,7,8,9]
count=0
for i in lst5:
    if i%2==0:
        count+=1
print(count)

#count odd num
lst6=[1,2,3,4,5,6,7,8,9]
count=0
for i in lst6:
    if i%2==0:
        continue
    count+=1
print(count)

#search an element
lst7=[2,3,4,5,6,7,8]
x=int(input())
if x in lst7:
    print("found")
else:
    print("not found")

# merge 2 list (concatination)
list1=[1,2,3]
list2=[3,4,5]
print(list1+list2)

#find common elements
list1=[1,2,2,3,4,]
list2=[1,2,3]
comon=[]
for i in list1:
    if i in list2:
        comon.append(i)
print(comon)




