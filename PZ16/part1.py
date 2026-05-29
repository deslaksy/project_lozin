class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}")

# Тестовые запуски
print("Тестирование CAR")
car1 = Car("Audi", "A6", 2019)
car2 = Car("Mercedes", "E220", 2021)
car3 = Car("Hyundai", "Solaris", 2022)
car4 = Car("Kia", "Rio", 2020)
car5 = Car("Nissan", "Qashqai", 2023)

print("\nИнформация о машинах:")
car1.info()
car2.info()
car3.info()
car4.info()
car5.info()
