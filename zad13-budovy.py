import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

budovy = [i.strip().split() for i in open("zastavba_na_ulici.txt", 'r')]
n = len(budovy)
for i in range(n):
    budovy[i] = int(budovy[i][0]), int(budovy[i][1])

def vykresli():
    k = int(entry.get()) # Max. vyska
    x = 150
    for sirka, vyska in budovy:
        if (not vyska):
            canvas.create_line(x, 400, x + sirka, 400 - vyska, fill = 'green', width = 2)
        else:
            canvas.create_rectangle(x, 400, x + sirka, 400 - vyska, fill = 'gray', outline = 'black', width = 2)
        x += sirka

    x = 150 + budovy[0][0]
    for i in range(1, n):
        if (budovy[i - 1][1] and budovy[i][1] and budovy[i][1] - budovy[i - 1][1] > k):
            canvas.create_line(x, 400 - budovy[i - 1][1], x, 400 - budovy[i][1], fill = 'red', width = 2)
        elif (budovy[i - 1][1] and budovy[i][1] and budovy[i - 1][1] - budovy[i][1] > k):
            canvas.create_line(x, 400 - budovy[i - 1][1], x, 400 - budovy[i][1], fill = 'red', width = 2)
        x += budovy[i][0]

entry = tkinter.Entry()
entry.pack()
button = tkinter.Button(text = 'Vykresli', command = vykresli)
button.pack()

root.mainloop()
