import sys
import tkinter
input = sys.stdin.readline

root = tkinter.Tk()

canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

vyraz = input()[:-1]
# napr: (a+b)-((a-b)*2)
dlzka = len(vyraz)
lave, prave = 0, 0
ok = 1
stak = [] # zasobnik na ukladanie farieb pravych zatvoriek
farby = ['red', 'green', 'blue', 'orange', 'yellow', 'magenta', 'brown', 'gray']
f = 0
ofarbenie = ['black'] * dlzka
for i, clen in enumerate(vyraz):
    if (clen == '('):
        lave += 1
        ofarbenie[i] = farby[f]
        stak.append(f)
        f += 1
    elif (clen == ')'):
        prave += 1
        if (prave > lave):
            ok = 0
            break
        ofarbenie[i] = farby[stak[-1]]
        stak.pop()
ok &= (lave == prave) # Je rovnaky pocet pravych aj lavych?
if (not ok):
    canvas.create_text(200, 200, text = "Uzátvorkovanie nie je správne")
else:
    for i, clen in enumerate(vyraz):
        canvas.create_text((i * 10) + 200, 200, text = clen, fill = ofarbenie[i])
    canvas.create_text(280, 250, text = "Uzátvorkovanie je správne")
root.mainloop()
