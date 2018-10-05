from pico2d import *

WIDTH,HEIGHT= 800,600

def handle_events():
    global running
    global x,y
    
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_MOUSEMOTION:# and e.key == SDL_MOUSEBUTTONDOWN:
            x,y=e.x,HEIGHT-1-e.y
        elif e.type == SDL_KEYDOWN and e.key ==SDLK_ESCAPE:
            running = False
            



open_canvas(WIDTH,HEIGHT)

grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x, y=50,40
frame =0
speed=5
while running:
    clear_canvas()
    grass.draw(400,30)
    delay(0.01*speed)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    delay(0.01)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)



close_canvas()
