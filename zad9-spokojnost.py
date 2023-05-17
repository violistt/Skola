import sys
import tkinter
from collections import defaultdict
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 480, height = 520)
canvas.pack()

spokojnost = [i.strip().split() for i in open("spokojnost_1.txt", 'r').readlines()]
casy = defaultdict(lambda: 0)
nie = 0
for cas, vyjadrenie in spokojnost:
    hodina = int(cas[:2])
    if (vyjadrenie == "nie"):
        casy[hodina] += 1
        nie += 1
print("Počet negatívnych vyjadrení:", nie)
x = 0
for i in range(24):
    canvas.create_line(x, 500, x + 15, 500)
    t = '0' + str(i + 1) if (i < 9) else i + 1
    canvas.create_text(x + 7.5, 510, text = t, fill = 'red')
    canvas.create_rectangle(x, 500, x + 15, 500 - (casy[i + 1] * 50), fill = 'red')
    x += 17
root.mainloop()
