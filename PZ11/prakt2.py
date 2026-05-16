#2. Составить генератор (yield), который выводит из строки только цифры.
def digits_gen(s):
    for ch in s:
        if ch.isdigit():
            yield ch
text = input('Введите строку:')
print ('Цифры', ''.join(digits_gen(text)))
