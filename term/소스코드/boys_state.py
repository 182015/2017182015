from pico2d import *
import game_framework
import random
from enum import Enum

open_canvas()
char=load_image('토끼run.png')

x=0
frame =0
while(x<800):
    clear_canvas()
    char.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    frame=(frame+1)%8
    x+=5
    delay(0.05)
    get_events()

close_canvas()
