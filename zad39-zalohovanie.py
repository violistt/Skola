import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 1000, height = 500)
canvas.pack()

anketa = [i.strip().split() for i in open("anketa.txt", 'r')]
ano, nie, neviem = int(anketa[1][0]), int(anketa[1][1]), int(anketa[1][1])
canvas.create_text(200, 100, text = anketa[0])
odp = ["Áno", "Nie", "Neviem"]
ludi = ano + nie + neviem
farby = ['green', 'red', 'blue']
for i in range(3):
    t = str(i + 1) + ') ' + odp[i] + ' - ' + anketa[1][i]
    canvas.create_text(200, i * 50 + 200, text = t, tags = 'graf')
    p = (int(anketa[1][i]) / ludi) * 400
    canvas.create_rectangle(270, i * 50 + 185, 270 + p, i * 50 + 215, fill = farby[i], outline = farby[i], tags = 'graf')

def hlasuj_ano(event):
    global ludi, ano
    canvas.delete('graf')
    ludi += 1
    anketa[1][0] = str(int(anketa[1][0]) + 1)
    for i in range(3):
        t = str(i + 1) + ') ' + odp[i] + ' - ' + anketa[1][i]
        canvas.create_text(200, i * 50 + 200, text = t)
        p = (int(anketa[1][i]) / ludi) * 400
        canvas.create_rectangle(270, i * 50 + 185, 270 + p, i * 50 + 215, fill = farby[i], outline = farby[i])

def hlasuj_nie(event):
    global ludi, ano
    canvas.delete('graf')
    ludi += 1
    anketa[1][1] = str(int(anketa[1][1]) + 1)
    for i in range(3):
        t = str(i + 1) + ') ' + odp[i] + ' - ' + anketa[1][i]
        canvas.create_text(200, i * 50 + 200, text = t)
        p = (int(anketa[1][i]) / ludi) * 400
        canvas.create_rectangle(270, i * 50 + 185, 270 + p, i * 50 + 215, fill = farby[i], outline = farby[i])

def hlasuj_neviem(event):
    global ludi, ano
    canvas.delete('graf')
    ludi += 1
    anketa[1][2] = str(int(anketa[1][2]) + 1)
    for i in range(3):
        t = str(i + 1) + ') ' + odp[i] + ' - ' + anketa[1][i]
        canvas.create_text(200, i * 50 + 200, text = t)
        p = (int(anketa[1][i]) / ludi) * 400
        canvas.create_rectangle(270, i * 50 + 185, 270 + p, i * 50 + 215, fill = farby[i], outline = farby[i])

canvas.bind_all('1', hlasuj_ano)
canvas.bind_all('2', hlasuj_nie)
canvas.bind_all('3', hlasuj_neviem)

root.mainloop()
