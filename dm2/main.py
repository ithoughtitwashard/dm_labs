from tkinter import Tk
from widget_maker import make_button
from tabs import info, win_2, win_3, win_4

root = Tk()
root.title('Лаб 2')
root.geometry('+1200+500')
root.resizable(False, False)

make_button(root, 'Інформація', info, 15).grid(row=0, column=0, sticky='wens')
make_button(root, 'Вікно 2', win_2, 15).grid(row=1, column=0, sticky='wens')
make_button(root, 'Вікно 3', win_3, 15).grid(row=2, column=0, sticky='wens')
make_button(root, 'Вікно 4', win_4, 15).grid(row=3, column=0, sticky='wens')

root.columnconfigure(0, minsize=200)
root.rowconfigure(0, minsize=50)
root.rowconfigure(1, minsize=50)
root.rowconfigure(2, minsize=50)
root.rowconfigure(3, minsize=50)

root.mainloop()
