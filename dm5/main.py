from tkinter import *
from random import *
from copy import deepcopy


def generate_binary_vectors(n, m):
    b = [randint(0, 1) for _ in range(n + 1)]
    vectors = []
    b[n] = 0
    while True:
        if b[n] == 0:
            vectors += [deepcopy(b)]
            m = m - 1
            if m == 0:
                r_vectors = []
                for v in vectors:
                    r_vectors.append(v[:n])
                return r_vectors
            else:
                for i in range(n):
                    if b[i] == 1:
                        b[i] = 0
                    else:
                        b[i] = 1
                        break


def solve():
    n = int(n_field.get())
    m = int(m_field.get())
    binary_vectors_list = generate_binary_vectors(n, m)
    binary_vectors_list.sort()
    vectors_listbox.delete(0, END)
    for vector in binary_vectors_list:
        vectors_listbox.insert(END, vector)


root = Tk()
root.title("Лаб 5")
root.geometry("510x380")
root.configure(bg='lightgray')
root.resizable(False, False)

Label(root, text=f"Скоробогатов Ігор\nІО-25 \nМій номер: 28 \nМій варіант: {(2528 % 26) + 1}", font=15).place(x=10,
                                                                                                              y=10)
Label(root, text="Введіть n:", font=15).place(x=10, y=95)
n_field = Entry(width=12, font=('Arial', 15))
n_field.place(x=10, y=125)
Label(root, text="Введіть m:", font=15).place(x=10, y=160)
m_field = Entry(width=12, font=('Arial', 15))
m_field.place(x=10, y=190)

Button(text='Розрахувати', width=11, height=1, command=solve, font=('Arial', 15)).place(x=12, y=225)
vectors_listbox = Listbox(root, width=30, font=('Arial', 15))
vectors_listbox.place(x=150, y=125)
scrollbar = Scrollbar(root)
vectors_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=vectors_listbox.yview)
scrollbar.place(x=485, y=125, height=245)

root.mainloop()