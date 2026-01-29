#Дано вещественное число A и целое число N (>0). Используя один цикл, вывести всецелые степени числа A от 1 до N.
a = input("Введите A: ")
b = input("Введите B: ")

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите A: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите B: ")

i = 1
while i <= b:
    print(a ** i)
    i += 1
