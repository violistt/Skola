import tkinter
import random

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

def obdlznik():
    global y, a, reverse, farba
    if (y == 450 and not reverse): # ak sa dostaneme na spodok platna a nas smer nie je hore
        reverse = True
        farba = 'white'
        canvas.create_rectangle(250 + a, y + 20, 250 - a, y - 20, fill = farba, outline = '')
    elif (y == 50 and reverse): # ak sa dostaneme na vrch platna a nas smer je hore
        reverse = False
        farba = 'black'
        canvas.create_rectangle(250 + a, y + 20, 250 - a, y - 20, fill = farba, outline = '')
    if (reverse):
        y -= 50; a -= 10
    else:
        y += 50; a += 10
    canvas.after(100, obdlznik)
    canvas.create_rectangle(250 + a, y + 20, 250 - a, y - 20, fill = farba, outline = '')

y = 50
a = 20
reverse = False
farba = 'black'
canvas.create_rectangle(250 + a, y + 20, 250 - a, y - 20, fill = farba, outline = '') # Zaciatocny obdlznik
obdlznik()
