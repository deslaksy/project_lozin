#Средствами языка Python сформировать текстовый файл (.txt), содержащий  последовательность из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую  обработку элементов:
numbers = [3, -5, 7, -2, 9, -8, 4]  
with open('input.txt', 'w') as file:
    for num in numbers:
        file.write(f"{num} ")
with open('input.txt', 'r') as file:
    data = file.read().split()
    numbers = [int(x) for x in data]
count = len(numbers) 
min_value = min(numbers)  
min_index = numbers.index(min_value) 
processed_numbers = [num * min_value for num in numbers]
with open('output.txt', 'w') as file:
    file.write("Исходные данные:\n")
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Индекс первого минимального элемента: {min_index}\n")
    file.write("Умножаем все элементы на минимальный элемент:\n")
    file.write(' '.join(map(str, processed_numbers)))
