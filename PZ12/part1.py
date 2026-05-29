from random import randint

# Создаю матрицу 4x5
rows = 4
cols = 5
matrix = [[randint(-20, 20) for j in range(cols)] for i in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

# Задание 1:
print("\nЗадание 1:")
for j in range(cols):
    if j % 2 == 0:  # четный номер столбца
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(f"Сумма в столбце {j}: {col_sum}")
