
from tkinter import *

root = Tk()


var = IntVar()
var.set(0)

def print_rvar():
    print(var.get())

r1 = Radiobutton(text='First', value = 0, command = print_rvar, variable = var).pack(anchor=W)
r2 = Radiobutton(text='Second', value = 1, command = print_rvar, variable = var).pack(anchor=W)
r2 = Radiobutton(text='Third', value = 2, command = print_rvar, variable = var).pack(anchor=W)


root.mainloop()