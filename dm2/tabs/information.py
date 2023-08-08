from tkinter import Toplevel
from widget_maker import make_label


def info():
    inform = Toplevel()
    inform.geometry('+1500+500')
    io = 25
    my_number = 28
    my_variant = (my_number + io % 60) % 30 + 1
    make_label(inform, f'Скоробогатов Ігор \n Моя група: ІО-{io} \n Мій номер: {my_number} \n Мій варіант: {my_variant}',
               25).grid(row=0, column=0,
                        sticky='wens')


if __name__ == '__main__':
    info()
