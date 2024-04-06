def eng_katta_element(list1, list2):
    eng_katta = max(max(list1), max(list2))
    return eng_katta

# Test qismi
list1 = [1, 4, 3, 9]
list2 = [2, 6, 8, 5]

natija = eng_katta_element(list1, list2)
print(natija)
