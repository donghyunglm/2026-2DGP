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
    delay(0.1)

def draw_right():
    for y in range(550, 50, -5):
        draw_character(750, y)
    pass

def draw_left():
    print('LEFT')
    pass

def draw_bottom():
    print('BOTTOM')
    pass

def draw_rectangle():
    print("rectangle")
    #draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def draw_triangle():
    print("triangle")

    pass
while True:
    #draw_circle()
    draw_rectangle()
    draw_triangle()
    break
    pass

close_canvas()