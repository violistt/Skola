import tkinter

root = tkinter.Tk()
term = tkinter.Frame(root, height = 500, width = 500)

term.pack(fill = tkinter.BOTH, expand = tkinter.YES)
wid = term.winfo_id()

canvas = tkinter.Canvas(width = 500, height = 500, bg = 'white')
canvas.pack()

def vlavo(p):
    global x_obdlznik
    x_obdlznik -= 20 if (x_obdlznik - 80 >= 0) else 0
    canvas.delete('obdlznik')
    obdlznik(p)

def vpravo(p):
    global x_obdlznik
    x_obdlznik += 20 if (x_obdlznik + 80 <= 500) else 0
    canvas.delete('obdlznik')
    obdlznik(p)

def obdlznik(p):
    canvas.create_rectangle(x_obdlznik + 50, y_obdlznik + 10, x_obdlznik - 50, y_obdlznik - 10, tags = 'obdlznik')

def lopticka():
    global x_lopticka, y_lopticka, opacne_x, opacne_y, flag, koniec
    canvas.delete('lopticka')
    canvas.create_oval(x_lopticka + 15, y_lopticka + 15, x_lopticka - 15, y_lopticka - 15, tags = 'lopticka')
    if (y_lopticka == 410):
        if (not x_obdlznik - 70 <= x_lopticka <= x_obdlznik + 70):
            koniec = 1
    if (not koniec):
        if (x_lopticka + 10 >= 500 or x_lopticka - 10 <= 0):
            opacne_x ^= 1
        if (y_lopticka + 10 >= 420 or y_lopticka - 10 <= 0):
            if ((flag & 1) ^ 1):
                flag ^= 1
            opacne_y ^= 1
        if (flag & 1):
            x_lopticka += (10 if (x_lopticka <= 490 and not opacne_x) else -10)
        y_lopticka += (10 if (y_lopticka <= 490 and not opacne_y) else -10)
        canvas.after(50, lopticka)
    
flag, koniec = 0, 0
opacne_x, opacne_y = 0, 0
x_obdlznik, y_obdlznik = 250, 440
x_lopticka, y_lopticka = 250, 250
canvas.bind_all("<Left>", vlavo, lopticka)
canvas.bind_all("<Right>", vpravo, lopticka)
canvas.create_rectangle(x_obdlznik + 50, y_obdlznik + 10, x_obdlznik - 50, y_obdlznik - 10, tags = 'obdlznik')
canvas.create_oval(x_lopticka + 15, y_lopticka + 15, x_lopticka - 15, y_lopticka - 15, tags = 'lopticka')
lopticka()

root.mainloop()
