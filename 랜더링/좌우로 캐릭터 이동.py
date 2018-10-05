from pico2d import *

def handle_events():
    global running
    global dir
    
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_RIGHT:
                dir += 1
            elif e.key == SDLK_LEFT:
                dir -= 1
            elif e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_RIGHT:
                dir -= 1
            elif e.key == SDLK_LEFT:
                dir += 1
            

#SDL_MOUSEMOTION

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0
x=800//2
dir = 0
running = True

while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir*20
    delay(0.05)

# fill here

close_canvas()
