"""tot = (1,5,9,7,3)
print(tot)"""
"""tot = (1,5,9,7,3)
print(len(tot))"""
"""tot = (1,5,9,7,3)
print(min(tot),max(tot))"""
"""tot = (1,5,9,7,3,3)
print(tot.count(3))"""
"""tot = (1,5,9,7,3)
print(tot.index(5))"""
"""tot = [1,5,9,7,3]
rrr = tuple(tot)
print(rrr)"""
"""rrr = (1,2,4,52)
ttt = (6,435,23)
qqq = rrr + ttt
print(qqq)"""
"""qqq = ("tyt","tewrt","werwe")
for  i in qqq:
    if i.startswith("t"):
        print(i)
    """
"""tot = [1,5,9,7,3]
rrr = tuple(tot)
yyy = list(rrr)
print(yyy)"""
"""tot = (9,2,5,7,4,6,2)
a = sum(tot)
print(a)"""
"""qqq = (1,2,3,4,5)
print(qqq[1:3])"""
"""qqq = (1,2,3,4,5)
for i in qqq:
    if 1 in qqq:
        print("true")
print(i)"""
"""qqq = (1,2,3,4,5)
b = qqq[::-1]
print(b)"""
"""qqq = (1,2,3,4,5)
def ooo(qqq):
    return ", ".join (map(str,qqq))
a = ooo(qqq)
l = [a]
print(l)"""
"""qqq = (1,2,3,4,5,6)
b =[]
for i in qqq:
    if i%2 == 0:
        b.append(i)
qqq = tuple(b)
print(qqq)"""
"""qqq = (1,2,3,4,5,5,4,3)
b=[]
for i in qqq:
    if i not in b:
        b.append(i)
qqq= tuple(b)
print(qqq)"""
"""qqq = ((2,6),(4,7),())
for i in qqq:
    for j in i:
        print(j)"""
        
"""qqq = ([321],(5),(3))
for i in qqq:
    if qqq is not list :"""
    
"""a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = a & b 
print(c)      """

"""a = {1,2,3,4,5,6,7,8,9,10}
b = {2,4,6,8,10}
a.difference_update(b)
print(a) 
"""

"""a = {1,3,5,7,9}
b = {2,4,6,8,10}
c = a | b
print(c)"""
"""
a = {1,2,3,4,5,6,7,8,9,10}
a.add(11)
print(a)"""

"""a = {1,2,3,4,5,6}
b = {7,8,9}
if b.issubset(a):
    print("b это под множество А")
else :
    print("false")"""
    
"""a = {1,2,2,3,3,3,4}
print(a)"""

"""a = {1,2,3,4}
b = {4,5,6,7}
print(a ^ b)"""

"""a = {}
if a == {}:
    print("True")
else:
    print("False")
    """
"""a = {1,2,3,4,5}
b = {2,3,4,5,6}
c = {3,4,5,6,7}
print(a & b & c)"""

"""a = {1,2,3,4,5}
b = {3,4,5,6}
print(a - b)"""

"""a = [1,2,3,4,5,5,5,1,3]
b = [2,4,5,2,5,4]
c = set(a)
d = set(b)
v = c | d
print(v)"""

"""a = {1,2,3,4,5,6,7}
print(7 in a)"""

"""a = {1,2,3,4,5,6,7,8,9,10}
import random
b = random.choice(tuple(a))
a.remove(b)
print(a)"""

"""a = {'asd','sad','ssa'}
b = "ssa"
if b in a:
    a.remove(b)
print(a)"""

"""a = {1,2,3,4,5}
b = {1.2,2.3,3.4}
c = a | b 
print(c)"""

"""a = {1,2,3}
a.clear()
print(a)"""

"""a = {7,8}
b = {4,5,6}
c = a & b
if a & b:
    print("True")
else:
    print("False")
"""
"""a = {1,2,3,4,5,6}
b = a.copy()

print(b)"""

"""a = {1,2,3,4,5,6,7}
print(max(a),min(a))"""

"""a = {1,2,3,4,5}
b = {6,7,8,9}
c = a | b
print(c)"""

"""a = [[1,2,3],[4,5,6]]
for  i in a :
    for l in i:
        print(l)"""
        
        
"""a = [[1,2,3],[4,5,6]]
b = 0
c = 0
for i in a:
    for j in i:
        b+= j
    c += b    
print(c)"""

