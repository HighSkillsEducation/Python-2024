
"""" 
a = int(input("ввидите число: "))
if a == 5:
    print("отлично")
elif a == 4:
    print("хорошо")
elif a == 3:
    print("Удовлетворительно")
else :
    print("старайся лучше")
""" 
"""
a = int(input("радиус круга"))
S = 3.14 * a**2
print(S)
"""
"""
a = int(input("ввидите число"))
if a < 0:
    print("число отрецательное")
else :
    print("число положительное")
    """
"""
a = input("ввидите имя")
print(f"привет,{a}")
"""
"""
a = int(input("ввидите число"))
v = int(input("ввидите число"))
print(a+v)
print(a*v)
print(a/v)
print(a-v)
"""
"""
a =[6287648236482,12,10,15,14,18]
print(a[0])
a[0] = 34
print(a)
a.append(45)
print(a)
a.extend([5,6,7,8,9])
print(a)
a.insert(2,24)
print(a)
"""
"""
a =["java","youtube","instagram","tiktok"]
a.append("python")
print(a)
"""
"""
a =["apple","banana","cherry"]
a.remove("banana")
print(a)
"""
"""
a =[2,3,7,5,6,7,8,9]
if 10 in a:
    print("число 10 есть в списке")
    """
"""
a = [1,2,3,4,5,6]
if len(a) > 3:
    a.pop()
    print(a)
    """
"""
a = ["bagi", "aava", "Sasha"]
if len(a[0]) > len(a[1]):
    a.sort()
print(a)
"""
"""
a = []
if a == []:
    a.append(1)
else:
    print("список пуст")
print(a)
"""
"""
a = [
    [1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16]
]
for i in a:
    for s in i:
        print(s)
    print()
    """
"""
a = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
for i in a:
    sum = 0
    for w in i:
        sum+=w
    print(sum)
    """
"""
a = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
for i in a:
    for w in i:
        if w%2==0:
            print(w)
        """
"""
a = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
for i in a:
    print(max(i))
        """
"""
a = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
for i in a:
    for w in i:
        if w > 5:
            print(w)
else:
 print()
 """
"""
a = [
     [1,2,3,4,5],
     [6,7,8,9,10]
 ]
for i in a:
    multiply = 1
    for w in i:
         multiply*=w
    print(multiply)
        """
"""
a = [
    ["asagi","weyne","laura"],
    ["asagi","python","weyne","laura"]
]
for i in a:
    if "python" in i:
        print(True)
else:
    print(False)
        """
"""
a = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
for i in a:
    for w in i:
        if w > 5:
            print(w)
   """
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
"""
a = [
     [1,2,3,4,5],
     [6,7,8,9,10]
 ]
for i in a:
    multiply = 1
    for w in i:
         multiply*=w
    print(multiply)
    """
"""
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in a:
    for r in i:
    """
"""
a = [
    [1,2,3],
    [4,5,6]
]
for i in a:
    for v in i:
        print(i.index(v))
    """
"""
a = [
    [-1,2,-3,4],
    [5,-6,7,-8]
]
q = []
for i in a:
    q.append([])
    ind = a.index(i)
    for c in i:
        if c < 0:
            c-=c
        q[ind].append(c)
print(q)
    """
"""
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
row = len(a)
cols = len(a[0])
for i in  range(cols):
    new_row = []
    for j in range(row):
        new_row.append(a[j][i])
    print(new_row)
    """
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s = matrix[0][0] + matrix[1][1] + matrix[2][2]
print(s)
    """
"""
a = [
    [1,115,3,4],
    [5,6,7,8]
]
for i in a:
    for j in i:
        s = i.index(j)
        if s %2 >= 1:
            print(j)
    """
"""
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
q = []
for i in a:
    q.append([])
    k = a.index(i)
    for j in i:
        j = j**2
        q[k].append(j)
print(q)
    """
"""
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in a:
    s = sum(i) // len(i)
    print(s)
    """
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s = matrix[0][0] + matrix[1][1] + matrix[2][2]
print(s)
"""
"""
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b = []
for i in a:
    print(min(i))    
     """
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = []
for i in matrix:
    a.append([])
    index = matrix.index(i)
    for j in i:
        if i.index(j)>0:
            a[index].append(j)
print(a)
"""
"""
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a & b)
    """
"""
a = {1,2,3,4,5,6,7,8,9,10}
d = {}
for i in a:
    if i%2==0:
        print(i)
"""
"""
a = {1,2,3,4,5}
b = {6,7,8,9}
print (a | b)
    """
"""
a = {2,4,6,8}
b = {1,3,5,7}
print( a | b)
    """
"""
a = {1,2,3,4}
b = {1,2,5,6,7,8}
print(a & b)
    """
"""
a = [1,1,2,2,3,3,4,5]
a = set(a)
a.clear()
print(a)
    """
"""
a = {1,2,3,4,5}
b = {1,2,3,4,5,6,7,8}
print(a ^ b)
    """
"""
a = {1,2,3,4,5}
if not a:
    print("true")
else:
    print("false")
    """
"""
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = {5,6,7,8,9}
print(a & b & c)
    """
"""
import random
a = random.randint(1,10)
b = {1,2,3,4,5,6,7,8,9,10}
b.remove(a)
print(a)
"""
"""
a = [1,1,2,3,4,5]
a = set(a)
print(a)
    """
"""
a = input()
b = {"Sagi","Biali","Dimash"}
if a in b:
    b.remove(a)
print(b)
"""
"""a = {1,2,3,4,5}
b = {1.5,2.1,4.5}
print(a | b)
"""
"""
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a & b)
"""
"""a  = (12,14,16,17,14)
print(len(a))"""
"""a = (1,2,4,5,6)
print(min(a))"""
a = (1,2,3,4,56)
a = list(a)
a.pop(-1)
a = tuple(a)
print(a)
