#find the length of the dictionary

student={
    "Name":"chithra",
    "age":23,
    "Roll_number":45
}
print(len(student))

#Count the frequency of each character in a string
s="apple"
freq={}

for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#Count the frequency of the each number in list
lst=[1,2,3,2,2,3,3,2,4,5,5,3,2]
freq1={}

for i in lst:
    if i in freq1:
        freq1[i]+=1
    else:
        freq1[i]=1
print(freq1)

#find the key with max value

student={
    "Name":66,
    "age":23,
    "Roll_number":45
}
print(max(student, key=student.get))

#or using loop

student={
    "Name":66,
    "age":23,
    "Roll_number":45
}
max_key=""
max_value=-1

for keys in student:
    if student[keys]>max_value:
        max_value=student[keys]
        max_key=keys

print("max value:",max_value)
print("max key:",max_key)


#find the key with minimum value

student={
    "Name":66,
    "age":23,
    "Roll_number":45
}
keys=list(student.keys())
min_key=keys[0]
min_value=student[min_key]

for key in student:
    if student[key]<min_value:
        min_key=key
        min_value=student[key]

print(min_key,":",min_value)
          

