import random
from tkinter import *

root = Tk()

canvas = Canvas(width = 500, height = 500, bg = 'white')
canvas.pack()

def stvorce():
    x, y = 200, 200
    for i in range(4):
        canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill = farba[i])
        canvas.create_text(x, y, text = i + 1)
        if ((i + 1) & 1):
            x += 110
        else:
            x = 200
            y += 110

def get_button():
    global pos
    n = int(entry0.get())
    for i in range(n):
        k = random.randint(0, 3)
        if (k == 0):
            canvas.create_rectangle(150, 150, 250, 250, fill = stlacenie[k])
            canvas.create_text(200, 200, text = k + 1)
            canvas.update()
            canvas.after(1000)
            canvas.create_rectangle(150, 150, 250, 250, fill = farba[k])
            canvas.create_text(200, 200, text = k + 1)

        elif (k == 1):
            canvas.create_rectangle(260, 150, 360, 250, fill = stlacenie[k])
            canvas.create_text(310, 200, text = k + 1)
            canvas.update()
            canvas.after(1000)
            canvas.create_rectangle(260, 150, 360, 250, fill = farba[k])
            canvas.create_text(310, 200, text = k + 1)

        elif (k == 2):
            canvas.create_rectangle(150, 260, 250, 360, fill = stlacenie[k])
            canvas.create_text(200, 310, text = k + 1)
            canvas.update()
            canvas.after(1000)
            canvas.create_rectangle(150, 260, 250, 360, fill = farba[k])
            canvas.create_text(200, 310, text = k + 1)

        else:
            canvas.create_rectangle(260, 260, 360, 360, fill = stlacenie[k])
            canvas.create_text(310, 310, text = k + 1)
            canvas.update()
            canvas.after(1000)
            canvas.create_rectangle(260, 260, 360, 360, fill = farba[k])
            canvas.create_text(310, 310, text = k + 1)
        if (i == 0):
            pos = k + 1
            continue
        pos *= 10
        pos += k + 1

def check_answer():
    k = int(entry1.get())
    canvas.delete('result')
    canvas.delete('odpoved')
    canvas.create_text(250, 400, text = "Right answer!" if (k == pos) else "Wrong! Right answer was: ", tags = 'result')
    if (k != pos):
        canvas.delete('odpoved')
        canvas.create_text(250, 420, text = pos, tags = 'odpoved')
        

farba = ['red', '#228B22', 'blue', 'yellow']
stlacenie = ['#800000', '#006400', '#00008B', '#FFA500']

stvorce()

pos = 1

entry0 = Entry()
entry0.pack()

button = Button(text = 'Start new game', command = get_button)
button.pack()

entry1 = Entry()
entry1.pack()

check = Button(text = 'Check my answer', command = check_answer)
check.pack()

root.mainloop()
