from pico2d import *

class Grass:
    def __init__(self):
        self.image1 = load_image('배경1.png')
        self.image2 = load_image('배경2.png')
        self.x1 = 800//2
        self.x2 = 800 + 800/2
        self.number=0
        
    def do(self):
        pass
        

    def draw(self):
        self.x1 -= 1
        self.x2 -= 1
        if (self.x1 <= -800/2):
            self.x1 = 800 + 800/2
        elif (self.x2 <= -800 / 2):
            self.x2 = 800 + 800 / 2
        self.image1.clip_draw(0, 0, 800, 600, self.x1, 600/2)
        self.image2.clip_draw(0, 0, 800, 600, self.x2, 600/2)
        
            
          
    
            


    
