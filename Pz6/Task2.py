A = list(map(int, input("Введите элементы списка через пробел: ").split()))
B = [x for x in A if x > 0]
C = [x for x in A if x < 0]
print("Список B (положительные):", len(B), "элементов:", B)
print("Список C (отрицательные):", len(C), "элементов:", C)
