import tkinter as tk  # PEP8: `import *` is not preferred
import random

class MyMap():
    def __init__(self, master, i, j, colour):
        self.text = tk.StringVar(master, value="")
        self.colour = colour
        self.label = tk.Label(master, textvariable=self.text, height=5, width=11, relief='flat', bg=self.colour, fg="white")
        self.label.grid(row=i, column=j, sticky='w')
        self.row = i
        self.col = j


def running(g,width,height):
    root = tk.Tk()

    ##width = 5
    ##height = 5
    ##g = [[0 for a in range(width)] for b in range(height)]
    ##for r in g:
    ##    for cell in range(0,len(r)):
    ##        if random.randint(0,1) ==  1:
    ##            r[cell] = 1

    for r in range(width):
        for c in range(height):
            
            f = tk.Frame(root)
            f.grid(row=r, column=c)

            if g[r][c] == 1:
                MyMap(f, 1, 1,"azure4")
            else:
                MyMap(f, 1, 1,"white")

    root.after(1000, running(g,width,height))
    root.mainloop()
