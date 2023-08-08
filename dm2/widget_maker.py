from tkinter import Button, Label, Radiobutton, Listbox, Variable


def make_button(win, text, command, font):
    return Button(win, text=text, command=command, font=font)


def make_label(win, text, font):
    return Label(win, text=text, font=font)


def make_radiobutton(win, text, font, variable, value):
    return Radiobutton(win, text=text, font=font, variable=variable, value=value)


def make_listbox(win, var):
    variable = Variable(value=var)
    return Listbox(win, listvariable=variable, font=15)


def main():
    pass


if __name__ == '__main__':
    main()
