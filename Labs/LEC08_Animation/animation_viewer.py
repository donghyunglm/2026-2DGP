from pathlib import Path

from pico2d import *

folder = Path(__file__).resolve().parent
open_canvas(800, 600)
character = load_image(str(folder / 'image_sheet.png'))
ground = load_image(str(folder / 'robot_ground.png'))

character_x = 400
character_width = 400
character_height = 400
ground_x = 400
ground_y = 31
character_y = ground_y + ground.h // 2 + character_height // 2
frame = 0
repeat_count = 0
action = 0
action_y = [300, 200, 100, 0]
frame_count = [8, 8, 6, 6]

running = True
while running:
	clear_canvas()
	ground.draw(ground_x, ground_y)
	character.clip_draw(frame * 100, action_y[action], 100, 100, character_x, character_y, character_width, character_height)
	update_canvas()
	frame = (frame + 1) % frame_count[action]
	if frame == 0:
		repeat_count += 1
		if repeat_count == 5:
			repeat_count = 0
			action = (action + 1) % len(action_y)
	delay(0.05)

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False
 
close_canvas()
