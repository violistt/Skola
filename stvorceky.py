import tkinter

canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(10, 50, 110, 100, width = 5, outline = 'yellow', fill = 'blue')
canvas.create_rectangle(110, 50, 210, 100, width = 5, outline = 'yellow', fill = 'blue')
canvas.create_rectangle(10, 100, 110, 150, width = 5, outline = 'yellow', fill = 'blue')
