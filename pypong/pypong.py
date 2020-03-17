from tkinter import *

desk_width, desk_height = 900, 300
pad_width, pad_height = 10, 100
ball_radius = 30

window = Tk()
window.title('PyPong')

desk_canvas = Canvas(window, width = desk_width,
                     height = desk_height, background = '#003300')

desk_canvas.pack()
desk_canvas.create_line(pad_width, 0, pad_width, desk_height, fill = 'white')
desk_canvas.create_line(desk_width - pad_width, 0, desk_width - pad_width,
                        desk_height, fill = 'white')

desk_canvas.create_line(desk_width / 2, 0, desk_width / 2,
                        desk_height, fill = 'white')

ball = desk_canvas.create_oval(desk_width / 2 - ball_radius / 2,
                               desk_height / 2 - ball_radius / 2,
                               desk_width / 2 + ball_radius / 2,
                               desk_height / 2 + ball_radius / 2, fill = 'white')

left_pad = desk_canvas.create_line(pad_width / 2, 0, pad_width / 2, pad_height,
                                   width = pad_width, fill = 'yellow')

right_pad = desk_canvas.create_line(desk_width - pad_width / 2, 0,
                                    desk_width - pad_width / 2, pad_height,
                                    width = pad_width, fill = 'yellow')

x_move, y_move = 20, 0

default_pad_speed = 20
left_pad_speed = 0
right_pad_speed = 0

def move_pads():
    pads = {left_pad: left_pad_speed,
            right_pad: right_pad_speed}
    for pad in pads:
        desk_canvas.move(pad, 0, pads[pad])
        if desk_canvas.coords(pad)[1] < 0:
            desk_canvas.move(pad, 0, - desk_canvas.coords(pad)[1])
        elif desk_canvas.coords(pad)[3] > height:
            desk_canvas.move(pad, 0, height - desk_canvas.coords(pad)[3])

def main():
     move_ball()
     move_pads()
     window.after(30, main)

desk_canvas.focus_set()

def movement_handler(event):
    global left_pad_speed, right_pad_speed
    if event.keysym == 'w':
        left_pad_speed = - default_pad_speed
    elif event.keysym == 's':
        left_pad_speed = default_pad_speed
    elif event.keysym == 'Up':
        right_pad_speed = - default_pad_speed
    elif event.keysym == 'Down':
        right_pad_speed = default_pad_speed

desk_canvas.bind('<KeyPress>', movement_handler)

def stop_pad(event):
    global left_pad_speed, right_pad_speed
    if event.keysym in 'ws':
        left_pad_speed = 0
    elif event.keysym in ('Up', 'Down'):
        right_pad_speed = 0

desk_canvas.bind('<KeyRelease>', stop_pad)

def move_ball():
    desk_canvas.move(ball, x_move, y_move)

main()

window.mainloop()
