#С помощью функций получить вертикальную и горизонтальную линии. Линияп роводится многократной печатью символа. Заключить слово в рамку изполученных линий.
def gorizontal(n, sim):
    print(sim * n)
def ramka(slovo, sim):
    dlina = len(slovo) + 4
    gorizontal(dlina, sim)
    print(f"{sim} {slovo} {sim}")
    gorizontal(dlina, sim)
slovo = input("Слово: ")
sim = input("Символ рамки: ")
ramka(slovo, sim)
