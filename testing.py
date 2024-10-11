x = 1
y = 1
width = 3
height = 3
g = [[0 for a in range(width)] for b in range(height)]
g[0][1] = 1
g[2][1] = 1
g[1][1] = 1
g[2][2] = 1
g[0][0] = 1
for r in g: print(r)

def updateBoard(g,x,y,width,height):
    newG = g.copy()
    livecount = checkNeighbours(g,x,y,width,height)
    print(livecount)
    if livecount < 2:
        newG[x][y] = 0
    elif livecount > 3:
        newG[x][y] = 0
    elif livecount == 3:
        newG[x][y] = 1
    return newG
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
        elif x == 0 and y == height: # bottom left corner
            print("checkq")
            for i in range(x, x + 2):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width and y == height: # bottom right corner
            print("check3")
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif x == width and y == 0: # top right corner
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
        elif x == width: #right side
            print("check6")
            for i in range(x-1, x + 1):
                for j in range(y - 1, y + 2):
                    if g[i][j] == 1:
                        if i == x and j == y:
                            continue
                        livecount += 1
        elif y == height: #bottom side
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


updateBoard(g,x,y,width,height)
print()
print()
for r in g: print(r)