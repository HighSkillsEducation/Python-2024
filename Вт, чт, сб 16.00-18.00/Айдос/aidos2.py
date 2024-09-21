'''
a = 'hello world'
b = []
for i in a:
    b.append(i)
print(b)

c = []
c.append(a)
print(c)

d = list(a)
print(d)
'''

'''
a = [1,2,2,3,4,4]
d = a
print(d)
b = []
for i in a:
    c = a.count(i)
    if c > 1:
        a.remove(i)
b = a
print(b)
'''

'''
a = [1,2,3,'a','b', '11']
b = 0
c = ''
for i in a:
    if str(i).isdigit():
        b = b + int(i)
    else:
        c += i
print(b)
print(c)
'''

'''
a = [1,2,3,5,17,11]
b = 0
for i in a:
    if b < i:
        b = i
print(b)
'''

'''
a = ['apple','strawberry', 'cherry']
b = []
for i in a:
    c = a.index(i)
    print(f'fruit: {i}, index {c}, length {len(a)}')
'''
"""
a = [1,3,4,2]
b = [1,2,3]
c = a + b
for i in c:
    d = c.count(i)
    if d > 1:
        c.remove(i)
print(c)"""

'''
a = [1,3,4,2]
b = [1,5,2,3]
for i in b:
    if i in a:
        b.remove(i)
    print(b)
c = a + b
print(c)
'''

'''
a = int(input())
n = 1
for i in range(10):
    print(f'{a} x {n} =', a*n)
    n += 1
'''

'''
a = int(input('Введите высоту треугольника = '))

for i in range(a):
    print(a*'*')
    a -= 1
'''

'''
a = input()
c = 0
v = 'auioe'
for i in a.lower():
    if i in v:
        c += 1        

print(f'Количество гласных: {c}')
'''
'''
a = list(range(1,101))
for i in a:
    if i > 1:
        c = True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                c = False
                break
        if c:
            print(i)        
'''

'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''

'''
import random
b = int(input())
v = int(input())
d = 1
x = 100
o = 0
k = []
matrix = [[random.randint(d,x) for _ in range(b)] for _ in range(v)]
print(matrix)
for i in matrix:
    for j in i:
        k.append(j)
print(k)
for l in k:
    o += l
print(o)
print(matrix[0][0])
print(matrix[1][1])
'''

'''
# A
n = int(input())
for i in range(2,n+1):
    for j in range(2,i+1):
        print(j,end=' ')
    print()

'''

'''
# B
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''

'''
# D
n = int(input())
for i in range(0,n+1):
    for j in range(0,i+1):
        print(j,end=' ')
    print()
'''

'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''

'''
a = 5
b = 7
def f(t,r):
    return t+r
print(f(a,b))
'''

'''
a = 100
def f():
    global a
    a = 145
f()
print(a)
'''

'''
def f():
    a = 12
    return a
print(f())
'''

'''
def hello(name = 'Aidos', age = 14, city = 'Shymkent'):
    print(f'hello {name}, age = {age}, {city}')
hello()
'''

'''
def f(a=47,b=21):
    print('Сумма =',a+b)
    print('Разность =',a-b)
    print('Умножение =',a*b)
    print('Деление =',a/b)
f()

# 2

def f(*args):
    return sum(args)
a = f(1,2,3,4,5)
print(a)
'''

'''
def f(**kwargs):
    for key,value in kuargs.items():
         print(f'{key}: {value}')
f(name= 'Aidos', city ='Shymkent', age='14')
'''

'''
def f(*args, **kwargs):
    print(args)
    print(kwargs.values())
f(1,2,3,4,5,6,7,8,9,10,a='123')
'''

'''
def add(a: int, b: int)-> int:
    return a+b
c = add(45,90)
print(c)
'''

'''
def f(a: str, b: list)->str:
    return f'Hello, {a}! you speak {', '.join(b)}'
c = ['russian', 'english', 'deustch']
print(f('dsff', c))
'''

'''
from typing import Union
def f(value:Union[int,float], b:Union[int,float])->float:
    return value+b
c = f(100,14.27)
print(c)
'''

'''
def d(a: str, b: list):
   return print(f'{a},{", ".join(b)}')
d()
'''

'''
b = [1,2,3,4,5,6,7,8,9,10]
a = lambda x:x%2==0
print(b)
c = list(filter(a,b))
print(c)
'''

'''
def calculate_volume(d,c):
    p = 3.14
    return p * (d**2) *c
c = calculate_volume(10,20)
print(c)
'''

'''
def farewell(name='Aidos'):
    print(f'До свидания, {name}')
farewell('a')
farewell('b')
farewell('c')
'''

'''
def circle_circumference(r):
    p = 3.14
    return 2 * p * r
print(circle_circumference(20))
'''

'''
b = [1,2,3,4,5,6,7,8,9,10]
def list_max(a: list)-> int:
    return max(b)
print(list_max(b))
'''

'''
def f(a: int, b = 0, c = 1):
    if b < a or b > a:
        b += c
        print(b)
        f(a,b,c)
f(10, 1, 1)
'''

'''
def rectangle_area(a: int, b: int):
    c = a*b
    return c
print(rectangle_area(5, 15))
'''

'''
def a(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d < 0:
        print(f'Дискриминант = {d}, корней нет')
    elif d > 0:
        print('Дискриминант имеет два корня')
        print(-b+d**0.5/2*a)
        print(-b-d**0.5/2*a)
    elif d == 0:
        print('Дискриминант имеет один корень')
        print(-b+d**0.5/2*a)
print(a(1,4,5))
'''

'''
import random
grades = [['mathematics', 'computing', 'english', 'Kazakh language', 'Physics'],[]]
students = []

while True:
    a = input('Введите имя студента, 0 - остановка программы ')
    if a.isalpha():
        students.append(a)
        grades[1].append([])
    if a == '0':
        break


print(students)
print(grades)
'''