"""a = [[1,2,3],[4,5,6]]
b = []
c = []
for i in a:
    for j in i:
        if  j%2 == 0:
            b.append(j)
        else:
            c.append(j)
print(b)"""

"""a = [[1,2,3],[4,5,6]]
b = []
for i in a:
    print(max(i))"""
    
"""a = [[1,2,3],[4,5,6]]
for i in a:
    print(len(i))
            """
            
"""a = [[4,5,6],[7,8,1]]
b=[]
for i in a:
    for j in i:
        if j>5:
            b.append(j)
print(b)"""

"""a = [[1,2,3],[4,5,6]]
for i in a:
    b = 1
    for j in i:
        b *= j
    print(b)
"""

"""a = [["jack"],["Python"],["Arnur"]]
for i in a:
    for j in i :
        if j == "Python":
            print("true")
        else:
            print("false")"""
            
"""a = [[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        """
        
"""a = [[1,2,3],[4,5,6]]
for i in a:
    for j in i:
        print(i.index(j))
        """
""""a = [[-1,2,3],[-4,5,-6]]
b = []
c = []
for i in a:
    for j in i :
        if j<0:
            j -= j
        b.append(j)
print(b)"""

"""a = [["Arnur"],["Cool"],["Tut"],["Lorento"]]
b= []
for i in a :
    for j in i:
        if len(j)>4:
            b.append(j)
print(b) """

"""a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b= a[0][0]+a[1][1]+a[2][2]
print(b)"""
"""
a = [
    [1,2,3,4,5,6],
    [7,8,9,10,11]
] 
b = []
for i in a :
    for j in i:
        if i.index(j) %2 >0:
           print(j)
"""

"""a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in a :
    for j in i:
        b = j*j
        print(b)"""
        
"""a = [[1,2,3],[4,5,6],[7,8,9]]
b = []
for i in a:
    for j in i:
        b.append(j)
print(b)"""

"""a = [[1,2,3],[4,5,6],[7,8,9]]
b = []
for i in a:
    b = sum(i)/len(i)
    print(b)"""
    
"""a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
g = a[1][0] + a[1][1] + a[1][2]
print(g) """

"""a = [[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    print(min(i))"""
    
"""a = [[-4,0,2],[9,0,21]]
b = []
c= []
for i in a :
    for j in i:
        if j == 0:
            b.append(j)
        else :
            c.append(j)
print(c)"""

"""a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b = len(a)
c =len(a[0])
for i in range(c):
    d = []
    for h in range(b):
        d.append(a[h][i])
    print(d)"""

"""class Car :
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    def get_description(self):
        return f"your car model {self.model} and brand {self.brand} "
        
car1 = Car("BMW", "M5")
car2 = Car("Toyota","Camry")
print(car2.get_description())
"""
"""class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def ploshad(self):
        return self.width * self.height
ploshad1 = Rectangle(5,9)
print(ploshad1.ploshad())"""
"""
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name 
    def Arnur(self):
        return f"Привет, меня зовут {self.name} и мне {self.age} лет"
Person1 = Person("Arnur","18")
print(Person1.Arnur())"""
        
"""class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self, ttt):
        if ttt>0:
            self._balance += ttt
            print(f"{ttt} поступила счет ")
        else :
            print("сумма не может быть отрицательной")
    def withdraw(self,ttt):
        if 0<ttt <self._balance:
            self._balance -= ttt
            print(f"{ttt} снят со счета")
        else:
            print("недостаточно средств")
    def get_balance(self):
        return self._balance
account = BankAccount(1000)
account.deposit(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())"""

"""class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} делает звуки"
class Dog(Animal):
    def speak(self):
        return f"{self.name} издает звук woof"
dog = Dog("Graf")
print(dog.speak())"""

"""class Bird:
    def __init__(self,name):
        self.name = name
class Fly:
    def fly(self):
        print(f"{self.name} может летать " )
class FlyingBird(Bird,Fly):
    def __init__ (self,name):
        Bird.__init__(self,name)
bird = FlyingBird("DERTER" )
bird.fly()"""

"""class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} издает звук meaw"
class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} издает звук woof"          
dog = Dog("Sezar")
cat = Cat("Tabriska")
print(cat.speak()) """

