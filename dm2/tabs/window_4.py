from tkinter import Toplevel, Canvas, LAST
from widget_maker import *
from pickle import load
from copy import deepcopy


def win_4():
    win4 = Toplevel()
    win4.title('Вікно 4')
    win4.geometry('460x260+1000+500')
    win4.resizable(False, False)

    file_a = open('a.txt', 'rb')
    A = load(file_a)
    file_a.close()
    file_b = open('b.txt', 'rb')
    B = load(file_b)
    file_b.close()
    file_s = open('s.txt', 'rb')
    S = load(file_s)
    file_s.close()
    file_r = open('r.txt', 'rb')
    R = load(file_r)
    file_r.close()

    def button_1():
        relations.delete("all")
        relations.create_text(150, 20, text='R ⋃ S', font='Arial 16')
        line_1 = {}
        line_2 = {}
        U = R + S
        for i in range(len(A)):
            relations.create_text(30 + i * 50, 50, text=list(A)[i], font='Arial 10')
            relations.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#e365c1")
            line_1.update({list(A)[i]: [30 + i * 50, 80]})
        for j in range(len(B)):
            relations.create_text(30 + j * 50, 190, text=list(B)[j], font='Arial 10')
            relations.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#cce8cc")
            line_2.update({list(B)[j]: [30 + j * 50, 160]})
        for k in U:
            relations.create_line(line_1[k[0]], line_2[k[1]], arrow=LAST)

    def button_2():
        relations.delete("all")
        relations.create_text(150, 20, text='R ⋂ S', font='Arial 16')
        line_1 = {}
        line_2 = {}
        U = []
        for i in R:
            if i in S:
                U.append(i)

        for i in range(len(A)):
            relations.create_text(30 + i * 50, 50, text=list(A)[i], font='Arial 10')
            relations.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#e365c1")
            line_1.update({list(A)[i]: [30 + i * 50, 80]})
        for j in range(len(B)):
            relations.create_text(30 + j * 50, 190, text=list(B)[j], font='Arial 10')
            relations.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#cce8cc")
            line_2.update({list(B)[j]: [30 + j * 50, 160]})

        for k in U:
            if len(U) != 0:
                relations.create_line(line_1[k[0]], line_2[k[1]], arrow=LAST)

    def button_3():
        relations.delete("all")
        relations.create_text(150, 20, text='R \ S', font='Arial 16')
        line_1 = {}
        line_2 = {}
        U = deepcopy(R)
        for i in U:
            if i in S:
                U.remove(i)

        for i in range(len(A)):
            relations.create_text(30 + i * 50, 50, text=list(A)[i], font='Arial 10')
            relations.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#e365c1")
            line_1.update({list(A)[i]: [30 + i * 50, 80]})
        for j in range(len(B)):
            relations.create_text(30 + j * 50, 190, text=list(B)[j], font='Arial 10')
            relations.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#cce8cc")
            line_2.update({list(B)[j]: [30 + j * 50, 160]})
        for k in U:
            relations.create_line(line_1[k[0]], line_2[k[1]], arrow=LAST)

    def button_4():
        relations.delete("all")
        relations.create_text(150, 20, text='U \ R', font='Arial 16')
        line_1 = {}
        line_2 = {}
        U = []
        a = deepcopy(A)
        b = deepcopy(B)
        for i in a:
            for j in b:
                U.append([i, j])
        for i in U:
            if i in R:
                U.remove(i)
        for i in range(len(A)):
            relations.create_text(30 + i * 50, 50, text=list(A)[i], font='Arial 10')
            relations.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#e365c1")
            line_1.update({list(A)[i]: [30 + i * 50, 80]})
        for j in range(len(B)):
            relations.create_text(30 + j * 50, 190, text=list(B)[j], font='Arial 10')
            relations.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#cce8cc")
            line_2.update({list(B)[j]: [30 + j * 50, 160]})
        for k in U:
            if len(U) != 0:
                relations.create_line(line_1[k[0]], line_2[k[1]], arrow=LAST)

    def button_5():
        relations.delete("all")
        relations.create_text(150, 20, text='S⁻¹', font='Arial 16')
        line_1 = {}
        line_2 = {}
        U = deepcopy(S)
        for i in U:
            i[0], i[1] = i[1], i[0]
        for i in range(len(A)):
            relations.create_text(30 + i * 50, 50, text=list(A)[i], font='Arial 10')
            relations.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#e365c1")
            line_1.update({list(A)[i]: [30 + i * 50, 80]})
        for j in range(len(B)):
            relations.create_text(30 + j * 50, 190, text=list(B)[j], font='Arial 10')
            relations.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#cce8cc")
            line_2.update({list(B)[j]: [30 + j * 50, 160]})
        for k in U:
            relations.create_line(line_2[k[0]], line_1[k[1]], arrow=LAST)

    make_label(win4, '       ', 15).grid(row=0, column=0)
    make_label(win4, 'Операції', 'Arial 15').grid(row=0, column=1, columnspan=2)
    make_button(win4, 'R ⋃ S', button_1, 'Arial 15').grid(row=1, column=1, sticky='wens')
    make_button(win4, 'R ⋂ S', button_2, 'Arial 15').grid(row=2, column=1, sticky='wens')
    make_button(win4, 'R \ S', button_3, 'Arial 15').grid(row=3, column=1, sticky='wens')
    make_button(win4, 'U \ R', button_4, 'Arial 15').grid(row=4, column=1, sticky='wens')
    make_button(win4, 'S⁻¹', button_5, 'Arial 15').grid(row=5, column=1, sticky='wens')
    make_label(win4, '       ', 15).grid(row=6, column=2)

    relations = Canvas(win4, width=600, height=250)
    relations.grid(row=1, column=3, rowspan=6)


if __name__ == '__main__':
    win_4()
