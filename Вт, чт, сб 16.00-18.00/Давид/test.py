'''
a = [1,2,23,41,42,42,6346,4213]

b = [52,4,235,324,341,4142,6346]
c = a + b

for i in c:
    if c.count(i) != 1:
        c.remove(i)
            
print(c)

c = set(c)
c = list(c)
print(c)
'''
'''
a = [1,2,3,4,5,6,7,8,9,10]
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
        
    elif i % 2 != 0:
        c.append(i)
        
print(b)
print(c)
'''
'''
a = [1,52,67,47,84,525,46,85,73,75,543,745,52,73,75,525,46,47,89,47,47]
b = int(input())
for i in a:
    if b == i:
        a.remove(i)
print(a)
'''
'''
a = ['a', 'b', 'adw', 'dwajidja', 'l', 'tie', 'iu']
d = ['a', 'b', 'adw', 'dwajidja', 'l', 'tie', 'iu']

b = sorted(a, key=len)
d.sort(key=len)
print(b)
print(d)
'''
'''
a = []
amount = []
fruits = ['apple', 'banan', 'watermelon']
fruits_price = [100,200,300]
while True:
    print('\nMenu:')
    print('1. Dobavit tjvar v spisok')
    print('2. Udalit tovar iz spiska')
    print('3. pokazat spisok')
    print('4. pokazat obshee kolichestvj tovarov')
    print('5. search')
    print('6. Vihod')
    choice = input('Viberit deistvie (1-6): ')
    if choice == '1':
        c = input('kakoi tovar vi hotite: ')
        if c in a:
            print('etot tovar uzhe est v spiske')
        else:
            a.append(c)
            f = int(input('kolichestvo tovara: '))
            amount.append(f)
    elif choice == '2':
        d = input('kakoi tovar vi hotite udalit: ')
        if d in a:
            a.remove(d)
            print('etot tovar ubran')
        else:
            print('takovo tovara net')
    elif choice == '3':
        print('vash spisok')
        i = 0
        for j in range(len(a)):
            i +=1
            print(f'{i}. {a[j]} - amount {amount[j]}')
    elif choice == '4':
        print(len(a))

    elif choice == '5':
        e = int(input('vvedite nomer tovara: '))
        if e < len(a):
            if a[e] in fruits:
                print(f'takoi tovar est {fruits_price[fruits.index(a[e])]}')
            else:
                print('takogo tovara net')
    elif choice == '6':
        print('vi vishli iz magazina')
        break
        '''
'''
for i in range(2,10):
    print(i)
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')
        
'''
'''a = input()
b = ['a', 'u', 'i', 'o', 'e']
c = 0
a = a.lower()
for i in b:
    
    if i in b:
        c = a.count(i)
        print(f'{i} : {c}')
        b.remove(i)
    for j in a:
            if j == i:
                c += 1
    print(f'{i} : {c}')
    c = 0'''    
'''
a = int(input())
b = a
for i in range(a):
    for j in range(b):
        print('*', end=" ")
    print('\n')
    b -= 1
'''
'''
c = 0

for i in range(1,101):
    if i == 1:
        c += 1
    
    for j in range(1, i+1):
        if i % j == 0:
            c += 1
    if c == 2:
        print(i)
    c = 0
    '''
'''
a = int(input())
b = a
for i in range(1,a+1):
    for j in range(1,i+1):
        print(f'{j}', end='')
    print('')
    b -= 1
    '''
'''
import random
n = int(input())
b = []
d = 0
f = ''
for i in range(n):
    c = []
    for j in range(n):
        e = random.randint(0,100)
        d += e
        f = f +' '+ str(e)
        c.append(e)
        
    b.append(c)
    
print(f)    
for k in range(n):
    print(b[k][k])

print(d)
'''
''''''
'''
import random
f = 0
grades = []
item = ['математика', 'информатика', 'казахский', 'английский', 'физика']
print('Меню изменения списков ' )

students_name = []
menu = [
    '1. Обновить оценки студента',
    '2. Добавить нового студента',
    '3. Удаление студента из списка учащихся',
    '4. Добавить в список новый предмет',
    '5. Удаление предмета из списка',
    '6. Ничего не делать',
    '7. удалить оценку'
]
def callMenu():
    for u in menu:
        print(u)
def programm():
    global f
    
    while True:
    
        name = input('ФИО студента: ')
        if name.lower() != 'выход' and name != '0':
            students_name.append(name)
        if name.isdigit() == True:
            print('такое не может быть в ФИО')
        if name == '0':
            callMenu()
           
        if name.lower() == 'выход':
            break

    for i in range(len(students_name)):
    
        print(f"{students_name[i]}: ")
        grad = []
        for j in range(len(item)):
            e = random.randint(0,100)
            grad.append(e)
            min_n = min(grad)
            min_i = grad.index(min_n)
            max_n = max(grad)
            max_i = grad.index(max_n)
            print(f"{item[j]}:{grad[j]}")
        print(f"Максимальный балл по {item[max_i]}: {max_n} \n Минимальный балл по {item[min_i]}: {min_n}")
        for h in range(len(grad)):
            f += grad[h]
        print(f'Средний балл: {f/len(grad)}')
        if f/len(grad) < 60:
            print(f"{item[min_i]}: {min_n}")
        
        f = 0

while True:
    list_editing = input('Старт программа')
    if list_editing.lower() == 'добавить студента':
        programm()
    if list_editing.lower() == 'стоп':
        break
def progr():
    '''
