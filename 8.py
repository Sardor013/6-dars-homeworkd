def qoshib_ketish(list1, list2):
    natija = [satr + str(son) for satr, son in zip(list2, list1)]
    return natija


list1 = [1, 4, 3, 9]
list2 = ['chelsea', 'real', 'barca', 'MU']

natija = qoshib_ketish(list1, list2)
print(natija)
