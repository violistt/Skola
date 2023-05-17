import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 10000, height = 10000)
canvas.pack()

slovensko = [i.strip().split() for i in open("sr.txt", 'r').readlines()]
for x, y in slovensko:
    x, y = int(x), int(y)
    canvas.create_oval(x, y, x, y, outline = 'green')

strediska = [i.split() for i in open("sneh.txt", 'r').readlines()]
# strediska boli aj von z mapy, treba ich posunut (cca. o 100 hore)

def vykresli(event):
    global cislo_strediska
    canvas.delete('stredisko')
    canvas.delete('udaj')
    x, y = int(strediska[cislo_strediska][0]), int(strediska[cislo_strediska][1])
    canvas.create_oval(x, y - 100, x, y - 100, width = 5, outline = 'red', tags = 'stredisko')
    canvas.create_text(500, 500, text  = strediska[cislo_strediska], tags = 'udaj')
    cislo_strediska += 1
    if (cislo_strediska == len(strediska) - 1):
        sys.exit()

cislo_strediska = 0
canvas.bind_all('<Key>', vykresli)

root.mainloop()