'''
import random
students = []
grades = [
    ['математика', 'информатика', 'казахский язык', 'английский язык', 'физика'],
    []
]
menu = [
    '1. Добавить студента', 
    '2. удалить студента',
    '3. Изменить оценки',
    '4. Добавить предметы',
    '5. Удалить предметы',
    '6. Остановить программу'
]
def menuOutput():
    for i in menu:
        print(i)
def menuFunc():
    g = int(input('Выберите опцию: '))
    if g == 1:
        addstudent()
    elif g == 2:
        removestudent()
    elif g == 3:
        changegrades()
    elif g == 4:
        addlesson()
    elif g == 5:
        removelesson()
        
def start():
    while True:
        h = int(input('Чтобы открыть меню напишите 0, а чтобы завершить программу нажмите 6: '))
        if h == 0:
            menuOutput()
            menuFunc()
        elif h == 6:
            break
def addstudent():
    while True:
        student = input("Введите ФИО студента или 'Стоп' для завершения: " )
        if student.strip().lower() == 'стоп':
            break
        if student.isalpha():
            students.append(student)
            grades[1].append([])
            creategrades(grades[1][-1])
        else:
            print('Неверный формат вводимых данных')
    outputstudentswithgrades()
def removestudent():
    if not students:
        print('список студентов пуст')
        return
    index = int(input("Введите номер из списка начиная с нуля: "))
    if 0<= index<len(students):
        students.pop(index)
        grades[1].pop(index)
    else:
        print('Неверный индекс студента')
    outputstudentswithgrades()
def changegrades():
    if not students:
        print('список студентов пуст')
        return
    indexoffstudents = int(input("Введите индекс студента начиная с нуля чьи оценки хотите изменить: "))
    if 0<=indexoffstudents<len(students):
        if not grades[1][indexoffstudents]:
            print("оценки для данного студента не установлены")
            return
        indexofgrades = int(input("Введите индекс предмета оценку по которому нужно изменить: "))
        if 0<=indexofgrades<len(grades[0]):
            grade = input("Введите новую оценку: ")
            if grade.isdigit():
                 grades[1][indexoffstudents][indexofgrades] = int(grade)
            if int(grade)<0:
                print('Оценка не может быть ниже нуля')

            else:
                print('Неверный формат вводимых данных')
        else:
            print("Неверный индекс предмета")
    else:
        print('Неверный индекс студента')
    outputstudentswithgrades()
def addlesson():
    lesson = input('Введите названия предмета: ')
    if lesson not in grades[0]:
        grades[0].append(lesson)
        for studentgrades in grades[1]:
            studentgrades.append(random.randint(0,100))
    else:
        print('Такой предмет уже существует')
    outputstudentswithgrades()
def removelesson():
    if not grades[0]:
        print('Список предметов пуст')
        return
    print('Список предметов:')
    for idx, lesson in enumerate(grades[0]):
        print(f'{idx}. {lesson}')
        index = int(input("Введите индекс предмета который хотите удалить: "))
        if 0<= index<len(grades[0]):
            grades[0].pop(index)
            for studentgrades in grades[1]:
                studentgrades.pop(index)
        else:
            print('Неверный индекс предмета')
        outputstudentswithgrades()
def creategrades(gList):
    for _ in range(len(grades[0])):
        gList.append(random.randint(0, 100))
    
def outputgrades(student_index):
    for k in range(len(grades[0])):
        print(f"{grades[0][k]}: {grades[1][student_index][k]} баллов")
def outputstudentswithgrades():
    if not students:
        print('список студентов пуст')
        return
    for student_index in range(len(students)):
        print(f"{students[student_index]}")
        outputgrades(student_index)
        max_grades()
        med_grades()
        min_grades()
def max_grades():
    for i in range(len(students)):
       maxgrade = max(grades[1][i])
    print(f'Максимальный балл: {maxgrade}') 
def med_grades():
    sum = 0
    for y in range(len(students)):
        for o in grades[1][y]:
            sum += o  
    print(f"Средний балл: {sum/(len(grades[0])+1)}")
    sum = 0
def min_grades():
    for i in range(len(students)):
       mingrade = min(grades[1][i])
    print(f'Минимальный балл: {mingrade}')
start()
'''
'''
a = int(input())
b = a
for i in range(a):
    for j in range(b):
        print('*')
        print('\n')
    b += 1
    '''
