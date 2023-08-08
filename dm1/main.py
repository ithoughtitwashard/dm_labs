import tkinter as tk
from random import sample
from ast import literal_eval
import pickle

A = set()
B = set()
C = set()
U = set()
X = set()
Y = set()
Z = set()
my_Z = set()

result = set()


def make_tab_button(name, command):
    return tk.Button(text=name, bd=0, font=('Arial', 15, 'bold'), bg='#f3f3f4', fg='#14110f', command=command)


def make_gen_button(name):
    return tk.Button(text=name, bd=0, font=('Arial', 15, 'bold'), bg='#f3f3f4', fg='#14110f', command=generate_sets)


def show_info():
    io = 25
    my_number = 28
    my_variant = (my_number + io % 60) % 30 + 1
    return tk.Label(win, text=f"Моя група: ІО-{io} \n Мій номер: {my_number} \n Мій варіант: {my_variant}",
                    font=('Arial', 18, 'bold'), bg='#3a3732', fg='#fefcfb').grid(
        row=1, column=4, sticky='wens', rowspan=16
    )


def make_info_button():
    return tk.Button(text='Відомості', bd=0, font=('Arial', 14, 'bold'), bg='#d6d6d8', fg='#14110f', command=show_info)


def make_lable(some_text, color):
    return tk.Label(win, text=some_text, font=('Arial', 14, 'bold'), bg=color, fg='#fefcfb')


def generate_sets():
    global A, B, C, U
    select = radio_var.get()
    if select == 1:
        A = set(literal_eval(field_1.get()))
        B = set(literal_eval(field_2.get()))
        C = set(literal_eval(field_3.get()))
    elif select == 2:
        A = set(sample((range(0, 10)), int(field_4.get())))
        B = set(sample((range(0, 10)), int(field_5.get())))
        C = set(sample((range(0, 10)), int(field_6.get())))
    U = set(sample(range(int(field_7.get()), int(field_8.get()) + 1), int(field_8.get()) + 1))
    make_lable(f"{A}", '#605a55').grid(row=17, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)
    make_lable(f"{B}", '#605a55').grid(row=19, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)
    make_lable(f"{C}", '#605a55').grid(row=21, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)
    make_lable(f"{U}", '#605a55').grid(row=23, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)


def select_btn():
    select = radio_var.get()
    if select == 1:
        field_1['state'] = tk.NORMAL
        field_2['state'] = tk.NORMAL
        field_3['state'] = tk.NORMAL
        field_4['state'] = tk.DISABLED
        field_5['state'] = tk.DISABLED
        field_6['state'] = tk.DISABLED
    elif select == 2:
        field_1['state'] = tk.DISABLED
        field_2['state'] = tk.DISABLED
        field_3['state'] = tk.DISABLED
        field_4['state'] = tk.NORMAL
        field_5['state'] = tk.NORMAL
        field_6['state'] = tk.NORMAL


def open_window_2():
    global A, B, C, U

    def solve_sets():
        global A, B, C, U, result
        not_a = U - A
        not_c = U - C
        b_and_not_c = B & not_c
        not_a_and_c = not_a & C
        a_and_b = A & B
        result = not_a | B | not_c | b_and_not_c | not_a_and_c | a_and_b
        tk.Label(win_2, text="Розв'язок:", font=('Arial', 14, 'bold'), bg='#c3b4a7',
                 fg='#fefcfb').grid(row=6, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'!A: {not_a}', font=('Arial', 14, 'bold'), bg='#8e8680',
                 fg='#fefcfb').grid(row=7, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'!C: {not_c}', font=('Arial', 14, 'bold'), bg='#706a64',
                 fg='#fefcfb').grid(row=8, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'B & !C: {b_and_not_c}', font=('Arial', 14, 'bold'), bg='#605a55',
                 fg='#fefcfb').grid(row=9, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'!A & C: {not_a_and_c}', font=('Arial', 14, 'bold'), bg='#524e49',
                 fg='#fefcfb').grid(row=10, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'A & B: {a_and_b}', font=('Arial', 14, 'bold'), bg='#43403b',
                 fg='#fefcfb').grid(row=11, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'Відповідь D:', font=('Arial', 14, 'bold'), bg='#3c3934',
                 fg='#fefcfb').grid(row=12, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_2, text=f'{result}', font=('Arial', 14, 'bold'), bg='#34312d',
                 fg='#fefcfb').grid(row=13, column=0, sticky='wens', padx=1, pady=1, columnspan=2)

    def save_to_file():
        global result
        res = open('res.txt', 'wb')
        pickle.dump(result, res)
        res.close()

    win_2 = tk.Toplevel()
    win_2.geometry('500x430+1500+300')
    win_2.title('Вкладка 2')
    win_2.config(bg='#000000')
    win_2.resizable(False, False)
    tk.Label(win_2, text='Множина D:', font=('Arial', 14, 'bold'), bg='#34312d',
             fg='#fefcfb').grid(row=0, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_2, text='!A | B | !C | (B & !C) | (!A & C) | (A & B)', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=1, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_2, text=f'Множина A: {A}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=2, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_2, text=f'Множина B: {B}', font=('Arial', 14, 'bold'), bg='#706a64',
             fg='#fefcfb').grid(row=3, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_2, text=f'Множина C: {C}', font=('Arial', 14, 'bold'), bg='#605a55',
             fg='#fefcfb').grid(row=4, column=0, sticky='wens', padx=1, pady=1, columnspan=2)

    tk.Button(win_2, text='Обчислити', bd=0, font=('Arial', 15, 'bold'), bg='#f3f3f4', fg='#14110f', command=solve_sets).grid(
        row=5,
        column=0,
        sticky='wens',
        padx=1,
        pady=1)
    tk.Button(win_2, text='Зберегти до файлу', bd=0, font=('Arial', 15, 'bold'), bg='#f3f3f4', fg='#14110f',
              command=save_to_file).grid(
        row=5,
        column=1,
        sticky='wens',
        padx=1,
        pady=1)

    win_2.grid_columnconfigure(0, minsize=250)
    win_2.grid_columnconfigure(1, minsize=250)


