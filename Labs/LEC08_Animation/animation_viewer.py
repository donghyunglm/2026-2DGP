from pico2d import *

open_canvas(800, 600)

running = True
while running:
	clear_canvas()
	update_canvas()

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False

close_canvas()
