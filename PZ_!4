import tkinter as tk

root = tk.Tk()
root.title("Step 3 / External Details")

# Четкие размеры: горизонталь 450, вертикаль 550
root.geometry("450x550")
root.configure(bg="#3a70a4")

# Главная рамка с контуром
box = tk.LabelFrame(
    root, text=" Registration Details ", fg="white", bg="#3a70a4"
)
box.pack(padx=15, pady=10, fill="both", expand=True)


# Короткая функция для создания подписей сверху полей
def add_lbl(txt):
    tk.Label(box, text=txt, font=("Arial", 10), fg="white", bg="#3a70a4").pack(
        anchor="w", padx=25, pady=(6, 2)
    )


# 1. University
add_lbl("University :")
e1 = tk.Entry(box, width=48, bd=0)
e1.pack(anchor="w", padx=25, ipady=2)

# 2. Institute
add_lbl("Institute :")
e2 = tk.Entry(box, width=48, bd=0)
e2.pack(anchor="w", padx=25, ipady=2)

# 3. Branch
add_lbl("Branch :")
v1 = tk.StringVar(value="-- select --")
tk.OptionMenu(box, v1, "-- select --", "1", "2", "3").pack(
    anchor="w", padx=25
)

# 4. Degree & Radiobuttons
add_lbl("Degree :")
v2 = tk.StringVar(value="-- select --")
tk.OptionMenu(box, v2, "-- select --", "1", "2", "3").pack(
    anchor="w", padx=25
)

f_rb = tk.Frame(box, bg="#3a70a4")
f_rb.pack(anchor="w", padx=25, pady=4)
vr = tk.StringVar(value="Pursuing")
tk.Radiobutton(
    f_rb, text="Pursuing", variable=vr, value="Pursuing", fg="white", bg="#3a70a4"
).pack(side="left")
tk.Radiobutton(
    f_rb,
    text="Completed",
    variable=vr,
    value="Completed",
    fg="white",
    bg="#3a70a4",
    selectcolor="#3a70a4",
).pack(side="left", padx=10)

# 5. Average CPI
add_lbl("Avarage CPI :")
f_cpi = tk.Frame(box, bg="#3a70a4")
f_cpi.pack(anchor="w", padx=25)
tk.Spinbox(f_cpi, from_=0, to=10, width=5, bd=0).pack(side="left", ipady=2)
tk.Label(f_cpi, text="Upto", fg="white", bg="#3a70a4").pack(
    side="left", padx=5
)
spin_sem = tk.Spinbox(f_cpi, from_=1, to=8, width=5, bd=0)
spin_sem.pack(side="left", ipady=2)
tk.Label(f_cpi, text="Th Sem", fg="white", bg="#3a70a4").pack(
    side="left", padx=5
)

# 6. Experience
add_lbl("Experience :")
f_exp = tk.Frame(box, bg="#3a70a4")
f_exp.pack(anchor="w", padx=25)
tk.Spinbox(f_exp, from_=0, to=30, width=5, bd=0).pack(side="left", ipady=2)
tk.Label(f_exp, text="Years", fg="white", bg="#3a70a4").pack(
    side="left", padx=5
)

# 7. Your Website Or Blog
add_lbl("Your Website Or Blog :")
e3 = tk.Entry(box, width=48, bd=0)
e3.insert(0, "http://")
e3.pack(anchor="w", padx=25, ipady=2)

# Навигация в самом низу окна
nav = tk.Frame(root, bg="#3a70a4")
nav.pack(pady=10)

tk.Button(nav, text="◀", fg="white", bg="#7ca82b", bd=0, width=4).pack(
    side="left", padx=5
)
tk.Label(nav, text="Step 2", fg="white", bg="#3a70a4").pack(side="left", padx=10)
tk.Button(nav, text="▶", fg="white", bg="#7ca82b", bd=0, width=4).pack(
    side="left", padx=5
)

root.mainloop()
