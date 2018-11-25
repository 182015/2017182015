import random
import json
import os

from pico2d import *

import game_framework
import title_state

from plane import Plane
from grass import Grass
from enemy import Enemy


name = "MainState"

plane = None
grass = None
font = None
enemy = None


def enter():
    global plane, grass, enemy
    plane = Plane()
    grass = Grass()
    enemy = Enemy()


def exit():
    global plane, grass, enemy
    del plane
    del grass
    del enemy



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            plane.handle_event(event)



def update():
    plane.update()
    enemy.update()

def draw():
    clear_canvas()
    grass.draw()
    plane.draw()
    enemy.draw()
    update_canvas()






