#find missing number

list1=[1,2,3,5]
x=5
expected=x*(x+1)//2
actual=sum(list1)

result=expected - actual
print(result)

#seperate even and odd  num
list1=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# find maximum and minimun without using max and min function

list1=[1,2,4,55,6,78,89]
maximum=list1[0]
minimum=list1[0]
for i in list1:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(maximum)
print(minimum)

    
