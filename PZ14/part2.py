# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 1 – 9.
import tkinter as tk

root = tk.Tk()
root.geometry("450x400")
root.configure(bg="white")


# Функция горизонтальной линии
def hor(sym, n):
    return sym * n


# Функция вертикальной линии
def ver(sym):
    return sym


# Функция сборки рамки
def run():
    w = e1.get()
    s = e2.get()

    n = len(w) + 4
    line = hor(s, n)
    v = ver(s)

    res = f"{line}\n{v} {w} {v}\n{line}"
    lbl_res.config(text=res)


# Окно ввода данных
box = tk.LabelFrame(root, text=" Создание рамки из линий ", bg="white")
box.pack(padx=20, pady=20, fill="both", expand=True)

tk.Label(box, text="Введите слово:", bg="white").pack(
    anchor="w", padx=25, pady=5
)
e1 = tk.Entry(box, width=40, bd=1)
e1.pack(anchor="w", padx=25, ipady=2)

tk.Label(box, text="Введите символ для печати линий:", bg="white").pack(
    anchor="w", padx=25, pady=5
)
e2 = tk.Entry(box, width=10, bd=1)
e2.pack(anchor="w", padx=25, ipady=2)

tk.Button(
    box, text="Построить рамку", fg="white", bg="#7ca82b", bd=0, command=run
).pack(anchor="w", padx=25, pady=15, ipady=3)

# Вывод результата черным текстом
lbl_res = tk.Label(
    box, font=("Courier New", 12, "bold"), fg="black", bg="white"
)
lbl_res.pack(anchor="w", padx=25, pady=10)

root.mainloop()
