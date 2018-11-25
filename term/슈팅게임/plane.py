from pico2d import *


# Boy Event
UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP,RIGHT_DOWN, LEFT_DOWN, RIGHT_UP,LEFT_UP, Z = range(9)

# fill here

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_z):Z
}



# Boy States
class IdleState:
    @staticmethod
    def enter(plane, event):
        if event == UP_DOWN:
            plane.ydir = +1
        elif event == DOWN_DOWN:
            plane.ydir = -1
        elif event == UP_UP:
            plane.ydir = 0
        elif event == DOWN_UP:
            plane.ydir = 0
        elif event == RIGHT_DOWN:
            plane.xdir = +1
        elif event == LEFT_DOWN:
            plane.xdir = -1
        elif event == RIGHT_UP:
            plane.xdir = 0
        elif event == LEFT_UP:
            plane.xdir = 0
        elif event == Z:
            plane.bullet_x = plane.x + 50
            plane.bullet_y = plane.y + 8
            plane.bullet_xy.append([plane.bullet_x,plane.bullet_y])
            

            
            
        plane.timer = 1000

    @staticmethod
    def exit(plane, event):
        pass

    @staticmethod
    def do(plane):
        #plane.frame = (plane.frame +1 )% 8
        #plane.timer -= 1
        plane.frame = (plane.frame + 1) % 5
        plane.y += plane.ydir
        plane.x += plane.xdir
        if(plane.y>550):
            plane.y=550
        elif (plane.y<50):
            plane.y=50
        #elif(plane.x>750):
         #   plane.x=750
        elif(plane.x<50):
            plane.x = 50

        if len(plane.bullet_xy)!= 0:
            for i, bxy in enumerate(plane.bullet_xy):
                bxy[0]+= 5
                plane.bullet_xy[i][0] = bxy[0]
                if bxy[0] >= 800:
                    plane.bullet_xy.remove(bxy)

        
                

    
    @staticmethod
    def draw(plane):
        plane.image.clip_draw(plane.frame * 100, 0, 100, 100, plane.x, plane.y)

        if len(plane.bullet_xy) != 0:
            for bx, by in plane.bullet_xy:
                plane.bullet.draw(bx,by)

        
# fill here
class RunState:
    @staticmethod
    def enter(plane, event):
        if event == UP_DOWN:
            plane.ydir = 1
        elif event == DOWN_DOWN:
            plane.ydir = -1
        elif event == UP_UP:
            plane.ydir = 0
        elif event == DOWN_UP:
            plane.ydir = 0
        elif event == RIGHT_DOWN:
            plane.xdir = +1
        elif event == LEFT_DOWN:
            plane.xdir = -1
        elif event == RIGHT_UP:
            plane.xdir = 0
        elif event == LEFT_UP:
            plane.xdir = 0
        elif event == Z:
            plane.bullet_x = plane.x + 50
            plane.bullet_y = plane.y +8
            plane.bullet_xy.append([plane.bullet_x,plane.bullet_y])
        #plane.dir = plane.velocity

    @staticmethod
    def exit(plane, event):
        pass

    @staticmethod
    def do(plane):
        #plane.frame = (plane.frame +1 )% 8
        #plane.timer -= 1
        #plane.x += plane.velocity
        #plane.x = clamp(25, plane.x, 800 - 25)
        plane.frame = (plane.frame + 1) % 5
        plane.y += plane.ydir
        plane.x += plane.xdir
        if(plane.y>550):
            plane.y=550
        elif (plane.y<50):
            plane.y=50
        #elif(plane.x>750):
         #   plane.x=750
        elif(plane.x<50):
            plane.x = 50

        if len(plane.bullet_xy)!= 0:
            for i, bxy in enumerate(plane.bullet_xy):
                bxy[0]+= 5
                plane.bullet_xy[i][0] = bxy[0]
                if bxy[0] >= 800:
                    plane.bullet_xy.remove(bxy)

    
    @staticmethod
    def draw(plane):
        plane.image.clip_draw(plane.frame * 100, 0, 100, 100, plane.x, plane.y)
        if len(plane.bullet_xy) != 0:
            for bx, by in plane.bullet_xy:
                plane.bullet.draw(bx,by)


next_state_table = {
    IdleState: {UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState,RIGHT_DOWN:RunState, LEFT_DOWN:RunState, RIGHT_UP:RunState,LEFT_UP:RunState, Z :RunState},
    RunState: {UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState,RIGHT_DOWN:IdleState, LEFT_DOWN:IdleState, RIGHT_UP:IdleState,LEFT_UP:IdleState, Z:IdleState}

}







class Plane:

    def __init__(self):
        self.x, self.y = 100, 300
        self.image = load_image('plane_animation.png')
        self.bullet = load_image('bullet.png')
        self.ydir = 0
        self.xdir = 0
        self.frame = 0
        self. timer =0
        self.frame=0
        self.event_que = []
        self.bullet_xy = []
        self.bullet_x = 0
        self.bullet_y = 0
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        # fill here
        pass

    def update_state(self):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    #def change_state(self,  state):



    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)




