from tkinter import *

width = 900
height = 300

pad_width = 10
pad_height = 100
ball_radius = 30

window = Tk()
window.title("PyPong")

c = Canvas(window, width = width, height = height, background = "#003300")
c.pack()

c.create_line(pad_width, 0, pad_width, height, fill = "white")
c.create_line(width - pad_width, 0, width - pad_width, height, fill = "white")
c.create_line(width / 2, 0, width / 2, height, fill = "white")

ball = c.create_oval(width / 2-ball_radius / 2,
                     height / 2 - ball_radius / 2,
                     width / 2 + ball_radius / 2,
                     height / 2 + ball_radius / 2, fill = "white")

left_pad = c.create_line(pad_width / 2, 0, pad_width / 2, pad_height, width = pad_width, fill = "yellow")
right_pad = c.create_line(width - pad_width / 2, 0, width - pad_width / 2, pad_height, width = pad_width, fill = "yellow")

window.mainloop()