def open_window_3():
    global A, B, C, U

    def solve_sets():
        global A, B, C, U, result
        not_a = U - A
        not_c = U - C
        result = not_a | B | not_c
        tk.Label(win_3, text="Розв'язок спрощенної множини:", font=('Arial', 14, 'bold'), bg='#c3b4a7',
                 fg='#fefcfb').grid(row=6, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_3, text=f'!A: {not_a}', font=('Arial', 14, 'bold'), bg='#8e8680',
                 fg='#fefcfb').grid(row=7, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_3, text=f'!C: {not_c}', font=('Arial', 14, 'bold'), bg='#706a64',
                 fg='#fefcfb').grid(row=8, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_3, text=f'Відповідь D:', font=('Arial', 14, 'bold'), bg='#605a55',
                 fg='#fefcfb').grid(row=9, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
        tk.Label(win_3, text=f'{result}', font=('Arial', 14, 'bold'), bg='#524e49',
                 fg='#fefcfb').grid(row=10, column=0, sticky='wens', padx=1, pady=1, columnspan=2)

    def save_to_file():
        global result
        res = open('res_2.txt', 'wb')
        pickle.dump(result, res)
        res.close()

    win_3 = tk.Toplevel()
    win_3.geometry('500x340+1500+300')
    win_3.title('Вкладка 3')
    win_3.config(bg='#000000')
    win_3.resizable(False, False)
    tk.Label(win_3, text='Спрощенна множина D:', font=('Arial', 14, 'bold'), bg='#34312d',
             fg='#fefcfb').grid(row=0, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_3, text='!A | !C | B', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=1, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_3, text=f'Множина A: {A}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=2, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_3, text=f'Множина B: {B}', font=('Arial', 14, 'bold'), bg='#706a64',
             fg='#fefcfb').grid(row=3, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_3, text=f'Множина C: {C}', font=('Arial', 14, 'bold'), bg='#605a55',
             fg='#fefcfb').grid(row=4, column=0, sticky='wens', padx=1, pady=1, columnspan=2)

    tk.Button(win_3, text='Обчислити', bd=0, font=('Arial', 15, 'bold'), bg='#f3f3f4', fg='#14110f', command=solve_sets).grid(
        row=5,
        column=0,
        sticky='wens',
        padx=1,
        pady=1)
    tk.Button(win_3, text='Зберегти до файлу', bd=0, font=('Arial', 15, 'bold'), bg='#f3f3f4', fg='#14110f',
              command=save_to_file).grid(
        row=5,
        column=1,
        sticky='wens',
        padx=1,
        pady=1)

    win_3.grid_columnconfigure(0, minsize=250)
    win_3.grid_columnconfigure(1, minsize=250)


def open_window_4():
    global A, B, C, U, X, Y, Z, my_Z

    X = U - B
    Y = U - A

    def xor_sets():
        global X, Y, my_Z
        my_Z = X.union(Y)
        for i in X:
            for j in Y:
                if i == j:
                    my_Z.remove(j)

    xor_sets()
    z_file = open('res_z.txt', 'wb')
    pickle.dump(my_Z, z_file)
    z_file.close()

    win_4 = tk.Toplevel()
    win_4.geometry('500x150+1500+300')
    win_4.title('Вкладка 4')
    win_4.config(bg='#000000')
    win_4.resizable(False, False)
    tk.Label(win_4, text='Операція Z:', font=('Arial', 14, 'bold'), bg='#34312d',
             fg='#fefcfb').grid(row=0, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_4, text='X ^ Y', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=1, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_4, text=f'Множина X: {X}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=2, column=0, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_4, text=f'Множина Y: {Y}', font=('Arial', 14, 'bold'), bg='#706a64',
             fg='#fefcfb').grid(row=2, column=1, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_4, text='Множина Z (авторська функція):', font=('Arial', 14, 'bold'), bg='#605a55',
             fg='#fefcfb').grid(row=3, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_4, text=f'{my_Z}', font=('Arial', 14, 'bold'), bg='#605a55',
             fg='#fefcfb').grid(row=4, column=0, sticky='wens', padx=1, pady=1, columnspan=2)

    win_4.grid_columnconfigure(0, minsize=250)
    win_4.grid_columnconfigure(1, minsize=250)


def open_window_5():
    global X, Y
    win_5 = tk.Toplevel()
    win_5.geometry('500x240+1500+300')
    win_5.title('Вкладка 5')
    win_5.config(bg='#000000')
    win_5.resizable(False, False)

    def open_res(file, value):
        file_name = open(file, 'rb')
        value = pickle.load(file_name)
        file_name.close()
        return value

    def if_equal(value_1, value_2):
        if value_1 == value_2:
            return 'Результати сходяться'
        elif value_1 != value_2:
            return 'Результати не сходяться'

    hard_D = set()
    hard_D = open_res('res.txt', hard_D)
    easy_D = set()
    easy_D = open_res('res_2.txt', easy_D)
    hard_Z = set()
    hard_Z = open_res('res_z.txt', hard_Z)
    easy_Z = X ^ Y

    tk.Label(win_5, text='Множина D:', font=('Arial', 14, 'bold'), bg='#34312d',
             fg='#fefcfb').grid(row=0, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_5, text='Початкова', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=1, column=0, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'{hard_D}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=2, column=0, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'Спрощена', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=1, column=1, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'{easy_D}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=2, column=1, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'{if_equal(hard_D, easy_D)}', font=('Arial', 14, 'bold'), bg='#605a55',
             fg='#fefcfb').grid(row=3, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_5, text=f'Множина Z:', font=('Arial', 14, 'bold'), bg='#34312d',
             fg='#fefcfb').grid(row=4, column=0, sticky='wens', padx=1, pady=1, columnspan=2)
    tk.Label(win_5, text=f'Авторська функція', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=5, column=0, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'{hard_Z}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=6, column=0, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'Функція Python', font=('Arial', 14, 'bold'), bg='#524e49',
             fg='#fefcfb').grid(row=5, column=1, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'{easy_Z}', font=('Arial', 14, 'bold'), bg='#8e8680',
             fg='#fefcfb').grid(row=6, column=1, sticky='wens', padx=1, pady=1, columnspan=1)
    tk.Label(win_5, text=f'{if_equal(hard_Z, easy_Z)}', font=('Arial', 14, 'bold'), bg='#605a55',
             fg='#fefcfb').grid(row=7, column=0, sticky='wens', padx=1, pady=1, columnspan=2)

    win_5.grid_columnconfigure(0, minsize=250)
    win_5.grid_columnconfigure(1, minsize=250)


win = tk.Tk()
win.title('Лаб')
win.geometry('700x700+1200+500')
win.resizable(False, False)
win.config(bg='#34312d')

make_tab_button('Вкладка 2', open_window_2).grid(row=0, column=0, sticky='wens', padx=1, pady=1)
make_tab_button('Вкладка 3', open_window_3).grid(row=0, column=1, sticky='wens', padx=1, pady=1)
make_tab_button('Вкладка 4', open_window_4).grid(row=0, column=2, sticky='wens', padx=1, pady=1)
make_tab_button('Вкладка 5', open_window_5).grid(row=0, column=3, sticky='wens', padx=1, pady=1)
make_info_button().grid(row=0, column=4, stick='wens', padx=1, pady=1, ipadx=2)

radio_var = tk.IntVar()
tk.Radiobutton(win, text='Ввести множину вручну', font=('Arial', 15, 'bold'), bg='#c3b4a7', fg='#14110f',
               variable=radio_var, value=1, command=lambda: select_btn()).grid(row=1, column=0, columnspan=4,
                                                                               sticky='wens', padx=1, pady=1)
make_lable("Введіть множини:", '#aca29b').grid(row=2, column=0, columnspan=4, sticky='wens', padx=1, pady=1)
make_lable("Множина A:", '#8e8680').grid(row=3, column=0, columnspan=2, sticky='we', padx=1, pady=1)
field_1 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.DISABLED)
field_1.grid(row=3, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)
make_lable("Множина B:", '#706a64').grid(row=4, column=0, columnspan=2, sticky='we', padx=1, pady=1)
field_2 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.DISABLED)
field_2.grid(row=4, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)
make_lable("Множина C:", '#605a55').grid(row=5, column=0, columnspan=2, sticky='we', padx=1, pady=1)
field_3 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.DISABLED)
field_3.grid(row=5, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)

