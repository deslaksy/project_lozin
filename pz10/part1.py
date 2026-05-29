#Создаём исходный файл с числами
numbers = [3, -5, 7, -2, 9, -8, 4]  
with open('input.txt', 'w') as file:
    for num in numbers:
        file.write(f"{num} ")
# Читаем файл, обрабатываем данные
with open('input.txt', 'r') as file:
    data = file.read().split()
    numbers = [int(x) for x in data]

# Вычисляем требуемые значения
count = len(numbers)  # Количество элементов
min_value = min(numbers)  # Минимальное значение
min_index = numbers.index(min_value)  # Индекс первого минимального элемента

# Умножаем все элементы на минимальный элемент
processed_numbers = [num * min_value for num in numbers]

# Формируем новый файл с результатами
with open('output.txt', 'w') as file:
    file.write("Исходные данные:\n")
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Индекс первого минимального элемента: {min_index}\n")
    file.write("Умножаем все элементы на минимальный элемент:\n")
    file.write(' '.join(map(str, processed_numbers)))
