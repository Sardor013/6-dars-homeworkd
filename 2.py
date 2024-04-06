def strr(list, satr):
    return [satr + str(element) for element in list]


list1 = [1, 4, 3, 9]
satr = input("satrni kiriting: ")

natija = strr(list1, satr)
print(natija)
