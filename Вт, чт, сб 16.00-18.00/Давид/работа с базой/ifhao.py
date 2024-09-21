'''class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def a(self):
        return f"model: {self.model}, brand: {self.brand}"
toyota = Car("toyota", "camry")
gelik = Car("mercedes", "G63")
print(toyota.a(), gelik.a())'''
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def rewr(self):
        return self.width * self.height
squr = Rectangle(9, 8)
print(squr.rewr())'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eqeq(self):
        return f"Привет, меня зовут {self.name} и мне {self.age} лет"
Dav = Person("David", 17)
print(Dav.eqeq())