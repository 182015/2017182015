from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('헤네필드1.png')

    def draw(self):
        self.image.draw(0, 300)
