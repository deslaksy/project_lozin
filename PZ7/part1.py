s = input("Введите строку:")
count = 0
for c in s:
    if 'A' <= c <= 'Z':
        count += 1
        print("Количество заглавных латинских букв",count)
