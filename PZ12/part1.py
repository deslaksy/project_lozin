#1. Для каждого столбца матрицы с четным номером найти сумму ее элементов.
from random import randint
rows, cols = 4, 5
matrix = [[randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)
# Сумма в каждом четном столбце
print("\nСуммы в четных столбцах:")
for j in range(0, cols, 2):
    print(f"Столбец {j}: {sum(row[j] for row in matrix)}")
#2. В матрице найти минимальный элемент в предпоследнем столбце.
print(f"\nМинимум в столбце {cols-2}: {min(row[cols-2] for row in matrix)}")
