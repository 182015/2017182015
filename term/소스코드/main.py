from pico2d import *


def handle_events():
    global running
    global dir
    
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running == False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


open_canvas()
a = load_image('토끼run.png')
b = load_image('토끼runleft.png')
c = load_image('헤네필드1.png')



running = True
x = 400
frame = 0
dir = 0


while running:
    clear_canvas()
    c.draw(400,300)
    a.clip_draw(frame*100,0,100,100,x,90)
    
    update_canvas()
    
    handle_events()
    frame=(frame+1)%8
    x += dir * 5
    delay(0.05)

close_canvas()
