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
action = 'walk'

running = True
while running:
	clear_canvas()
	ground.draw(ground_x, ground_y)
	if action == 'walk':
		action_y = 300
	elif action == 'run':
		action_y = 200
	character.clip_draw(frame * 100, action_y, 100, 100, character_x, character_y, character_width, character_height)
	update_canvas()
	frame = (frame + 1) % 8
	delay(0.05)

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_1:
				action = 'walk'
				frame = 0
			elif event.key == SDLK_2:
				action = 'run'
				frame = 0

close_canvas()
