#2. Составить генератор (yield), который выводит из строки только цифры.
def digits_gen(s):
    for ch in s:
        if ch.isdigit():
            yield ch
#Пример
text = "my years of 23"
print('Цифры:',''.join(digits_gen(text)))
