from pico2d import *
import random

speed = 3

class Grass:
	def __init__(self):
		self.image = load_image('grass.png')
		print(self.image)
	def draw(self):
		self.image.draw(400, 300)

class Boy:
	def __init__(self):
		print("Creating..")
		self.x = random.randint(0, 200)
		self.y = random.randint(90, 550)
		self.speed = random.uniform(1.0, 3.0)
		self.frame = random.randint(0, 7)
		self.image = load_image('run_animation.png')
	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.frame = (self.frame + 1) % 8
		self.x += self.speed

def handle_events():
	global running
	global waypoints
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT: 
			running = False
		elif e.type == SDL_KEYDOWN:
                    if e.key == SDLK_ESCAPE:
                        running = False
                elif e.type == SDL_MOUSEBUTTONDOWN:
                    if e.button == 1:
                        tx, ty = e.x, 600 - e.y
                        waypoints += [ (tx, ty) ]
                    else:
                        waypoints = []
		
open_canvas()

g = Grass()
# b = Boy()
# b2 = Boy()
# b2.y = 200

boys = [ Boy() for i in range(20) ]
# boys = []
# for i in range(20):
# 	boys += [ Boy() ]


# for b in boys:
# 	b.y = random.randint(90, 550)

running = True


while running:
	handle_events()

	for b in boys:
		b.update()
	# b.update()
	# b2.update()

	clear_canvas()
	g.draw()
	for b in boys:
		b.draw()
	# b.draw()
	# b2.draw()
	update_canvas()

	delay(0.03)


