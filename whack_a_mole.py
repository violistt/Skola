import random
from tkinter import *

root = Tk()
canvas = Canvas(width = 500, height = 500, bg = 'white')
canvas.pack()

def krtko(suradnica):
    global x, y, cnt
    klik_x, klik_y = suradnica.x, suradnica.y
    if (x - 30 <= klik_x <= x + 30 and y - 30 <= klik_y <= y + 30):
        x, y = 170 + 70 * random.randint(0, 2), 170 + 70 * random.randint(0, 2)
        canvas.delete('krtko')
        canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill = 'red', tags = 'krtko')
        cnt += 1
    canvas.delete('cnt')
    canvas.create_text(450, 450, text = cnt, tags = 'cnt')

def stvorce():
    x, y = 170, 170
    for i in range(9):
        canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30)
        canvas.create_text(x, y, text = i)
        if ((i + 1) % 3):
            x += 70
        else:
            x = 170
            y += 70

stvorce()
x, y = 170, 170
canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill = 'red', tags = 'krtko')
cnt = 0
canvas.create_text(450, 450, text = cnt, tags = 'cnt')
canvas.bind('<Button-1>', krtko)

root.mainloop()
