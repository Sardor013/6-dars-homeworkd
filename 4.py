def find_int(list):

    count = 0

    for i in list:
        if isinstance(i, int):
            count += 1

    return count

list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
natija = find_int(list)
print(natija)
