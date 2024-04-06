def eng_katta_yigindisi(list):
    eng_katta_yig = max(list, key=sum)
    return eng_katta_yig

list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
natija = eng_katta_yigindisi(list)
print(natija)
