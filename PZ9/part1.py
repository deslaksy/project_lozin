#в каких магазинах можно одновременно нельзя приобрести книги Достоевского и Пушкина.
Magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
Domknigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BookMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galereya = {"Чехов", "Тютчев", "Пушкин"}
Authors = {"Достоевский", "Пушкин"}
if Magistr&Authors == Authors:
    print ("Магистр")
if Domknigi&Authors == Authors:
      print("ДомКниги")
if BookMarket&Authors == Authors:
      print("БукМаркет")
if Galereya&Authors == Authors:
      print("Галерея")
