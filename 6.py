def qoshish(list):
    son = int(''.join(map(str, list))) + 1
    return [int(x) for x in str(son)]

list1 = [1, 2, 3]
list2 = [9]
list3 = [9, 9, 9, 9]

print(qoshish(list1))
print(qoshish(list2))
print(qoshish(list3))
