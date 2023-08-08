from widget_maker import *
from tkinter import *
from math import sqrt
import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import *



def make_matrix():
    global length, mtrx_arr_copy, summa
    length = len(mtrx_arr)
    for i in range(length):
        temp_arr = []
        for j in range(length):
            temp_arr.append(mtrx_arr[i][j])
        mtrx_arr_copy.append(temp_arr)
    for i in range(length):
        for j in range(i, length):
            if mtrx_arr[i][j] > 0:
                summa += mtrx_arr[i][j]
    set_graph(summa, length)


def build_graph():
    global mtrx_arr, length

    g = nx.DiGraph()
    for i in range(length):
        g.add_node(i + 1)
    for i in range(length):
        for j in range(i, length):
            if mtrx_arr[i][j] == 1:
                g.add_edge(i + 1, j + 1)
    return g


def matrix_graph():
    g = build_graph()
    return g


def draw_graph(G: Graph, x: int, y: int, c: list):
    global wtf
    size = int(sqrt(len(G.nodes)) ** 1.15)
    f = plt.Figure(figsize=(size, size), dpi=200 / size)
    a = f.add_subplot(111)
    nx.draw(G, ax=a, with_labels=True, node_color=c, arrowstyle='-', pos=nx.spring_layout(G, seed=wtf))
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.get_tk_widget().place(x=x, y=y)


def set_graph(weight: int, height: int):
    global mtrx_arr_copy, void
    a = 0
    void = []
    for i in range(height):
        current_void = []
        for j in range(weight):
            current_void.append(0)
        void.append(current_void)

    for i in range(height):
        for j in range(height):
            if mtrx_arr_copy[i][j] > 0 and a < weight:
                while mtrx_arr_copy[i][j] != 0:
                    if i != j:
                        void[i][a] += 1
                        void[j][a] -= 1
                        a += 1
                        mtrx_arr_copy[i][j] -= 1
                    else:
                        if i == j:
                            void[i][a] += 2
                            a += 1
                            mtrx_arr_copy[i][j] -= 1


def clear_all():
    global mtrx_arr, void, mtrx_arr_copy, summa, length, wtf
    mtrx_arr.clear()
    void.clear()
    mtrx_arr_copy.clear()
    summa = 0
    length = 0
    land.clear()


def fill_color(i):
    global node_color
    zxc = {0}
    for j in range(i):
        if mtrx_arr[j][i] > 0:
            zxc.add(node_color[j])
    current_color = 0
    while True:
        current_color += 1
        if current_color not in zxc:
            break
    return current_color


def set_col():
    global node_color, next_col, original_col
    node_color = [0 for i in range(len(mtrx_arr))]
    next_col = [0 for i in range(len(mtrx_arr))]
    original_col = ['#9fffcb' for i in range(len(mtrx_arr))]
    for i in range(len(mtrx_arr)):
        node_color[i] = fill_color(i)
        next_col[i] = my_colors[node_color[i]]


def run():
    make_matrix()
    set_col()
    draw_graph(matrix_graph(), 270, 85, original_col)
    draw_graph(matrix_graph(), 480, 85, next_col)


def read_matrix(s: str):
    global mtrx_arr
    s = s.replace(" ", "").replace("\n", "")
    if len(s) > 0:
        mtrx_arr.clear()
        split = s.split(",")
        length = int(sqrt(len(split)))
        for i in range(length):
            temp_arr = []
            for j in range(length):
                if len(split[length * i + j].strip()) > 0:
                    temp_arr.append(int(split[length * i + j]))
            mtrx_arr.append(temp_arr)


def read_matrix_text():
    global wtf
    wtf += 1
    clear_all()
    s: str = txt_matrix.get('1.0', END)
    read_matrix(s)
    run()


mtrx_arr = []
length = 0
void = []
summa = 0
mtrx_arr_copy = []
land = {}
wtf = 0
my_colors = ['#fca311', '#00b4d8', '#8338ec',
             '#ef233c', '#ffd60a', '#f72585',
             '#fc7753', '#06d6a0', '#eb4511']
node_color = []
original_col = []
next_col = []

root = Tk()
root.resizable(False, False)
root.title("Лаб 4")
root.geometry("690x330")
root.config(bg="lightgray")
make_label(root, f"Скоробогатов Ігор\nІО-25 \nМій номер: 28 \nМій варіант: {2528 % 6 + 1}",
           ('Arial', 12)).place(x=10, y=10)
make_label(root, "Метод 'модифікований евристичний \nалгоритм'", ('Arial', 12)).place(x=157, y=10)
make_label(root, "Задайте граф у вигляді \nматриці суміжності", ('Arial', 12)).place(x=10, y=95)
txt_matrix = Text(width=30, height=11, wrap=WORD)
txt_matrix.place(x=10, y=140)
Button(root, text="Побудувати граф", command=read_matrix_text).place(x=270, y=292)

Label(root, text="Граф").place(x=350, y=60)
Label(root, text="Розфарбований граф").place(x=520, y=60)
root.mainloop()
