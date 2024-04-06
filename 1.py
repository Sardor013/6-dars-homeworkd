def arifmetik(lists, uzunlik):
    return lists / uzunlik


def arifmetik_topish(sonlar):


    uzunlik = len(sonlar)
    if uzunlik == 0:
        return None

    lists = sum(sonlar)
    orta_arifmetik = arifmetik(lists, uzunlik)
    return orta_arifmetik

royxat1 = [1, 1, 3, 4, 4, 5, 6, 7]
royxat2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

natija1 = arifmetik_topish(royxat1)
natija2 = arifmetik_topish(royxat2)

print(natija1)
print(natija2)
