#sort by its value
marks={
    "English":48,
    "Hindi":35,
    "math":50
}

Sorted_marks=dict(sorted(marks.items(), key=lambda x:x[1]))
print(Sorted_marks)

#create dictionary from 2 list(one is key and one is value)

keys=["name","class","marks"]
values=["chithra",7,35]

student={}

for i, j in zip(keys,values):
    if i not in student:
        student[i]=j
print(student)
#{'name': 'chithra', 'class': 7, 'marks': 35}

