# Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
# унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
# вычисления площади и периметра.

class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Круг")
        self.radius = radius

    def get_area(self):
        return 3.14159 * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14159 * self.radius

if __name__ == "__main__":
    # Добавлены возможные варианты
    c1 = Circle("Красный", 5)
    c2 = Circle("Синий", 10)
    c3 = Circle("Зеленый", 3.5)

    print(f"Фигура: {c1.shape_type}, Цвет: {c1.color}, Радиус: {c1.radius}, Площадь: {round(c1.get_area(), 2)}, Периметр: {round(c1.get_perimeter(), 2)}")
    print(f"Фигура: {c2.shape_type}, Цвет: {c2.color}, Радиус: {c2.radius}, Площадь: {round(c2.get_area(), 2)}, Периметр: {round(c2.get_perimeter(), 2)}")
    print(f"Фигура: {c3.shape_type}, Цвет: {c3.color}, Радиус: {c3.radius}, Площадь: {round(c3.get_area(), 2)}, Периметр: {round(c3.get_perimeter(), 2)}")
