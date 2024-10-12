import time
import random

x = 1
y = 1
width = 5
height = 5

g = [[0 for a in range(width)] for b in range(height)]
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
g[1][2] = 1
g[2][2] = 1
g[3][2]= 1
### expected result
#[0][0][0][0][0]
#[0][0][0][0][0]
#[0][1][1][1][0]
#[0][0][0][0][0]
#[0][0][0][0][0]

import copy

for r in g:
    #for cell in range(0,len(r)):
        #if random.randint(0,1) ==  1:
            #r[cell] = 1
    print (r)
            

def updateBoard(g,x,y,width,height,newG):
    newG = copy.deepcopy(newG)
    livecount = checkNeighbours(g,x,y,width,height)
    if livecount < 2:
        newG[x][y] = 0
    elif livecount > 3:
        newG[x][y] = 0
    elif livecount == 3:
        newG[x][y] = 1
    return newG

def runGen(g,x,y,width,height):
    userinp = input("enter 0 to end the game")
    newG = g.copy()
    while userinp != "0":
        for x in range(width):
            for y in range(height):
                newG = updateBoard(g,x,y,width,height,newG)
        print()
        for r in newG:print(r)
        userinp = input("enter 0 to end the game")
        g = copy.deepcopy(newG)

def checkNeighbours(g,x,y,width,height):
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


runGen(g,x,y,width,height)
print()
print()
for r in g: print(r)
