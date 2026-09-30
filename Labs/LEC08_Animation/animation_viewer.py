import json
from pathlib import Path
import sys

from pico2d import *

folder = Path(__file__).resolve().parent
image_sheet_path = folder / 'image_sheet.png'
trimmed_sheet_path = folder / 'image_sheet_trimmed.png'
frame_data_path = folder / 'image_sheet_trimmed.json'
ground_path = folder / 'robot_ground.png'
missing_files = []
if not image_sheet_path.is_file():
	missing_files.append(image_sheet_path)
if not trimmed_sheet_path.is_file():
	missing_files.append(trimmed_sheet_path)
if not frame_data_path.is_file():
	missing_files.append(frame_data_path)
if not ground_path.is_file():
	missing_files.append(ground_path)
if missing_files:
	for missing_file in missing_files:
		print(f'파일을 찾을 수 없습니다: {missing_file}')
	sys.exit(1)

with frame_data_path.open(encoding='utf-8') as frame_file:
	sprite_data = json.load(frame_file)
action_frames = [entry['frames'] for entry in sprite_data['actions']]

open_canvas(800, 600)
source_sheet = load_image(str(image_sheet_path))
if source_sheet.w != 800 or source_sheet.h != 400:
	print(f'image_sheet.png 크기 오류: 실제 {source_sheet.w}x{source_sheet.h}, 필요 800x400')
	close_canvas()
	sys.exit(1)

character = load_image(str(trimmed_sheet_path))
ground = load_image(str(ground_path))

character_x = 400
character_scale = 4
character_height = 100 * character_scale
ground_x = 400
ground_width = 800
ground_height = 62
ground_y = ground_height / 2
character_y = ground_y + ground_height / 2 + character_height / 2
frame = 0
repeat_count = 0
action = 0
action_name = ['걷기', '달리기', '점프', '공격']
frame_count = [len(frames) for frames in action_frames]
frame_interval = [0.10, 0.06, 0.12, 0.08]
previous_time = get_time()
paused = False
pause_start = 0

running = True
while running:
	current_time = get_time()
	if paused:
		if current_time - pause_start >= 1:
			paused = False
			action = (action + 1) % len(action_frames)
			print(f'다음 동작: {action_name[action]}')
			frame = 0
			repeat_count = 0
			previous_time = current_time
	elif current_time - previous_time >= frame_interval[action]:
		previous_time = current_time
		if frame == frame_count[action] - 1:
			repeat_count += 1
			print(f'{action_name[action]} 완료: {repeat_count}회')
			if repeat_count == 5:
				paused = True
				pause_start = current_time
				print(f'{action_name[action]} 정지 시작')
			else:
				frame = 0
		else:
			frame += 1

	clear_canvas()
	ground.draw(ground_x, ground_y, ground_width, ground_height)
	frame_data = action_frames[action][frame]
	character_draw_x = character_x + (frame_data['offset_x'] + frame_data['width'] / 2 - 50) * character_scale
	character_draw_y = character_y + (50 - frame_data['offset_y'] - frame_data['height'] / 2) * character_scale
	character.clip_draw(
		frame_data['x'], frame_data['y'], frame_data['width'], frame_data['height'],
		character_draw_x, character_draw_y,
		frame_data['width'] * character_scale, frame_data['height'] * character_scale,
	)
	update_canvas()

	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_r:
				action = 0
				frame = 0
				repeat_count = 0
				paused = False
				current_time = get_time()
				previous_time = current_time
				pause_start = current_time
	delay(0.001)
close_canvas()
