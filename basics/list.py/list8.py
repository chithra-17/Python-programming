#second largest element

lst=[1,2,3,4,5]
lst2=sorted(lst)
lst2.reverse() #or print(list2[-2])
print(lst2[1])


# largest element in list without max() func
lst3=[2,6,7,4,9]
largest=lst3[0]
for i in lst3:
    if i>largest:
        largest = i
print(largest)

#smallest element without min() func
lst4=[2,6,7,4,9]
smallest=lst4[0]
for i in lst4:
    if i < smallest:
        smallest = i
print(smallest)

