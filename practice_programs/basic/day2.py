# A constructor is a special method used to initialize object values.

class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

s1 = student("Chithra",21)

print(s1.name)
print(s1.age)