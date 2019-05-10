'''a1 = [8, 19, 148, 4]
a2 = [9, 1, 33, 83]
a3 = []
for i in a1:
    a = i
    for j in a2:
        a *= j
    a3.append(a)
print(a3)
'''
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)
