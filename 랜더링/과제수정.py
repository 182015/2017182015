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
		self.frame = random.randint(0, 7)
		self.image = load_image('run_animation.png')
	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.frame = (self.frame + 1) % 8
		self.x += speed
		
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

wp = load_image('wp.png')

x, y = 800 // 2, 90
# tx, ty = x, y
waypoints = []

g = Grass()
boys = [ Boy() for i in range(20) ]


frame = 0
running = True
while running:
    handle_events()
    for b in boys:
	    b.update()
	    
    clear_canvas()
    g.draw()
    for b in boys:
        b.draw()
    for loc in waypoints:
        wp.draw(loc[0], loc[1])
        
    update_canvas()
    
    if len(waypoints) > 0:
        (tx, ty) = waypoints[0]
        dx, dy = tx - b.x, ty - b.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            x += speed * dx / dist
            y += speed * dy / dist

            if dx < 0 and x < tx: x = tx
            if dx > 0 and x > tx: x = tx
            if dy < 0 and y < ty: y = ty
            if dy > 0 and y > ty: y = ty

        if (x,y) == (tx,ty):
            del waypoints[0]
            # hide_cursor()
        # else:
        #     show_cursor()
    
    delay(0.03)

# fill here
    
close_canvas()