"""class Employee:
    employee_count = 0 
    def __init__(self,name):
        self.name = name
        Employee.employee_count+=1
    def get_employee_count():
        return Employee.employee_count
sot = Employee("Arnur")
sot2 = Employee("Anri")
print(Employee.employee_count)    """
"""
class MathOperations :
    def add(a,b):
        return a+b
result = MathOperations.add(7,8)
print(result)
    """
    
"""class Circle:
    def __init__(self,radius):
        self.radius = radius 
    def ret(self):
        return int(2 * 3.14 * self.radius)
ggg = Circle(5)
print(ggg.ret())"""
    
"""class Parent:
    def __init__(self,name):
        self.name = name
    def says(self):
        return f"Hello from {self.name}"
class Child(Parent):
    def __init__(self,name):
        self.name = name
    def says(self):
        return f"Hello from {self.name}"
name1 = Parent("Parent")
name2 = Child("Child")
print(name2.says())
"""
"""class Company:
    name = "Subzero"
    @classmethod
    def get_company_name(cls):
        return cls.name
print(Company.get_company_name())"""

"""class Book:
    avtor = "Pyshkin"
    name = "CLS"
    @classmethod
    def __str__(cls):
        return f"Автор книги{cls.avtor} название книги {cls.name}"
print(Book.__str__())"""

"""class Laptop:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"Добро пожаловать,{self.name}"
name1 = Laptop("Arnur")
print(name1.speak()) 
"""
"""a = ["Arnur","Anri","Sabit","Arman","Beknur"]
class Students:
    def __init__(self,name):
        self.name=name
for i in a:
    new_student=Students(i)
    print(new_student.name)"""
    
"""class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def JJJ(self,points):
        return ((points.x-self.x)**2 + (points.y - self.y)**2) ** 0.5
fff = Point(0,0)
rrr = Point(3,4)
qqq = fff.JJJ(rrr)
print(qqq)
        """
"""class School:
    def __init__(self,name):
        self.name=name
        self.classrooms=[]
    class Classroom:
        def __init__(self,number):
            self.number=number
            self.students=[]
        def add_students(self,student_name):
            self.students.append(student_name)
shool=School("High School 125")
classroom=shool.Classroom(87)
classroom.add_students("Sabit")
classroom.add_students("Sab")
shool.classrooms.append(classroom)

print(shool.name)
for i in shool.classrooms:
    print(f"CLassroom {i.number}: {', '.join(i.students)}")"""
    
"""class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
ss = {
    
}
def TTT(name,age,grades):
    new_student=Student(name,age,grades)
    ss[name] = {}
    student = ss[name]
    
    for key,value in vars(new_student).items():
        student[key] = value
       
TTT("Arnur",12,[9,56,88])
print(ss)"""

"""class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
aa = {}
def PPP(name,price,quantity):
    new_product=Product(name,price,quantity)
    aa[name] = {}
    product = aa[name]
    for key,value in vars(new_product).items():
        product[key] = value
PPP("Pomidor",777,7)
aa["Pomidor"]["quantity"] = 345
print(aa)"""

"""class Contact:
    def __init__(self,name,phone_number):
        self.phone_number = phone_number
        self.name = name
aa = {}
def TTT(name,phone_number):
    new_contact=Contact(name, phone_number)
    aa[name] = phone_number
TTT("Arnur","777")
print(aa)"""

