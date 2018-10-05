from pico2d import *

class Grass:
    def _init_(self):
        self.image=load_image('grass.png')
        print(self.image)
    def draw(self):
        self.image.draw(400,300)

class Boy:
    def _init_(self):
        self.x,self.y=0,90
        self.frame=0
        self.image=load_image('run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame *100,0,10,100,self.x,self.y)
    def update(self):
        self.frame =(self.frame + 1) % 8
        self.x +=2


open_canvas()

g=Grass()
#b=Boy()
#b2=Boy()
#b2.y=200
running=True

while running:
    #handle_events()
    b.update()
    b2.update()

    clear_canvas()
    g.draw()
    b.draw()
    b2.draw()
    update_canvas()

    delay(0.03)
