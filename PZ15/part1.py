# Практическое занятие № 15. Вариант 14
# Приложение ТОРГОВАЯ ФИРМА
# Таблица: Продажа товаров (Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер)
import sqlite3

conn = sqlite3.connect('trading_firm.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_date TEXT,
        product TEXT,
        amount REAL,
        discount REAL,
        branch TEXT,
        manager TEXT
    )
''')

records = [
    ('2025-05-12', 'Ноутбук', 45000, 5, 'ТЦ РосМаш', 'Иванов'),
    ('2025-05-13', 'Мышь', 1500, 0, 'ТЦ РосМаш', 'Петрова'),
    ('2025-05-14', 'Клавиатура', 2500, 10, 'ТЦ Миртехники', 'Сидоров'),
    ('2025-05-15', 'Монитор', 18000, 15, 'ТЦ Западный', 'Иванов'),
    ('2025-05-16', 'Ноутбук', 52000, 5, 'ТЦ РосМаш', 'Козлова'),
    ('2025-05-17', 'Флешка', 800, 0, 'ТЦ Миртехники', 'Петрова'),
    ('2025-05-18', 'Диск', 5000, 10, 'ТЦ Западный', 'Сидоров'),
    ('2025-05-19', 'Наушники', 3000, 5, 'ТЦ РосМаш', 'Иванов'),
    ('2025-05-20', 'Принтер', 12000, 20, 'ТЦ Миртехники', 'Козлова'),
    ('2025-05-21', 'Сканер', 8000, 0, 'ТЦ Западный', 'Петрова'),
]

cur.executemany('INSERT INTO sales VALUES (?,?,?,?,?,?)', records)
conn.commit()

print("Поиск :")
print("1. Продажи менеджера Иванова:")
cur.execute("SELECT * FROM sales WHERE manager = 'Иванов'")
for row in cur.fetchall():
    print(row)

print("\n2. Продажи в ТЦ РосМаш с суммой больше 10000:")
cur.execute("SELECT * FROM sales WHERE branch = 'ТЦ РосМаш' AND amount > 10000")
for row in cur.fetchall():
    print(row)

print("\n3. Продажи с 16.05 по 21.05:")
cur.execute("SELECT * FROM sales WHERE sale_date BETWEEN '2025-05-16' AND '2025-05-21'")
for row in cur.fetchall():
    print(row)

print("\nУдаление:")
cur.execute("DELETE FROM sales WHERE amount < 1000")
print("1. Удалены продажи с суммой < 1000")

cur.execute("DELETE FROM sales WHERE product = 'Мышь'")
print("2. Удалены продажи товара 'Мышь'")

cur.execute("DELETE FROM sales WHERE discount > 10")
print("3. Удалены продажи со скидкой > 10%")
conn.commit()

print("\nРедактирование:")
cur.execute("UPDATE sales SET amount = amount * 1.1 WHERE product = 'Ноутбук'")
print("1. Сумма для ноутбуков увеличена на 10%")

cur.execute("UPDATE sales SET discount = 15 WHERE branch = 'ТЦ РосМаш'")
print("2. Скидка для ТЦ РосМаш изменена на 15%")

cur.execute("UPDATE sales SET manager = 'Смирнов' WHERE amount > 20000")
print("3. Менеджер Смирнов назначен на продажи с суммой > 20000")
conn.commit()

print("\nИтоговая таблица:")
cur.execute("SELECT * FROM sales")
for row in cur.fetchall():
    print(row)

conn.close()
