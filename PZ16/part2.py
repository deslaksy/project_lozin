import math

class Form:
    def __init__(self, color):
        self.color = color

class Circle(Form):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def info(self):
        print(f"Круг цвета {self.color}, радиус = {self.radius}")
        print(f"  Площадь: {self.area():.2f}")
        print(f"  Длина окружности: {self.perimeter():.2f}")

# Тестовые запуски
print("Тестирование CIRCLE")
circle1 = Circle("Красный", 4)
circle2 = Circle("Синий", 7)
circle3 = Circle("Зеленый", 2.5)
circle4 = Circle("Желтый", 10)

print("\n")
circle1.info()
print()
circle2.info()
print()
circle3.info()
print()
circle4.info()
