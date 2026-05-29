import re

# Читаем исходный файл
with open("hotline1.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Задание 1: ищем номера 8(000)000-00-00
phones = re.findall(r"8\(\d{3}\)\d{3}-\d{2}-\d{2}", text)

print("=" * 50)
print("Задание 1. Поиск номеров телефонов")
print("=" * 50)
print(f"Найдено номеров: {len(phones)}")
print("Номера:")
for p in phones:
    print(f"  {p}")

# Задание 2: добавляем фразу и создаём новый файл
new_text = re.sub(r"(Горячая линия)", r"\1 Министерства образования Ростовской области", text)

with open("hotline1_new.txt", "w", encoding="utf-8") as f:
    f.write(new_text)

print("\n" + "=" * 50)
print("Задание 2. Создан файл hotline1_new.txt")
print("=" * 50)
