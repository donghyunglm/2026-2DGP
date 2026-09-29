from pico2d import *
import math
open_canvas(800,600)

character = load_image('character.png')
# 실습 과제 진행
def draw_circle():
    for degree in range(0,360,5):
        rad = math.radians(degree)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        draw_character(x,y)
        pass

def draw_top():
    print('TOP')
    for x in range(50, 750, 5):
        draw_character(x,550)

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)

def draw_right():
    for y in range(550, 50, -5):
        draw_character(750, y)
    pass

def draw_bottom():
    for x in range(750, 50, -5):
        draw_character(x, 50)

def draw_left():
    for y in range(50, 550, 5):
        draw_character(50, y)


def draw_rectangle():
    print("rectangle")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def draw_line(x0, y0, x1, y1):
    n = 100  
    for step in range(n + 1):
        t = step / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_character(x, y)

def draw_triangle_bottom():
    print("triangle - bottom (A -> B)")
    draw_line(100, 100, 700, 100)

def draw_triangle_right_up():
    print("triangle - right up (B -> C)")
    draw_line(700, 100, 400, 500)
    
def draw_triangle_left_down():
    print("triangle - left down (C -> A)")
    draw_line(400, 500, 100, 100)

def draw_triangle():
    print("triangle")
    draw_triangle_bottom()
    draw_triangle_right_up()
    draw_triangle_left_down()
    pass

while True:
    #draw_circle()
    draw_rectangle()
    #draw_triangle()
    
    pass
close_canvas()