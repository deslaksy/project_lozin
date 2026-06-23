# Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
# Напишите метод, который выводит информацию о машине в формате "Марка: марка, Модель: модель, Год выпуска: год".

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")


if __name__ == "__main__":
    # Добавлено 5 вариантов машин
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Lada", "Vesta", 2023)
    car3 = Car("BMW", "M5", 2021)
    car4 = Car("Kia", "Rio", 2019)
    car5 = Car("Hyundai", "Solaris", 2022)

    car1.show_info()
    car2.show_info()
    car3.show_info()
    car4.show_info()
    car5.show_info()
