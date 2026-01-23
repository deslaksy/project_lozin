try:
s = input("Введите строку:")
if not s:
else:
count = 0
for c in s:
    if 'A' <= c <= 'Z':
        count += 1
        print("Количество заглавных латинских букв",count)
except exception as e:
print("Error")
