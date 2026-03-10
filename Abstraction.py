from abc import ABC, abstractmethod
# abc is a built in module of python
# 1.ABC is used to create abstract class
# 2. abstractmethod is used to declare a method that must be implemented by child classes

class Animal(ABC): #ABC must write, otherwise it is not considered as abstract class

    def sleep(self):
        print("animal sleeping")

    @abstractmethod #this must be implemented in all the child class
    def sound(self):
        pass

class dog(Animal):
    def sound(self):
        print("Bark")
    
d = dog()
d.sleep()
d.sound()

# We cannot create object for animal class coz it is abstract class it doesnt work.When class contain an abstract method, Python does not aloow creating its object.

