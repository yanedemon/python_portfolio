from tkinter import *
import random

desk_width, desk_height = 900, 300
pad_width, pad_height = 10, 100
ball_radius = 30
player_1_score, player_2_score = 0, 0
initial_speed = 20
ball_speed_up = 1.05
max_ball_speed = 40
x_speed = 20
y_speed = 20
right_line_distance = width - pad_width
x_move, y_move = 20, 0
default_pad_speed = 20
left_pad_speed = 0
right_pad_speed = 0

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

p_1_text = desk_canvas.create_text(width - width / 6, pad_height / 4,
                         text = player_1_score,
                         font = 'Arial 20',
                         fill = 'white')

p_2_text = desk_canvas.create_text(width / 6, pad_height / 4,
                          text = player_2_score,
                          font = 'Arial 20',
                          fill = 'white')

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

def bounce(action):
    global x_speed, y_speed
    if action == 'strike':
        y_speed = random.randrange(-10, 10)
        if abs(x_speed) < max_ball_speed:
            x_speed *= - ball_speed_up
        else:
            x_speed = - x_speed
    else:
        y_speed = - y_speed

def move_ball():
    ball_left, ball_top, ball_right, ball_bot = desk_canvas.coords(ball)
    ball_center = (ball_top + ball_bot) / 2
    if ball_right + x_speed < right_line_distance and \
            ball_left + x_speed > pad_width:
        desk_canvas.move(ball, x_speed, y_speed)
    elif ball_right == right_line_distance or ball_left == pad_width:
        if ball_right > wid / 2:
            if desk_canvas.coords(right_pad)[1] < ball_center < desk_canvas.coords(right_pad)[3]:
                bounce('strike')
            else:
                update_score('left')
                spawn_ball()
        else:
            if desk_canvas.coords(left_pad)[1] < ball_center < desk_canvas.coords(left_pad)[3]:
                bounce('strike')
            else:
                update_score('right')
                spawn_ball()
    else:
        if ball_right > width / 2:
            desk_canvas.move(ball, right_line_distance - ball_right, y_speed)
        else:
            desk_canvas.move(ball, - ball_left + pad_width, y_speed)
    if ball_top + y_speed < 0 or ball_bot + y_speed > height:
        bounce('ricochet')

def update_score(player):
    global player_1_score, player_2_score
    if player == 'right':
        player_1_score += 1
        c.itemconfig(p_1_text, text = player_1_score)
    else:
        player_2_score += 1
        c.itemconfig(p_2_text, text = player_2_score)

def spawn_ball():
    global x_speed
    c.coords(ball, width / 2 - ball_radius / 2,
             height / 2 - ball_radius / 2,
             width / 2 + ball_radius / 2,
             height / 2 + ball_radius / 2)
    x_speed = - (x_speed * - initial_speed) / abs(x_speed)

main()

window.mainloop()
