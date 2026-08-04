#sum of all the value in dictionary

marks={
    "math":20,
    "english":30,
    "kannada":25
}
total=0
#print(sum(marks.values())) without loop
for i in marks.values(): #using loop
    total+=i

print(total)

#merge two dictionary

student={
    "Name":"chithra",
    "age":23,
    "Roll_number":45
}
marks={
    "math":20,
    "english":30,
    "kannada":25
}
info={}
info.update(student)
info.update(marks)
print(info)

# if we want it in nested dictionary 

student={
    "Name":"chithra",
    "age":23,
    "Roll_number":45
}
marks={
    "math":20,
    "english":30,
    "kannada":25
}
info={
    "student":student,
    "marks": marks
}
print(info)

#reverse dictionary
student={
    "Name":"chithra",
    "age":23,
    "Roll_number":45
}
rev={}

for i in student:
    rev[student[i]] = i 

print(rev)

#If want to print keys and values of required index.
first_value=list(student.items())[0]
print(first_value)

#if u want to print all keys and values
for key, value in student.items():   
    print(key, value)

#Group words by their first letter

lst=["APPLE","AMLA","BANANA","BREAD","CAT","DOG"]

GROUP={}

for word in lst:
    first_value1=word[0]

    if first_value1 not in GROUP:
        GROUP[first_value1]=[]
    GROUP[first_value1].append(word)
print(GROUP)

#output:{'A': ['APPLE', 'AMLA'], 'B': ['BANANA', 'BREAD'], 'C': ['CAT'], 'D': ['DOG']}

#find duplicate elements in list using dictionary
num1=[10,20,30,40,30,20,10,30,20]

GROUP1={}

for i in num1:
    if i in GROUP1:
        GROUP1[i]+=1
    else:
        GROUP1[i]=1
print(GROUP1)

#{10: 2, 20: 3, 30: 3, 40: 1}

## find the first non-repeating character in string
#using list
name1="apple"
lst1=[]

for i in name1:
    if i not in lst1:
        lst1.append(i)
print(lst1[0])
#using dictionary
txt="programming"
count={}

for char in txt:
    if char in count:
        count[char]+=1
    else:
        count[char]=1

for i in count:
    count[i]==1
    print(i)
    break

#sort dictionary with its values

marks={
    "English":48,
    "Hindi":35,
    "math":50
}

min=list(marks.values())[0]

for i in marks.values():
    if i < min:
        min=i
print(min)




