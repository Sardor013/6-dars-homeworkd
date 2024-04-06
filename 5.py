def kop_takrorlanuvchi(list):
    son = {}

    for i in list:
        if i in son:
            son[i] += 1
        else:
            son[i] = 1

    takrorlanuvchi = max(son, key=son.get)
    takrorlanish_soni = son[takrorlanuvchi]

    return f"{takrorlanuvchi} -> {takrorlanish_soni} marta"


list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

natija = kop_takrorlanuvchi(list)
print(natija)
