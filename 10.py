def fibonacci(n):
    a = [0, 1]
    for i in range(2, n):
        b = a[-1] + a[-2]
        a.append(b)
    return a

n = int(input(" "))

fib_numbers = fibonacci(n)
print("fib sonlar:", fib_numbers)
