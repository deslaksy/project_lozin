from random import randint
rows = 4
cols = 5
matrix = [[randint(-20, 20) for j in range(cols)] for i in range(rows)]
print("Исходная матрица:")
for row in matrix:
    print(row)
print("\nЗадание 1:")
for j in range(cols):
    if j % 2 == 0:  # четный номер столбца
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(f"Сумма в столбце {j}: {col_sum}")
if cols >= 2:
    min_value = matrix[0][cols-2]
    for i in range(rows):
        if matrix[i][cols-2] < min_value:
            min_value = matrix[i][cols-2]
    print(f"\nЗадание 2:")
    print(f"Минимальный элемент в предпоследнем столбце ({cols-2}): {min_value}")
else:
    print("В матрице нет предпоследнего столбца")
