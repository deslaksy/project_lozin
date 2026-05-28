from tkinter import *

root = Tk()
root.title("Registration Details")
root.geometry("380x500")
root.configure(bg="#3a6ea5")

Label(root, text="Registration Details", font=("Arial", 14, "bold"), bg="#3a6ea5", fg="white").pack(pady=10)

frame = Frame(root, bg="white")
frame.pack(fill="both", expand=True, padx=20, pady=10)

Label(frame, text="University:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(15,0))
Entry(frame, font=("Arial", 10), relief="solid", bd=1).pack(fill="x", padx=15, pady=(0,5))

Label(frame, text="Institute:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(5,0))
Entry(frame, font=("Arial", 10), relief="solid", bd=1).pack(fill="x", padx=15, pady=(0,5))

Label(frame, text="Branch:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(5,0))
Entry(frame, font=("Arial", 10), relief="solid", bd=1).pack(fill="x", padx=15, pady=(0,5))

Label(frame, text="Degree:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(5,0))
Entry(frame, font=("Arial", 10), relief="solid", bd=1).pack(fill="x", padx=15, pady=(0,5))

f_radio = Frame(frame, bg="white")
f_radio.pack(fill="x", padx=15, pady=5)
var = StringVar(value="Pursuing")
Radiobutton(f_radio, text="Pursuing", variable=var, value="Pursuing", bg="white").pack(side=LEFT, padx=5)
Radiobutton(f_radio, text="Completed", variable=var, value="Completed", bg="white").pack(side=LEFT, padx=5)

Label(frame, text="Average CPI:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(5,0))
f_cpi = Frame(frame, bg="white")
f_cpi.pack(fill="x", padx=15, pady=5)
Entry(f_cpi, width=15, relief="solid", bd=1).pack(side=LEFT)
Label(f_cpi, text="Upto", bg="white").pack(side=LEFT, padx=5)
Entry(f_cpi, width=10, relief="solid", bd=1).pack(side=LEFT)
Label(f_cpi, text="Th Semester", bg="white").pack(side=LEFT, padx=5)

Label(frame, text="Experience:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(5,0))
f_exp = Frame(frame, bg="white")
f_exp.pack(fill="x", padx=15, pady=5)
Entry(f_exp, width=15, relief="solid", bd=1).pack(side=LEFT)
Label(f_exp, text="Years", bg="white").pack(side=LEFT, padx=5)

Label(frame, text="Your Website Or Blog:", bg="white", font=("Arial", 10)).pack(anchor="w", padx=15, pady=(5,0))
Entry(frame, relief="solid", bd=1).pack(fill="x", padx=15, pady=5)

Button(frame, text="SAVE", bg="#3a6ea5", fg="white", font=("Arial", 10, "bold"), relief="flat").pack(pady=20)

root.mainloop()
