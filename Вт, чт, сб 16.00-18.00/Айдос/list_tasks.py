'''
a = [1,2,3,4,4,5]
max_value = max('nambers')
print('vvyvesti max chislo:', max_value)
'''
'''
a = ['apple', 'banana', 'cherry']
for i in a:
    first_letter = i[0]
    last_letter = i[-1]
    first_index = a.index(i)
    
    print(f"fruct: {i}, index {first_index}, {len(i)}")
    print(f"pervyi bucvu na: {first_letter}, index 0 ")
    print(f"poslednyu bucvu na: {last_letter}, index -1")
'''
'''
list1 = [1,2,3,3,4,5]
list2 = [6,7,8,9,9]
combined_list = list(set(list1+list2))
print("vvyvesti spisoc bez lublirovaniai:", combined_list)

list3 = list1+list2
for i in list3:
    count = list3.count(i)
    if count > 1:
        list3.remove(i)
print(list3)
'''    
'''
a = [1,2,3,4,5,6,7,8,9,10]
b = []
c = []
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
'''

a = ['apple','banana','cherry','apple','apple']
b = input("vvedite vash element:")
"""
while b in a:
    a.remove(b)
print(a)
"""
j = []
for i in a:
    if b != i:
        j.append(i)
a = j        
print(a)