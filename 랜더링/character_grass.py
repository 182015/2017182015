
from pico2d import *

open_canvas()

grass=load_image('grass.png')
person=load_image('character.png')

grass.draw_now(400,30)
person.draw_now(400,90)

delay(5)

close_canvas()
