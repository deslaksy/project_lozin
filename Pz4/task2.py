n = input("Введите N: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите N: ")

k = 1
while k * k <= n:
    k += 1
print('K =', k)