""""class BankAccount:
    def __init__(self,balance,owner,account_number):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
aa = {}
def ppp(balance,owner,account_number):
    new_acccount = BankAccount(balance,owner,account_number)
    aa[account_number]= {}
    account_number = aa[account_number]
    for key,value in vars(new_acccount).items():
        account_number[key]=value
ppp("78996","777","9")
print(aa)
"""
"""class Subject:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
class Zhyrnal:
    def __init__(self):
        self.zhyrnal = {}
    def add_student(self,name_student):
        if name_student not in self.zhyrnal:
            self.zhyrnal[name_student] = {}
    def add_subject(self,name_student,subject:Subject):     
        if name_student in self.zhyrnal:
            if subject.name not in self.zhyrnal[name_student]:
                self.zhyrnal[name_student][subject.name] = []
    def add_great(self,name_student,subject_name,grades):
        if name_student in self.zhyrnal and subject_name in self.zhyrnal[name_student]:
            self.zhyrnal[name_student][subject_name].append(grades)
    def show_zhyrnal(self):
        for student,subject in self.zhyrnal.items():
            print(f"Student: {student} ")
        for subject,grades in subject.items():
            print(f"Yrok: {subject},Grades: {grades}")
a = Subject("Fizika","Sabit")
b = Subject("Matematika","Arman")
zhyrnal = Zhyrnal()
zhyrnal.add_student("Arnur")
zhyrnal.add_subject("Arnur",a)
zhyrnal.add_subject("Arnur",b)
zhyrnal.add_great("Arnur","Fizika",9)
zhyrnal.add_great("Arnur","Matematika",7)
zhyrnal.add_great("Arnur","Matematika",6)
zhyrnal.show_zhyrnal()
"""
"""class Course:
    def __init__(self,name,instructor,student):
        self.name = name
        self.instructor = instructor
        self.student = student
course = Course("Pyton разроботчик","Sabit",["Arnur","David"])
courses = {}
courses[course.name] = {}
courses[course.name]["instructor"] = course.instructor
for i in course.student:
    courses[course.name][i] = 99
print(courses)"""
"""
class Car:
    def __init__(self,make,model,year,owner):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner 
    def change_owner(self,new_owner):
        self.owner = new_owner
car = Car("USA","x","2006","Arnur")
c = {
    
}
def add_car(car):
    c[car.owner] = car
add_car(car)
for owner,car in c.items():
    print(f"Vladeles: {owner}, Marka: {car.make}, Model: {car.model}, year: {car.year}")

car.change_owner("Anri")
add_car(car)


for owner,car in c.items():
    print(f"Vladeles: {owner}, Marka: {car.make}, Model: {car.model}, year: {car.year}")"""
    
"""class Book :
    def __init__(self,title,autgor,year):
        self.title = title
        self.autgor = autgor
        self.year = year
books = Book("xxxxx","yyyy","2006")
c= {}
def add_book(book):
    c[books.title] = books
add_book(books)
a = input("введите название киниги")
if a in c :
    print(c[a])"""
    
"""class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
sotrydnik1 = [Employee("Arnur","student",2000)]
sotrydniki = {}
for i in sotrydnik1:
    sotrydniki[i.name] = {}
    dict = i.__dict__
    for key,value in dict.items():
        sotrydniki[i.name][key] = value 
        
    def HHH(dict):
        a = input("vvedite sotrydnika ")
        b = int(input("vvedite zarplaty "))
        dict[a]["salary"] = b
        
HHH(sotrydniki)
print(sotrydniki)"""
"""
class Task:
    def __init__(self,discription,status,deadline):
        self.discription = discription
        self.status = status
        self.deadline = deadline
    def HHH(self,new_status):
        self.status = new_status
tasks_dict = {"выучить пайтон": Task("изучить язык програмирования python и стать разроботчиком", "Не выполнено","пол года ")}
tasks_dict["выучить пайтон"].HHH("выполнено")
print(tasks_dict["выучить пайтон"].__dict__)"""

"""class Movie:
    def __init__(self,title,director,release_year):
        self.title = title
        self.director = director
        self.release_year = release_year
movies = Movie("mas","ytt","ttt")
movie = {}
def add_movie(dict,title,director,release_year):
    dict[title]=Movie(title,director,release_year)
add_movie(movie,"Titanik ","Arnur", "2006")
def find_cinema(director,dict):
    for i in dict.values():
        i = i.__dict__
        if director == i["director"]:
            print(i["title"])
find_cinema("Arnur",movie)"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
students = ["Arnur","Anri","Sabit","Arman"]
course = {}
class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    def add_student(self,student):
        self.students.append(student)
    def list_students(self):
        if self.students:
            print(f"студенты на курсе {self.course_name}")
            for student in self.students:
                print(f"name: {student.name} age: {student.age}")
        else:
            print("пока нет студентов")
def add_course(dict,course_name):
    dict[course_name] = Course(course_name)
def register(dict,course_name,student):
    if course_name in course:
        dict[course_name].add_student(student)
    else:
        print("курс не найден")
def list_student(course_name,dict):
    if course_name  in course:   
        dict[course_name].list_students()
    else:
        print("курс не найден")
add_course(course,"Python programing")
student1 = Student("Arnur", 18)
register(course,"Python programing",student1)
list_student("Python programing",course)

