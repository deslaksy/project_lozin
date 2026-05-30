#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 1 – 9.
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Числа от A до B")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

Label(root, text="Числа от A до B", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333").pack(pady=15)

frame = Frame(root, bg="white", relief="solid", bd=1)
frame.pack(fill="both", expand=True, padx=20, pady=10)

Label(frame, text="A:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(15,0))
entry_a = Entry(frame, font=("Arial", 10), relief="solid", bd=1)
entry_a.pack(fill="x", padx=15, pady=(0,10))

Label(frame, text="B:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15)
entry_b = Entry(frame, font=("Arial", 10), relief="solid", bd=1)
entry_b.pack(fill="x", padx=15, pady=(0,5))

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        if a >= b:
            messagebox.showwarning("Ошибка", "A < B")
            return
        nums = list(range(a, b + 1))
        label_result.config(text=f"Числа: {nums}\n\nN = {len(nums)}")
    except:
        messagebox.showerror("Ошибка", "Введите целые числа")

Button(frame, text="Вывести", bg="#4CAF50", fg="white", font=("Arial", 10), command=calculate).pack(pady=20)

label_result = Label(frame, text="Результат", bg="white", font=("Arial", 10))
label_result.pack(anchor="w", padx=15, pady=10)

root.mainloop()
