#Inheritance

class Animal:

    def speak(self):
        print("Animal makes sound")

class dog(Animal):
    pass

d=dog()
d.speak()