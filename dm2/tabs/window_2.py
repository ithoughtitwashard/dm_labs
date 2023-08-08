from tkinter import Toplevel, IntVar, ANCHOR
from widget_maker import *
from pickle import dump, load

a, b, women, men = list(), list(), ('Вероніка', 'Анастасія', 'Марія', 'Вікторія', 'Мікаса', 'Александра'), (
    'Ігор', 'Діо', 'Джотаро', 'Іван', 'Ерен', 'Микита')


def win_2():
    def copy_to():
        when = radio_var.get()
        pol = sex_var.get()
        global a, b
        if when == 0 and pol == 0:
            a.append(women_listbox.get(ANCHOR))
        elif when == 1 and pol == 0:
            b.append(women_listbox.get(ANCHOR))
        elif when == 0 and pol == 1:
            a.append(men_listbox.get(ANCHOR))
        elif when == 1 and pol == 1:
            b.append(men_listbox.get(ANCHOR))

    def delete_a():
        global a
        a.clear()
        make_listbox(win2, a).grid(row=9, column=0)

    def delete_b():
        global b
        b.clear()
        make_listbox(win2, b).grid(row=9, column=1)

    def save_a():
        global a
        res = open('a.txt', 'wb')
        dump(a, res)
        res.close()

    def save_b():
        global b
        res = open('b.txt', 'wb')
        dump(b, res)
        res.close()

    def read_a():
        file = open('a.txt', 'rb')
        res = load(file)
        file.close()
        make_listbox(win2, res).grid(row=9, column=0)

    def read_b():
        file = open('b.txt', 'rb')
        res = load(file)
        file.close()
        make_listbox(win2, res).grid(row=9, column=1)

    win2 = Toplevel()
    win2.title('Вікно 2')
    win2.geometry('430x560+1000+500')
    win2.resizable(False, False)

    # ListBoxes
    global women, men
    make_label(win2, 'Жіночі імена', 15).grid(row=0, column=0)
    make_label(win2, 'Чоловічі імена', 15).grid(row=0, column=1)
    women_listbox = make_listbox(win2, women)
    men_listbox = make_listbox(win2, men)
    women_listbox.grid(row=1, column=0)
    men_listbox.grid(row=1, column=1)

    radio_var = IntVar()
    sex_var = IntVar()
    make_button(win2, 'Додати до:', copy_to, 15).grid(row=2, column=0, sticky='wens', rowspan=2)
    make_radiobutton(win2, 'A', 15, radio_var, 0).grid(row=2, column=1, sticky='wens')
    make_radiobutton(win2, 'B', 15, radio_var, 1).grid(row=3, column=1, sticky='wens')
    make_radiobutton(win2, 'Жін.', 15, sex_var, 0).grid(row=2, column=2, sticky='wens')
    make_radiobutton(win2, 'Чол.', 15, sex_var, 1).grid(row=3, column=2, sticky='wens')

    make_button(win2, 'Очистити А', delete_a, 15).grid(row=4, column=0, sticky='wens')
    make_button(win2, 'Очистити В', delete_b, 15).grid(row=4, column=1, sticky='wens')
    make_button(win2, 'Зберегти А', save_a, 15).grid(row=5, column=0, sticky='wens')
    make_button(win2, 'Зберегти В', save_b, 15).grid(row=5, column=1, sticky='wens')
    make_button(win2, 'Зчитати А', read_a, 15).grid(row=6, column=0, sticky='wens')
    make_button(win2, 'Зчитати В', read_b, 15).grid(row=6, column=1, sticky='wens')

    global a, b
    make_label(win2, 'A', 15).grid(row=8, column=0)
    make_label(win2, 'B', 15).grid(row=8, column=1)

    if __name__ == '__main__':
        win_2()