make_lable("Або", '#34312d').grid(row=6, column=0, columnspan=4, sticky='wens', padx=1, pady=1)

tk.Radiobutton(win, text='Згенерувати множину випадково', font=('Arial', 15, 'bold'), bg='#c3b4a7', fg='#14110f',
               variable=radio_var, value=2, command=lambda: select_btn()).grid(row=7, column=0, columnspan=4,
                                                                               sticky='wens', padx=1, pady=1)
make_lable("Введіть потужність множин:", '#aca29b').grid(row=8, column=0, columnspan=4, sticky='wens', padx=1, pady=1)
make_lable("Потужність множини A:", '#8e8680').grid(row=9, column=0, columnspan=2, sticky='we', padx=1, pady=1)
field_4 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.DISABLED)
field_4.grid(row=9, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)
make_lable("Потужність множини B:", '#706a64').grid(row=10, column=0, columnspan=2, sticky='we', padx=1, pady=1)
field_5 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.DISABLED)
field_5.grid(row=10, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)
make_lable("Потужність множини C:", '#605a55').grid(row=11, column=0, columnspan=2, sticky='we', padx=1, pady=1)
field_6 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.DISABLED)
field_6.grid(row=11, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)

make_lable("", '#4a4641').grid(row=12, column=0, columnspan=4, sticky='wens', padx=1, pady=1)

