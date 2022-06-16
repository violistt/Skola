import random
from tkinter import *

root = Tk()
canvas = Canvas(width = 500, height = 500, bg = 'white')
canvas.pack()

def krtko(sus):
    global krtko_x, krtko_y, x, y, cnt, wrong_cnt
    klik_x, klik_y = sus.x, sus.y
    if (x - 30 <= klik_x <= x + 30 and y - 30 <= klik_y <= y + 30):
        posun_x, posun_y = 170 + 70 * random.randint(0, 2), 170 + 70 * random.randint(0, 2)
        x, y = posun_x, posun_y
        canvas.delete('krtko')
        canvas.create_oval(posun_x - 30, posun_y - 30, posun_x + 30, posun_y + 30, fill = 'red', tags = 'krtko')
        cnt += 1
    else:
        wrong_cnt += 1
    canvas.delete('cnt')
    canvas.delete('wrong_cnt')
    canvas.create_text(450, 450, text = 'OK: ' + str(cnt), tags = 'cnt')
    canvas.create_text(450, 465, text = 'Mimo: ' + str(wrong_cnt), tags = 'wrong_cnt')

def stvorce():
    x, y = 170, 170
    for i in range(9):
        canvas.create_rectangle(x + 30, y + 30, x - 30, y - 30)
        canvas.create_text(x, y, text = i)
        if ((i + 1) % 3):
            x += 70
        else:
            x = 170
            y += 70

stvorce()
krtko_x, krtko_y = 170, 170
canvas.create_oval(krtko_x - 30, krtko_y - 30, krtko_x + 30, krtko_y + 30, fill = 'red', tags = 'krtko')
x, y = 170, 170
cnt, wrong_cnt = 0, 0
canvas.create_text(450, 450, text = 'OK: ' + str(cnt), tags = 'cnt')
canvas.create_text(450, 465, text = 'Mimo: ' + str(wrong_cnt), tags = 'wrong_cnt')
canvas.bind_all('<Button-1>', krtko)

root.mainloop()
