spaces = 0

# вывод и подсчет пробелов
for line in open('text18-14.txt', encoding='UTF-8'):
    print(line, end='')
    for ch in line:
        if ch == ' ':
            spaces += 1

print('\nКоличество пробелов:', spaces)

# читаем строки
f1 = open('text18-14.txt', encoding='UTF-8')
l = f1.readlines()
f1.close()

# заменяем 3 строку на коды
if len(l) >= 3:
    new_line = ''
    for ch in l[2]:
        new_line += str(ord(ch)) + ' '
    l[2] = new_line + '\n'

# запись
f2 = open('result.txt', 'w')
f2.writelines(l)
f2.close()
