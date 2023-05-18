import sys
import random
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 1000, height = 500)
canvas.pack()

n, k = random.randint(11, 20), random.randint(2, 9)
c = int((n / k) // 1) # ⌊n / k⌋
farby = ['green', 'red', 'blue', 'brown', 'orange', 'cyan', 'magenta', 'yellow', 'black', 'gray']
x, f = 100, 0
canvas.create_text(110, 200, text = str(n) + ' : ' + str(k), font = 15)
for i in range(c):
    for j in range(k):
        canvas.create_oval(x - 10, 240, x + 10, 260, fill = farby[f])
        x += 30
    f += 1
x += 30
m = n % k
for i in range(m):
    canvas.create_oval(x - 10, 240, x + 10, 260, fill = farby[f])
    x += 30

def skontroluj():
    odpoved = int(entry.get())
    if (odpoved == c):
        canvas.create_text(135, 225, text = "SPRÁVNE", font = 15)
    else:
        canvas.create_text(135, 225, text = "NESPRÁVNE", font = 15)

        


entry = tkinter.Entry()
entry.pack()
button = tkinter.Button(text = "Zadaj vysledok", command = skontroluj)
button.pack()

root.mainloop()
