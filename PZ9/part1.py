#в каких магазинах можно одновременно нельзя приобрести книги Достоевского и Пушкина.
magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
Domknigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BookMarket = {"Пушкин", "Достоевский", "Маяковский"}
galereya = {"Чехов", "Тютчев", "Пушкин"}
authors = {"Достоевский", "Пушкин"}
if magistr&authors == authors:
    print ("Магистр")
if Domknigi&authors == authors:
      print("ДомКниги")
if BookMarket&authors == authors:
      print("БукМаркет")
if galereya&authors == authors:
      print("Галерея")
