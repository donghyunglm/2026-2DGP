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
frame_interval = 0.05
previous_time = get_time()

running = True
while running:
	current_time = get_time()
	if current_time - previous_time >= frame_interval:
		previous_time = current_time
		frame = (frame + 1) % frame_count[action]
		if frame == 0:
			repeat_count += 1
			if repeat_count == 5:
				repeat_count = 0
				action = (action + 1) % len(action_y)

	clear_canvas()
	ground.draw(ground_x, ground_y)
	character.clip_draw(frame * 100, action_y[action], 100, 100, character_x, character_y, character_width, character_height)
	update_canvas()

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False
	delay(0.001)
close_canvas()
