import time
import random
import tkinter as tk  # PEP8: `import *` is not preferred

x = 1
y = 1
width = 15
height = 15

g = [[random.randint(0,1) for a in range(width)] for b in range(height)]
gen = 1

class MyMap():
    def __init__(self, master, i, j, colour):
        self.text = tk.StringVar(master, value="")
        self.colour = colour
        self.label = tk.Label(master, textvariable=self.text, height=1, width=3, relief='flat', bg=self.colour, fg="white")
        self.label.grid(row=i, column=j, sticky='w')

    def update(self, colour):
        self.label.config(bg=colour)  # Update the background color
#test case 1 X
##g[1][1] = 1
##g[2][2] = 1
##g[3][3]= 1
##g[1][3] = 1
##g[3][1] = 1
# expected result
#[0][0][0][0][0]
#[0][0][1][0][0]
#[0][1][0][1][0]
#[0][0][1][0][0]
#[0][0][0][0][0]

#test case 2 bird
##g[1][1] = 1
##g[2][1] = 1
##g[2][3]= 1
##g[2][0] = 1
##g[1][3] = 1
##g[2][4] = 1
##g[3][2] = 1
# expected result
#[0][0][0][0][0]
#[0][1][0][1][0]
#[0][1][0][1][0]
#[0][1][1][1][0]
#[0][0][0][0][0]

#test case 3 star
##g[1][2] = 1
##g[2][1] = 1
##g[2][3]= 1
##g[3][2] = 1
##g[2][2] = 1
# expected result
#[0][0][0][0][0]
#[0][1][1][1][0]
#[0][1][0][1][0]
#[0][1][1][1][0]
#[0][0][0][0][0]

#test case 4 O
##g[1][2] = 1
##g[2][1] = 1
##g[2][3]= 1
##g[3][2] = 1
##g[1][1] = 1
##g[3][3] = 1
##g[1][3] = 1
##g[3][1] = 1
### expected result
#[0][0][0][0][0]
#[0][1][1][1][0]
#[0][1][0][1][0]
#[0][1][1][1][0]
#[0][0][0][0][0]


#test case 5 |
##g[2][1] = 1
##g[2][2] = 1
##g[2][3]= 1
### expected result
#[0][0][0][0][0]
#[0][0][1][0][0]
#[0][0][1][0][0]
#[0][0][1][0][0]
#[0][0][0][0][0]

#test case 5 |
#g[1][2] = 1
#g[2][2] = 1
#g[3][2]= 1
### expected result
#[0][0][0][0][0]
#[0][0][0][0][0]
#[0][1][1][1][0]
#[0][0][0][0][0]
#[0][0][0][0][0]

import copy

            

def updateBoard(g, x, y, width, height, newG):
    newG = copy.deepcopy(newG)
    livecount = checkNeighbours(g, width, height, x, y)
    if livecount < 2 or livecount > 3:
        newG[x][y] = 0
    elif livecount == 3:
        newG[x][y] = 1
    return newG




def checkNeighbours(g,width,height,x,y):
        livecount = 0
        if x == 0 and y == 0: # top left corner
            for i in range(x, x + 2):
                for j in range(y, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == 0 and y == height - 1: # bottom left corner
            for i in range(x, x + 2):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width -1 and y == height -1: # bottom right corner
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width -1 and y == 0: # top right corner
            for i in range(x, x + 1):
                for j in range(y, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == 0: #left side
            for i in range(x, x + 2):
                for j in range(y - 1, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width -1 : #right side
            for i in range(x-1, x + 1):
                for j in range(y - 1, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif y == height -1 : #bottom side
            for i in range(x-1, x + 2):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif y == 0: #top side
            for i in range(x-1, x + 2):
                for j in range(y, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        else:
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if g[i][j] == 1:
                            if i == x and j == y:
                                continue
                            livecount += 1
        return livecount

def update_grid():
    global g, newG, gen
    newG = copy.deepcopy(g)
    for x in range(width):
        for y in range(height):
            newG = updateBoard(g, x, y, width, height, newG)

    # Update the display grid by changing label colors
    for r in range(width):
        for c in range(height):
            if g[r][c] == 1:
                grid_labels[r][c].update("azure4")  # Update color for live cells
            else:
                grid_labels[r][c].update("white")   # Update color for dead cells

    g = copy.deepcopy(newG)
    gen.set(f"Gen: {generation[0]}")  # Update generation counter
    generation[0] += 1

    root.after(1000, update_grid)  # Update every second

# Create Tkinter root window
root = tk.Tk()
root.title("Game of Life")

# Generation counter
gen = tk.StringVar()
generation = [1]
tk.Label(root, textvariable=gen, height=1, width=10, relief='flat', bg="white", fg="black", font="Helvetica 12").grid(row=height, column=0, columnspan=width)

# Initialize grid labels only once and store them in grid_labels
grid_labels = [[MyMap(root, r, c, "white") for c in range(width)] for r in range(height)]

# Start updating the grid and GUI
update_grid()

root.mainloop()


