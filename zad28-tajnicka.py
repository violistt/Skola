import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 1000, height = 1000)
canvas.pack()

tajnicka = [i.strip().split() for i in open("krizovka1-1.txt", 'r').readlines()]
n = len(tajnicka)

def kresli():
    # Prazdna
    x, y = 250, 100
    for poz, slovo in tajnicka:
        # Najprv tajnicka, potom ostatne pismena
        poz = int(poz) - 1
        canvas.create_rectangle(x, y, x + 25, y + 25, fill = 'gray')
        _x, _y = x - 25, y
        for i in range(poz - 1, -1, -1): # Dozadu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            _x -= 25
        _x, _y = x + 25, y
        for i in range(poz + 1, len(slovo)): # Dopredu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            _x += 25
        y += 25

    # Vyriesena
    x, y = 500, 100
    for poz, slovo in tajnicka:
        # Najprv tajnicka, potom ostatne pismena
        poz = int(poz) - 1
        canvas.create_rectangle(x, y, x + 25, y + 25, fill = 'gray')
        canvas.create_text(x + 12.5, y + 12.5, text = slovo[poz])
        _x, _y = x - 25, y
        for i in range(poz - 1, -1, -1): # Dozadu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            canvas.create_text(_x + 12.5, _y + 12.5, text = slovo[i])
            _x -= 25
        _x, _y = x + 25, y
        for i in range(poz + 1, len(slovo)): # Dopredu
            canvas.create_rectangle(_x, _y, _x + 25, _y + 25)
            canvas.create_text(_x + 12.5, _y + 12.5, text = slovo[i])
            _x += 25
        y += 25

kresli()

root.mainloop()
