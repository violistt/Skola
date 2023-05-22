import tkinter
import random

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=1000, height = 1000, bg = "white")
canvas.pack()

x = 10
y = 10
hrubka = random.randint(0, 9)
cislo = hrubka


canvas.pack()
farby = ["red", "blue", "yellow", "brown", "magenta",  
        "lime", "black", "cyan", "orange", "purple", "pink", "white"]
#canvas.create_rectangle(x, y, x + 80, y + 80, fill = "black", outline = "" )
hrubka = random.randint(1, 9)
#canvas.create_rectangle(x, y, x + 5, y + 80, fill = "black", outline = "" )


for i in range(8):
    hrubka = random.randint(1, 9)
    x += 10
    canvas.create_rectangle(x, y, x + 10, y + 60, fill = "black", outline = "" )
    canvas.create_text(x, y + 70,  text = hrubka, fill = "black", font = ("Arial 10"))
    canvas.create_rectangle(x, y, x + hrubka, y + 60, fill = "white", outline = "")
canvas.create_rectangle(x + hrubka, y, x + 10, y + 80, fill = "black", outline = "" )

#vela kodov naraz
file = open("ciarove_kody.txt", "r")
def groupcodes():
    global x, y, hrubka
    for i in range(3):
        kody = file.readline()
        canvas.create_rectangle(x, y, x + 5, y + 80, fill = "black", outline = "" )
        for j in range (8):
            hrubka = int(kody[j])
            x += 10
            canvas.create_rectangle(x, y, x + 10, y + 60, fill = "black", outline = "" )
            canvas.create_text(x, y + 70,  text = hrubka, fill = "black", font = ("Arial 10"))
            canvas.create_rectangle(x, y, x + hrubka, y + 60, fill = "white", outline = "")
        canvas.create_rectangle(x + 10, y, x + 15, y + 80, fill = "black", outline = "" )
        x += 80
for i in range(3):
    groupcodes()
    y += 120
    x = 10

root.mainloop()
