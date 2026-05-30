#1. В соответствии с номером варианта перейти по ссылке на прототип. Реализоватьего в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимальноприближенный к оригиналу
from tkinter import *

root = Tk()
root.title("Registration Details")
root.geometry("400x550")
root.configure(bg="lightblue")

Label(root, text="Registration Details", font=("Arial", 16, "bold"), bg="lightblue", fg="white").pack(pady=(20,10))

frame = Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True, padx=30)

Label(frame, text="University:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
Entry(frame, font=("Arial", 11), relief="solid", bd=1).pack(fill="x", pady=(0,5))

Label(frame, text="Institute:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
Entry(frame, font=("Arial", 11), relief="solid", bd=1).pack(fill="x", pady=(0,5))

Label(frame, text="Branch:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
Entry(frame, font=("Arial", 11), relief="solid", bd=1).pack(fill="x", pady=(0,5))

Label(frame, text="Degree:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
Entry(frame, font=("Arial", 11), relief="solid", bd=1).pack(fill="x", pady=(0,5))

f_radio = Frame(frame, bg="lightblue")
f_radio.pack(fill="x", pady=5)
var = StringVar(value="Pursuing")
Radiobutton(f_radio, text="Pursuing", variable=var, value="Pursuing", bg="lightblue", fg="white", selectcolor="lightblue").pack(side=LEFT, padx=5)
Radiobutton(f_radio, text="Completed", variable=var, value="Completed", bg="lightblue", fg="white", selectcolor="lightblue").pack(side=LEFT, padx=5)

Label(frame, text="Average CPI:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
f_cpi = Frame(frame, bg="lightblue")
f_cpi.pack(fill="x", pady=5)
Entry(f_cpi, width=15, relief="solid", bd=1).pack(side=LEFT)
Label(f_cpi, text="Upto", bg="lightblue", fg="white").pack(side=LEFT, padx=5)
Entry(f_cpi, width=10, relief="solid", bd=1).pack(side=LEFT)
Label(f_cpi, text="Th Semester", bg="lightblue", fg="white").pack(side=LEFT, padx=5)

Label(frame, text="Experience:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
f_exp = Frame(frame, bg="lightblue")
f_exp.pack(fill="x", pady=5)
Entry(f_exp, width=15, relief="solid", bd=1).pack(side=LEFT)
Label(f_exp, text="Years", bg="lightblue", fg="white").pack(side=LEFT, padx=5)

Label(frame, text="Your Website Or Blog:", font=("Arial", 11), bg="lightblue", fg="white", anchor="w").pack(fill="x", pady=(5,0))
Entry(frame, relief="solid", bd=1).pack(fill="x", pady=5)

Button(frame, text="SAVE", bg="white", fg="lightblue", font=("Arial", 10, "bold"), relief="flat").pack(pady=20)

Label(root, text="Step 2", font=("Arial", 12, "bold"), fg="white", bg="lightblue").pack(pady=(0,20))

root.mainloop()
