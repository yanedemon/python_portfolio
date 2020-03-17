from tkinter import *

desk_width, desk_height = 900, 300
pad_width, pad_height = 10, 100
ball_radius = 30

window = Tk()
window.title("PyPong")

desk_canvas = Canvas(window, width = desk_width,
                     height = desk_height, background = "#003300")

desk_canvas.pack()
desk_canvas.create_line(pad_width, 0, pad_width, desk_height, fill = "white")
desk_canvas.create_line(desk_width - pad_width, 0, desk_width - pad_width,
                        desk_height, fill = "white")

desk_canvas.create_line(desk_width / 2, 0, desk_width / 2,
                        desk_height, fill = "white")

ball = desk_canvas.create_oval(desk_width / 2 - ball_radius / 2,
                               desk_height / 2 - ball_radius / 2,
                               desk_width / 2 + ball_radius / 2,
                               desk_height / 2 + ball_radius / 2, fill = "white")

left_pad = desk_canvas.create_line(pad_width / 2, 0, pad_width / 2, pad_height,
                                   width = pad_width, fill = "yellow")

right_pad = desk_canvas.create_line(desk_width - pad_width / 2, 0,
                                    desk_width - pad_width / 2, pad_height,
                                    width = pad_width, fill = "yellow")

x_move, y_move = 20, 0

def move_ball():
    desk_canvas.move(ball, x_move, y_move)

def main():
    move_ball()
    window.after(30, main)
    
main()

window.mainloop()