'''
a = 24
b = 56
def f(g,t):
    return g+t
print(f(15, 30))
def h(y,h):
    d = y+h
    return d
print(h(a, b)) #так тоже можно
'''
'''
a = 523
def f(b):
    b = 42
f(a)
print(a)
'''
'''
def f():
    a = 41
    b = 4653
    c = a+b
    return c
print(f())'''
'''
def hello(name="User"):
    print(f"Hello,{name}")
hello()
hello("Admin")
hello(name="david")
'''
'''
def f(name="User", city="Shymkent", age="17"):
    print(f"My {name}, I from {city}. I am {age} years old")
f("David", "Astana", "20")
f(city="Almaty")
'''
'''
def f(a=56, b=345):
    c = a+b
    d = a-b
    h = a*b
    g = a//b
    print(c, d, h, g)
f(b= 10)
'''
'''
def sum(a,b):
    print(a+b)
sum(12, 30, 45)
'''
'''
def f(*args):
    return sum(args)
a= f(1,2,3,4,5)
print(a)
'''
'''
def f(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
f(name= "David", city= "Shymkent", age= 20)'''
'''
def f(*args, **kwargs):
    print(args)
    print(kwargs.values())
f(1,232,42,53,5, name= "daojawpoj")1241222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222''' 
'''
def add(a: int, b: int)->int:
    return a+b
c=add(45,90)
print(c)'''
'''
def f(a: str, b: list)-> str:
    return f"Hello, {a}! you speak {', '.join(b)}"
c = ['russian', 'english', 'kazakh']

print(f("ijgwsij", c)))'''
'''
from typing import Union
def f(value:Union[int,float], key:Union[int,float])->float:
    return value+key
c = f(59, 20.5)
print(c))'''
'''
def f(a: str, b:list)->str:
    return f"Hello, {a}! you speak {', '.join(b)}"
c = ['russian', 'english', 'kazakh']
print(f("ijgwsij", c))'''
'''
square = lambda x:x*x 
print(square(5))))'''
'''
a = [1,23,54,63,64,73,3,1]
b = list(map(lambda x:x*x,a))
print(b)'''
'''
b= [1,321,4214,124,124,124,1]
a = lambda x:x%2==0
c = list(filter(a,b))
print(c)
'''
'''
def calculate_volume(r,h):
    p = 3.14
    return r**2*h*p
c = calculate_volume(20,40)
print(c)
'''
'''
def farewell(name= 'User'):
    print(f"До свидания {name}")
farewell("David")
farewell('dadkap')
farewell("afojfa")
'''
'''
def circle_circumference(r):
    p = 3.14
    return 2*p*r
print(circle_circumference(4))
print(circle_circumference(6))
'''
'''
def list_max(a: list)->int:
    return max(a)
c = [1,321,41,421,4,214,24,1,421,41]
print(list_max(c))'''
'''
def rectangle_area(a,b):
    return (a+b)*2
print(rectangle_area(5,8))'''
'''
def f(a:int, b=0, c=1):
    if b<a or b>a:
        b += c
        print(b)
        f(a,b,c)
f(-10,0,-1)
'''
'''
def f(a: str, b:int):
    for i in range(b+1):
        print(a)
print(f('dapdowapodkap', 5))
'''
'''
def f(a:int, b:int, c:int):
    d = b**2 - 4*a*c
    if d >0:
        print(-b+d**0.5/2*a)
        print(-b-d**0.5/2*a)
    elif d==0:
        print(-b+d**0.5/2*a)
    elif d<0:
        pass
f(4,22,2)
'''
'''
def f(a:int, b:int):
    return a-(a*b/100)

print(f(20, 15))
'''
'''
def f(a: list):
    return a[0]
print(f([31,4,24,154,12,12,412,412,4,214,21,41,2]))'''

'''
def i():
    a = "dwaopkdawo"
    return a
def j():
    n = i()
    return n
print(j())
'''
'''
d = 4801947201
print(d)
def f():
    global d
    d = 1204801297428
f()
print(d)
'''
'''
def f(a: str):
    return f"Hello , {a}"
print(f("David"))'''
'''
def u(a: str, b: str, c: str):
    return f"https://www.google.com/{a}/{b}/{c}.com"
print(u("daywd", "aiwhdao", "duawhdi"))'''
'''
def f(*args):
    g = sum(args)
    return g
print(f(1231,123,123,12,3123,213,1))
def  g (*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(g(11204791284712,2441241,4124,124,12,41,41,24,14,1))'''
''''
a = [123,124,12,421,412,4,12,4,24,124,1,4,124]
def f(a:list):
    return a[int(len(a)/2)]
print(f(a))'''
a = 412
