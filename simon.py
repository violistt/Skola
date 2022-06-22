import tkinter
import random

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 500, height = 500, bg = 'white')
canvas.pack()

def stvorce():
    x, y = 200, 200
    for i in range(4):
        canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill = farba[i])
        canvas.create_text(x, y, text = i + 1, fill = 'white')
        if ((i + 1) & 1):
            x += 110
        else:
            x = 200
            y += 110

def get_button():
    global cislo
    n = int(entry0.get())
    for i in range(n):
        k = random.randint(0, 3)
        if (k == 0):
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(150, 150, 250, 250, fill = stlacene[k])
            canvas.create_text(200, 200, text = k + 1, fill = 'white')
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(150, 150, 250, 250, fill = farba[k])
            canvas.create_text(200, 200, text = k + 1, fill = 'white')
        elif (k == 1):
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(260, 150, 360, 250, fill = stlacene[k])
            canvas.create_text(310, 200, text = k + 1, fill = 'white')
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(260, 150, 360, 250, fill = farba[k])
            canvas.create_text(310, 200, text = k + 1, fill = 'white')

        elif (k == 2):
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(150, 260, 250, 360, fill = stlacene[k])
            canvas.create_text(200, 310, text = k + 1, fill = 'white')
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(150, 260, 250, 360, fill = farba[k])
            canvas.create_text(200, 310, text = k + 1, fill = 'white')
        else:
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(260, 260, 360, 360, fill = stlacene[k])
            canvas.create_text(310, 310, text = k + 1, fill = 'white')
            canvas.update()
            canvas.after(500)
            canvas.create_rectangle(260, 260, 360, 360, fill = farba[k])
            canvas.create_text(310, 310, text = k + 1, fill = 'white')
        if (i == 0):
            cislo = k + 1
        else:
            cislo *= 10
            cislo += k + 1

def skontroluj():
    k = int(entry1.get())
    canvas.delete('vysledok')
    canvas.delete('odpoved')
    if (k == cislo):
        canvas.create_text(250, 400, text = "Right answer!", tags = 'vysledok')
    else:
        canvas.create_text(250, 400, text = "Wrong! Right answer was: ", tags = 'vysledok')
    if (k != cislo):
        canvas.delete('odpoved')
        canvas.create_text(250, 420, text = cislo, tags = 'odpoved')
        

farba = ['#800000', '#006400', '#00008B', '#008B8B']
stlacene = ['#FF0000', '#12AD2B', '#0000FF', '#4EE2EC']
cislo = 1

stvorce()

entry0 = tkinter.Entry()
entry0.pack()

button = tkinter.Button(text = 'Start new game', command = get_button)
button.pack()

entry1 = tkinter.Entry()
entry1.pack()

check = tkinter.Button(text = 'Check my answer', command = skontroluj)
check.pack()

root.mainloop()
