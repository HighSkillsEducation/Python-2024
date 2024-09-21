'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f'Hello! my name is {self.name} and i am {self.age} years old.'
person1 = Person("Mike", 25)
print(person1.greet())
'''



'''class Car:
    def __init__(self, brend, model):
        self.brend = brend
        self.model = model
    def greet(self):
        return f'Brend: {self.brend}, model: {self.model}'
        
car1 = Car('Mercedes-Benz', 'w211')
car2 = Car('Mercedes-Benz', 's-63')
print(car2.greet())
'''




'''class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def greet(self):
        return self.height * self.width 
result = Rectangle(20, 10)
print(result.greet())
'''





'''class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, num):
        self._balance += num
    def withdraw(self, num1):
        self._balance -= num1
    def get_balance(self):
        return self._balance
balance = BankAccount(2000)
balance.withdraw(100)
print(balance.get_balance())
'''




'''class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} makes a sound!' 
class Dog(Animal):
    def speak(self):
        return f'{self.name} says woof!'
dog1 = Dog('Fred')
print(dog1.speak())
'''




''''class Bird:
    def __init__(self, name):
        self.name = name
    def fly(self):
        return f'{self.name} fly!'
class Fly:
    def __init__(self, name):
        self.name = name
    def bird(self):
        return f'{self.name} fly to heaven!'
class Flyinbird(Bird, Fly):
    def flyed(self):
        return f'Fly and dont fall {self.name}!'
bird = Flyinbird('Markus')
print(bird.bird())
'''




'''class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says meow!'
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says woof!'
animal = [Dog('Mark'), Cat('Anna')]
print(animal[1].speak())
'''






class Worker:
    employee_count = 0
    def __init__(self, name):
        self.name = name
    def update_employee(self):
        employee_count += 1
        return employee_count
newrab = Worker("Aaaa")
print(newrab.update_employee())