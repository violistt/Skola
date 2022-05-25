import tkinter
import random
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

# Ak sme sa zeme dotkli zeme, nekreslime uz pavucinu a mozme sa posuvat len vlavo, vpravo

def posun_hore(suradnica):
    if (not na_zemi): # ak sme sa nedotkli zeme, mozme posuvat
        global y
        y -= 20
        canvas.delete('all')
        pavuk(suradnica)
        pavucina(suradnica)

def posun_dole(suradnica):
    global y, na_zemi
    if (not na_zemi): # Podobne ako pri posune hore
        y += 20
        # Musime skontrolovat ci sa pavuk svojim spodkom nedotkol zeme
        # Ak ano, uz nekreslime pavucinu a mozme sa hybat iba vlavo/vpravo
        if (y >= 450):
            na_zemi = True
        canvas.delete('all')
        pavuk(suradnica)
        if (not na_zemi): # moze sa nam stat, ze medzi tym sme sa uz zeme dotkli, kedze sme sa posunuli dole
            pavucina(suradnica)

def posun_vlavo(suradnica):
    global x
    x -= 20
    canvas.delete('all')
    pavuk(suradnica)
    if (not na_zemi):
        pavucina(suradnica)
    
def posun_vpravo(suradnica):
    global x
    x += 20
    canvas.delete('all')
    pavuk(suradnica)
    if (not na_zemi):
        pavucina(suradnica)

def pavuk(suradnica):
    canvas.create_oval(x + 50, y + 50, x - 50, y - 50)

def pavucina(suradnica):
    canvas.create_line(x, y - 50, 250, 20) # Ide zo stredu vrchu pavuka smerom hore
    
x, y = 250, 250
na_zemi = False
canvas.bind_all("<h>", posun_hore)
canvas.bind_all("<d>", posun_dole)
canvas.bind_all("<l>", posun_vlavo)
canvas.bind_all("<p>", posun_vpravo)
canvas.create_oval(x + 50, y + 50, x - 50, y - 50) # Nakreslime pavuka na zac. pozici
canvas.create_line(x, y - 50, 250, 20) # Zaciatocna pavucina
