from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


def move_along_circle(center_x=400, center_y=300, radius=200):
    for degree in range(0, 360, 5):
        rad = math.radians(degree)
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.02)


def move_along_square(center_x=400, center_y=300, half_size=200):
    points = [
        (center_x, center_y + half_size),
        (center_x + half_size, center_y + half_size),
        (center_x + half_size, center_y - half_size),
        (center_x - half_size, center_y - half_size),
        (center_x - half_size, center_y + half_size),
        (center_x, center_y + half_size)
    ]

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        for step in range(30):
            t = step / 30
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t

            clear_canvas()
            character.draw(x, y)
            update_canvas()
            delay(0.02)


def move_along_triangle(center_x=400, center_y=300, radius=200):
    points = [
        (center_x, center_y + radius),
        (center_x + radius, center_y - radius * 0.5),
        (center_x - radius, center_y - radius * 0.5),
        (center_x, center_y + radius)
    ]

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        for step in range(30):
            t = step / 30
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t

            clear_canvas()
            character.draw(x, y)
            update_canvas()
            delay(0.02)


while True:
    move_along_circle()
    move_along_square()
    move_along_triangle()

close_canvas()
