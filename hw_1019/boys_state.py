from pico2d import *
import game_framework
import random
import json
# from enum import Enum

BOYS_COUNT = 1000

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400, 30)


# Boy State
IDLE, RUN = range(2)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}

next_state_table = {
    IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN:RUN,LEFT_DOWN: RUN},
    IDLE: {RIGHT_UP: IDLE, LEFT_UP: IDLE, LEFT_DOWN: IDLE, RIGHT_DOWN: IDLE },
    
}


class Boy:
    image = None
    wp = None
    RUN_LEFT, RUN_RIGHT, IDLE_LEFT, IDLE_RIGHT = 0, 1, 2, 3
    def __init__(self):
        print("Creating..")
        # self.state = self.State.s1
        self.event_que = []
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.waypoints = []
        self.state = Boy.IDLE_RIGHT
        self.cur_state = IDLE
        self.dir = 1
        self.velocity = 0
        self.enter_state[IDLE](self)
        if Boy.image == None:
            Boy.image = load_image('../res/animation_sheet.png')
        if Boy.wp == None:
            Boy.wp = load_image('../res/wp.png')
    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        self.frame = (self.frame +1)%8
        self.timer -= 1

    def draw_IDLE(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
    def enter_RUN(self):
        self.frame =0
        self.dir = self.velocity
      

    def exit_RUN(self):
        pass

    def do_RUN(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity
        self.x = clamp(25, self.x, 800-25)

    def draw_RUN(self):
        if self.velocity == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


    # SLEEP state functions
    def enter_SLEEP(self):
        print('Enter SLEEP')
        self.frame = 0

    def exit_SLEEP(self):
        print('Exit SLEEP')

    def do_SLEEP(self):
        self.frame = (self.frame + 1) % 8

    def draw_SLEEP(self):
        if self.dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x-25, self.y-25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x+25, self.y-25, 100, 100)


    def add_event(self, event):
        self.event_que.insert(0, event)


    def change_state(self,  state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state

     

    enter_state = {IDLE: enter_IDLE, RUN: enter_RUN}
    exit_state = {IDLE: exit_IDLE, RUN: exit_RUN}
    do_state = {IDLE: do_IDLE, RUN: do_RUN}
    draw_state = {IDLE: draw_IDLE, RUN: draw_RUN}
    





    def draw(self):
        self.draw_state[self.cur_state](self)
        for wp in self.waypoints:
            Boy.wp.draw(wp[0], wp[1])
        Boy.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
    def update(self):
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])
        self.frame = (self.frame + 1) % 8
        if len(self.waypoints) > 0:
            tx, ty = self.waypoints[0]
            dx, dy = tx - self.x, ty - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                if dx < 0 and self.x < tx: self.x = tx
                if dx > 0 and self.x > tx: self.x = tx
                if dy < 0 and self.y < ty: self.y = ty
                if dy > 0 and self.y > ty: self.y = ty

                if (tx, ty) == (self.x, self.y):
                    del self.waypoints[0]
                    self.determine_state()

    def determine_state(self):
        if len(self.waypoints) == 0:
            self.state = Boy.IDLE_RIGHT if self.state == Boy.RUN_RIGHT else  Boy.IDLE_LEFT
        else:
            tx,ty = self.waypoints[0]
            self.state = Boy.RUN_RIGHT if tx > self.x else Boy.RUN_LEFT


span = 50
def handle_events():
    global boys
    global span
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif e.key in range(SDLK_1, SDLK_9 + 1):
                span = 20 * (e.key - SDLK_0)

        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                tx, ty = e.x, 600 - e.y
                for b in boys:
                    bx = tx + random.randint(-span, span)
                    by = ty + random.randint(-span, span)
                    b.waypoints += [ (bx, by) ]
                    b.determine_state()
            else:
                for b in boys:
                    b.waypoints = []
                    b.determine_state()

def enter():
    global boys, grass

    boys = []
    fh = open('boys_data.json', 'r')
    data = json.load(fh)
    for e in data['boys']:
        b = Boy()
        b.name = e['name']
        b.x = e['x']
        b.y = e['y']
        b.speed = e['speed']
        boys.append(b)

    # boys = [ Boy() for i in range(BOYS_COUNT) ]
    grass = Grass()


# def main():
#     global running
#     enter()
#     while running:
#         handle_events()
#         print(running)
#         update()
#         draw()
#     exit()

def draw():
    global grass, boys
    clear_canvas()
    grass.draw()
    for b in boys:
        b.draw()
    update_canvas()

def update():
    global boys
    for b in boys:
        b.update()
    delay(0.01)

# fill here

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
