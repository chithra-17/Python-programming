#1.remove duplicates from the list
lst=[1,1,2,3,5,4,4,6,7,7,8,9,8,7]
print(list(set(lst)))

#2.Union of two sets
sts1={1,2,3,4,4,5}
sts2={5,3,8,9,6}
print(sts1.union(sts2))

#3.intersection
sts1={1,2,3,4,4,5}
sts2={5,3,8,9,6}
print(sts2.intersection(sts1))

#4.Difference of two sets
sts1={1,2,3,4,4,5}
sts2={5,3,8,9,6}
print(sts1.difference(sts2))

#5.Symetric Difference
sts1={1,2,3,4,4,5}
sts2={5,3,8,9,6}
print(sts1.symmetric_difference(sts2))

#add
sts1={1,2,3,4,4,5}
print(sum(sts1))

#remove elements
sts1={1,2,3,4,4,5}
sts1.remove(3)
print(sts1)

#search elements
sts1={1,2,3,4,4,5}
if 2 in sts1:
    print("found")
else:
    print("not found")

#count unique elemets in list
lst=[1,2,3,4,4,5]
lst1=list(set(lst))

count=0

for i in lst1:
    count+=1
print(count)


