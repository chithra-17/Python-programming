student={
    "101":{
    "Name":"chithra",
    "age":23,
    "Roll_number":45
}}
if "Name" in student["101"]:
    print("Exixting")
else:
    print("not Existing")

    #or

#suppose chck if the nested dictionary itself existing

if "101" in student and "Name" in student["101"]:
    print("Exixting")
else:
    print("not Existing")

    #or
#using get

if "Name" in student.get("101",{}):
    print("Exixting")
else:
     print("not Existing")