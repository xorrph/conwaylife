import time
import random

x = 1
y = 1
width = 4
height = 4

g = [[0 for a in range(width)] for b in range(height)]
for r in g:
    for cell in range(0,len(r)):
        if random.randint(0,1) ==  1:
            r[cell] = 1
    print (r)
            

def updateBoard(g,x,y,width,height,newG):
    livecount = checkNeighbours(g,x,y,width,height)
    print(livecount)
    if livecount < 2:
        newG[x][y] = 0
    elif livecount > 3:
        newG[x][y] = 0
    elif livecount == 3:
        newG[x][y] = 1
    return newG

def runGame(g,x,y,width,height):
    userinp = input("enter 0 to end the game")
    while userinp != "0":
        newG = g.copy()
        for x in range(width):
            for y in range(height):
                newG = updateBoard(g,x,y,width,height,newG)
        for r in newG:print(r)
        userinp = input("enter 0 to end the game")
        g = newG.copy()
                

def checkNeighbours(g,x,y,width,height):
        livecount = 0
        if x == 0 and y == 0: # top left corner
            print("check1")
            for i in range(x, x + 2):
                for j in range(y, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == 0 and y == height - 1: # bottom left corner
            print("checkq")
            for i in range(x, x + 2):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width -1 and y == height -1: # bottom right corner
            print("check3")
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width -1 and y == 0: # top right corner
            print("check4")
            for i in range(x, x + 1):
                for j in range(y, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == 0: #left side
            print("check5")
            for i in range(x, x + 2):
                for j in range(y - 1, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width -1 : #right side
            print("check6")
            for i in range(x-1, x + 1):
                for j in range(y - 1, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif y == height -1 : #bottom side
            print("check7")
            for i in range(x-1, x + 2):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif y == 0: #top side
            print("check8")
            for i in range(x-1, x + 2):
                for j in range(y, y + 2):
                    print("x",x,y)
                    print(i,j)
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        else:
                print("check9")
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if g[i][j] == 1:
                            if i == x and j == y:
                                continue
                            livecount += 1
        return livecount


runGame(g,x,y,width,height)
print()
print()
for r in g: print(r)
