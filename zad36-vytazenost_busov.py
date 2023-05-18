import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 1000, height = 500)
canvas.pack()

zastavky = [i.strip().split() for i in open("vytazenost_autobusovej_linky.txt", 'r')]
k = int(zastavky[0][0])

for i, zastavka in enumerate(zastavky[1:]):
    if (len(zastavka) == 3):
        nast, vyst, meno = zastavka
    else:
        nast, vyst, meno_, _meno = zastavka
        meno = meno_ + ' ' + _meno
    canvas.create_text(100, i * 50 + 100, text = zastavka, font = 15)

def zobraz(event):
    global zastavka, cestujucich
    cestujucich += int(zastavky[zastavka + 1][0])
    cestujucich -= int(zastavky[zastavka + 1][1])
    f = 'green'
    if (cestujucich > k):
        f = 'red'
    # dlzka celeho obdlznika: 250
    # Podla preplnenosti zaplnime urcite percento
    p = int((cestujucich / k) * 250)
    canvas.create_rectangle(250, zastavka * 50 + 80, 250 + p, zastavka * 50 + 120, fill = f, outline = 'black', width = 2)
    if (250 + p < 500):
        canvas.create_rectangle(250 + p, zastavka * 50 + 80, 500, zastavka * 50 + 120, fill = 'white', outline = 'black', width = 2)
    zastavka += 1
    if (zastavka == len(zastavky)):
        sys.exit()

cestujucich = 0
zastavka = 0
canvas.bind_all('<Key>', zobraz)

root.mainloop()
