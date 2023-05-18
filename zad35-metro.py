import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 1000, height = 500)
canvas.pack()
linky = [i.strip() for i in open("trasa_linky_metra.txt", 'r')]
n = len(linky)
farba = linky[0]
canvas.create_line(100, 410, 70 + ((n - 1) * 30), 410, fill = 'red', width = 2)
for i in range(1, n):
    f = farba
    t = linky[i]
    if (linky[i][0] == '*'):
        f = 'white'
        t = t[1:]
    if (i == 1 or i == n - 1):
        canvas.create_rectangle(50 + (i * 30), 400, 70 + (i * 30), 420, fill = f, outline = 'red')
    else:
        canvas.create_oval(50 + (i * 30), 405, 60 + (i * 30), 415, fill = f, outline = 'red')
    canvas.create_text(100 + (i * 30), 340, text = t, angle = 45)
root.mainloop()
