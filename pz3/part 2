def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

a = safe_input("Число A: ")
b = safe_input("Число B: ")
c = safe_input("Число C: ")

print(sorted([a, b, c])[1])
