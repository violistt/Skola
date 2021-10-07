import tkinter

canvas = tkinter.Canvas(width = 1000, height = 1000)
canvas.pack()
"""
canvas.create_rectangle(10, 50, 110, 100, width = 5, outline = 'red', fill = 'blue')
canvas.create_rectangle(110, 50, 210, 100, width = 5, outline = 'blue', fill = 'black')
canvas.create_rectangle(10, 100, 110, 150, width = 5, outline = 'blue', fill = 'red')
canvas.create_oval(100, 50, 200, 100, width = 5, fill = 'yellow')
"""
canvas.create_oval(400, 100, 600, 300, fill = '#FF9999')
canvas.create_oval(510, 170, 520, 180, width = 20)
canvas.create_oval(470, 170, 480, 180, width = 20)
canvas.create_line(470, 230, 520, 230, width = 10, fill = '#FF0000')
canvas.create_rectangle(400, 300, 600, 600, fill = 'red')
canvas.create_rectangle(300, 300, 400, 400, fill = 'green') # Lave rameno
canvas.create_rectangle(200, 300, 300, 500, fill = 'green') # Lava ruka
canvas.create_rectangle(600, 300, 700, 400, fill = 'green') # Prave rameno
canvas.create_rectangle(700, 300, 800, 500, fill = 'green') # Prava ruka
canvas.create_rectangle(400, 600, 480, 850, fill = 'blue')
canvas.create_rectangle(520, 600, 600, 850, fill = 'blue')
