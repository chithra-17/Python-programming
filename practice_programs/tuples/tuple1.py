tple1=(1,2,3,4,5)
print(tple1)

#Find maximum num without max()

tple1=(1,2,4,6,8,6,4,5)
#print(max(tuple))
maximum=tple1[0]
for i in tple1:
    if i>maximum:
        maximum=i
print(maximum)


#minimum num
tuple1=(1,1,2,4,6,8,6,4,5)
min=tuple1[0]
for i in tuple1:
    if i<min:
        min=i

print(min)

#find sum
tuple1=(1,2,4,6,8,6,4,5)
sum=0
for i in tuple1:
    sum+=i
print(sum)

# count occurrences
tuple1=(1,1,2,4,2,4,6,8,6,4,5)
print(tuple1.count(2))

#index of the element

tuple1=(1,2,4,6,8,6,4,5)
print(tuple1.index(6))

#list to tuple
lst=[1,2,4,6,8,6,4,5]
t=tuple(lst)
print(t)

#tuple to list
tuple1=(1,2,4,6,8,6,4,5)
print(list(tuple1))

#unpack tuple

tuple1=(6,4,5)
a,b,c=tuple1
print(a)
print(b)
print(c)

#access nested tuple
tuple1=(1,2,(3,5,4),5)
print(tuple1[2][0])
print(tuple1[2][1])
print(tuple1[2][2])

