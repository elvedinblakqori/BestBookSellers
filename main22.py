class Person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi my name is {self.name} , and I am {self.age} years old")

person1 = Person("Trim" , 17)

person1.greet()


class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

r1 = Rectangle(5 , 2)

print(r1.area())

class Pet:
    def __init__(self , name , age, species , breed , color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color =  color

