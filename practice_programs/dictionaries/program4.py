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

    