make_lable("Введіть діапазон універсальної множини:", '#aca29b').grid(row=13, column=0, columnspan=4, sticky='wens', padx=1,
                                                                      pady=1)
make_lable("Від:", '#8e8680').grid(row=14, column=0, columnspan=2, sticky='wens', padx=1, pady=1)
field_7 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.NORMAL)
field_7.grid(row=14, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)
make_lable("До:", '#605a55').grid(row=15, column=0, columnspan=2, sticky='wens', padx=1, pady=1)
field_8 = tk.Entry(win, font=('Arial', 15, 'bold'), width=5, bd=0, bg='#d6d6d8', state=tk.NORMAL)
field_8.grid(row=15, column=2,
             columnspan=2,
             sticky='wens', pady=1,
             padx=1)

make_gen_button('Згенерувати множини').grid(row=16, column=0, columnspan=4, sticky='wens', padx=1, pady=1)

make_lable("Множина A:", '#706a64').grid(row=17, column=0, columnspan=2, rowspan=2, sticky='wens', padx=1, pady=1)
make_lable("Множина B:", '#706a64').grid(row=19, column=0, columnspan=2, rowspan=2, sticky='wens', padx=1, pady=1)
make_lable("Множина C:", '#706a64').grid(row=21, column=0, columnspan=2, rowspan=2, sticky='wens', padx=1, pady=1)
make_lable("Множина U:", '#706a64').grid(row=23, column=0, columnspan=2, rowspan=2, sticky='wens', padx=1, pady=1)

make_lable("0", '#605a55').grid(row=17, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)
make_lable("0", '#605a55').grid(row=19, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)
make_lable("0", '#605a55').grid(row=21, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)
make_lable("0", '#605a55').grid(row=23, column=2, columnspan=3, rowspan=2, sticky='wens', padx=1, pady=1)

win.grid_rowconfigure(0, minsize=30)
win.grid_rowconfigure(17, minsize=38.75)
win.grid_rowconfigure(19, minsize=38.75)
win.grid_rowconfigure(21, minsize=38.75)
win.grid_rowconfigure(23, minsize=38.75)

win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=50)
win.grid_columnconfigure(2, minsize=50)
win.grid_columnconfigure(3, minsize=50)
win.grid_columnconfigure(4, minsize=240)

win.mainloop()
