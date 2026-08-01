student={
    "101":{
    "Name":"chithra",
    "age":23,
    "Roll_number":45
}}

print(student["101"]["age"])
print(student.get("101","name"))
#adding new key to it
student["city"]="banglore"
print(student.items())
#remove the item
student.pop("city")
print(student.items())
#update the value of the kry
student["age"]=24
print(student.items())
student.popitem()
print(student.items())
print(sorted(student))
print(student.items())
student.update({"102":{
    "roll_num":45,
    "city":"banglore",
    "marks":100
}})
print(student.items())

#printing only keys using loop dictionary
for i in student:
    print(i)

#printing only values from the dictionary

for i in student.values():
    print(i)

#printing both keys and values both using values

for i in student.items():
    print(i)



