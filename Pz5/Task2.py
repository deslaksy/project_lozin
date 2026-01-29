#Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг:значение A переходит в C, значение C — в B, значение B — в A (A, B, C —вещественные параметры, являющиеся одновременно входными и выходными). Спомощью этой функции выполнить левый циклический сдвиг для двух данныхнаборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).
def ShiftLeft3(A, B, C):
    temp = A
    A = B
    B = C
    C = temp
    return A, B, C

a1 = float(input("A1: "))
b1 = float(input("B1: "))
c1 = float(input("C1: "))

a2 = float(input("A2: "))
b2 = float(input("B2: "))
c2 = float(input("C2: "))

a1, b1, c1 = ShiftLeft3(a1, b1, c1)
a2, b2, c2 = ShiftLeft3(a2, b2, c2)

print(f"Первый набор: {a1} {b1} {c1}")
print(f"Второй набор: {a2} {b2} {c2}")
