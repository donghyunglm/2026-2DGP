from pathlib import Path

from pico2d import *

folder = Path(__file__).resolve().parent
open_canvas(800, 600)
character = load_image(str(folder / 'image_sheet.png'))
ground = load_image(str(folder / 'robot_ground.png'))

running = True
while running:
	clear_canvas()
	ground.draw(400, 31)
	character.clip_draw(0, 300, 100, 100, 400, 300, 400, 400)
	update_canvas()
	delay(0.01)

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False

close_canvas()
