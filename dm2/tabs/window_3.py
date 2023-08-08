from tkinter import Toplevel, Canvas, LAST
from widget_maker import *
from pickle import load, dump
from .window_2 import women
from random import choice


def win_3():
    def a_grand_b():
        A = set()
        for i in res_a:
            if i in women:
                A.add(i)
        B = res_b
        S = []
        for i in range(min(len(A), len(B))):
            p = choice(list(A))
            q = choice(list(B))
            if p != q:
                S.append([p, q])
        return S

    def a_godmother_b():
        A = set()
        for i in res_a:
            if i in women:
                A.add(i)
        B = res_b
        R = []
        for i in range(min(len(A), len(B))):
            p = choice(list(A))
            q = choice(list(B))
            if p != q and [p, q] not in S:
                R.append([p, q])
        return R

    win3 = Toplevel()
    win3.title('Вікно 3')
    win3.geometry('375x640+1000+500')
    win3.resizable(False, False)

    file_a = open('a.txt', 'rb')
    res_a = load(file_a)
    file_a.close()
    make_label(win3, 'A', 15).grid(row=0, column=0)
    make_listbox(win3, res_a).grid(row=1, column=0)
    file_b = open('b.txt', 'rb')
    res_b = load(file_b)
    file_b.close()
    make_label(win3, 'B', 15).grid(row=0, column=1)
    make_listbox(win3, res_b).grid(row=1, column=1)
    S = a_grand_b()
    file_s = open('s.txt', 'wb')
    dump(S, file_s)
    file_s.close()
    R = a_godmother_b()
    file_r = open('r.txt', 'wb')
    dump(R, file_r)
    file_r.close()
    relation_s = Canvas(win3, width=330, height=200)
    relation_s.grid(row=2, column=0, columnspan=2)
    s_lines_a = {}
    s_lines_b = {}
    relation_s.create_text(160, 30, text='a онучка b', font='Arial 20')
    for i in range(len(res_a)):
        relation_s.create_text(30 + i * 50, 50, text=list(res_a)[i], font='Arial 10')
        relation_s.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#1d8a99")
        s_lines_a.update({list(res_a)[i]: [30 + i * 50, 80]})
    for j in range(len(res_b)):
        relation_s.create_text(30 + j * 50, 190, text=list(res_b)[j], font='Arial 10')
        relation_s.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#7c77b9")
        s_lines_b.update({list(res_b)[j]: [30 + j * 50, 160]})
    for k in S:
        relation_s.create_line(s_lines_a[k[0]], s_lines_b[k[1]], arrow=LAST)

    relation_R = Canvas(win3, width=330, height=200)
    relation_R.grid(row=3, column=0, columnspan=2)
    r_lines_a = {}
    r_lines_b = {}
    relation_R.create_text(160, 30, text='a хрещена b', font='Arial 20')
    for i in range(len(res_a)):
        relation_R.create_text(30 + i * 50, 50, text=list(res_a)[i], font='Arial 10')
        relation_R.create_oval(20 + i * 50, 60, 40 + i * 50, 80, fill="#8fbfe0")
        r_lines_a.update({list(res_a)[i]: [30 + i * 50, 80]})
    for j in range(len(res_b)):
        relation_R.create_text(30 + j * 50, 190, text=list(res_b)[j], font='Arial 10')
        relation_R.create_oval(20 + j * 50, 160, 40 + j * 50, 180, fill="#14fff7")
        r_lines_b.update({list(res_b)[j]: [30 + j * 50, 160]})
    for k in R:
        relation_R.create_line(r_lines_a[k[0]], r_lines_b[k[1]], arrow=LAST)


if __name__ == '__main__':
    win_3()
