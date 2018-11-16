from pico2d import *

class Grass:
    def __init__(self):
        self.x =400
        self.image = load_image('배경.png')
        
        
    def do(self):
        pass
        

    def draw(self):
        self.image.clip_draw(100, 0, 800, 600, self.x, 300)
            
          
    
            


    
