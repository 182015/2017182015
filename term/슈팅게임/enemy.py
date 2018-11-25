from pico2d import *
import random


class Enemy:
    def __init__(self):
        global fires

        fires = []
        fires.append(load_image('새1.png'))
        fires.append(load_image('새2.png'))
        fires.append(load_image('새3.png'))
        fires.append(load_image('새4.png'))
        fires.append(load_image('새5.png'))
        fires.append(load_image('새6.png'))

            
        self.a = 2
        self.b = random.randint(800, 1200)

        self.eee1 = load_image('eee1.png')
        self.eee2 = load_image('eee2.png')
        
        self.ex = 800
        self.ey = random.randint(50, 550)
        
        self.fire_x = 800
        self.fire_y = random.randint(50, 550)
        self.fire_x1 = 800
        self.fire_y1 = random.randint(50, 550)
        self.fire_x2 = 800
        self.fire_y2 = random.randint(50, 550)
        random.shuffle(fires)
        self.fire = fires[0]
        self.fire1 = fires[1]
        self.fire2 = fires[2]

        
            

        
    def do(self):
        pass
    def update(self):
        global fires
        if self.fire == None:
            self.fire_x -= 3.5
            self.fire_x1 -=4
            self.fire_x2 -= 1
        else:
            self.fire_x -= 3.5
            self.fire_x1 -= 4
            self.fire_x2 -= 1
            
        if self.fire_x <=0:
            self.fire_x = 800
            self.fire_y = random.randint(50, 550)
            random.shuffle(fires)
            self.fire = fires[0]

        if self.fire_x1 <=0:
            self.fire_x1 = 800
            self.fire_y1 = random.randint(50, 550)
            random.shuffle(fires)
            self.fire1 = fires[1]

        if self.fire_x2 <=0:
            self.fire_x2 = 800
            self.fire_y2 = random.randint(50, 550)
            random.shuffle(fires)
            self.fire2 = fires[2]
            

        
        self.ex -= 2
        if(self.ex <=0):
            self.ex = 800
            self.ey = random.randint(50, 550)
        

        

    def draw(self):
        #random.shuffle(lulu)
        #lulu = lulu[0]
        self.eee1.draw(self.ex, self.ey)
        if (self.fire!= None):
            self.fire.draw(self.fire_x, self.fire_y)
            self.fire1.draw(self.fire_x1, self.fire_y1)
            self.fire2.draw(self.fire_x2, self.fire_y2)


    
