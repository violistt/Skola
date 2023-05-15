import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 10000, height = 10000)
canvas.pack()

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

velkost = 1

def valid(x, y):
    if (0 <= x < r and 0 <= y < s):
        return 1
    return 0

def dfs(g, x, y, cislo):
    global velkost
    g[x][y] = cislo
    for i in range(4):
        susx, susy = x + dx[i], y + dy[i]
        if (not valid(susx, susy)):
            continue
        if (g[susx][susy] != '0' and type(g[susx][susy]) != int):
            velkost += 1
            dfs(g, susx, susy, cislo)

def komps(g):
    global velkost
    r = len(g)
    s = len(g[0])
    komp = 0
    najvacsi = 0
    for i in range(r):
        for j in range(s):
            if (g[i][j] != '0' and type(g[i][j]) != int):
                komp += 1
                dfs(g, i, j, komp)
                najvacsi = max(najvacsi, velkost)
                velkost = 1
    return komp, najvacsi

def kresli_mapu(g):
    x, y = 50, 50
    i, j = 0, 0
    farby = ['green', 'red', 'blue', 'brown', 'orange', 'cyan', 'magenta']
    farba = {}
    farba['0'] = 'black'
    for pos, vyska in enumerate(vysky):
        if (vyska != '0'):
            farba[vyska] = farby[pos]
    for poradie in range(len(g[0]) * len(g)):
        canvas.create_rectangle(x, y, x + 50, y + 50)
        canvas.create_text(x + 25, y + 25, text = g[i][j], fill = farba[g[i][j]])
        x += 50
        j += 1
        if ((poradie + 1) % len(g[0]) == 0):
            x = 50
            y += 50
            i += 1
            j = 0

vstup = [i.strip().split() for i in open('mapa.txt', 'r').readlines()]
r, s = len(vstup), len(vstup[0])
g = [[0 for i in range(s)] for j in range(r)]
vysky = set()
for i in range(r):
    for j in range(s):
        g[i][j] = vstup[i][j]
        vysky.add(g[i][j])
kresli_mapu(g)
pocet_ostrovov, najvacsi_ostrov = komps(g)
if (not pocet_ostrovov):
    print("Nie je tam ziaden ostrov")
else:
    print("Pocet ostrovov:", pocet_ostrovov)
    print("Rozloha najvacsieho ostrova:", najvacsi_ostrov)

root.mainloop()
