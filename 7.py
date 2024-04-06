def kvadrat(n, sonlar):
    kvadratlar = [x**2 for x in sonlar]
    return kvadratlar

n = int(input("Son kiriting "))
sonlar = list(map(int, input(f"{n} ta sonni kirting: ").split()))

natija = kvadrat(n, sonlar)
print(natija)
