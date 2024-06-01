from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()
ground = Entity(model = 'plane', scale = (50, 1, 50), color = color.white, texture = 'white cube', texture_scale = (50, 50), collider = 'box')

player = FirstPersonController(model = 'cube', collider = 'box', position = (0, 0, 0))

location = set()
for i in range(300):
    x = random.randrange(-24, 24, 2)
    y = 0
    z = random.randrange(-24, 24, 2)
    location.add((x, y ,z))

target_location = random.choice(list(location))
location.remove(target_location)
target = Entity(model = 'cube', scale = (2, 2, 1), color = color.gray, collider = 'box', position = target_location)

for loc in location:
    cube_width = 2
    cube_depth = 1
    cube_height = random.randrange(2, 8, 1)
    obstacle = Entity(model = 'cube', scale = [cube_width, cube_height, cube_depth], position = loc, texture = 'brick', color = color.yellow, collider = 'box')

def update():
    hit_info = player.intersects()
    if hit_info.hit:
        if hit_info.entity == target:
            message = Text(text = 'You lose', scale = 2, orgin = (0, 0), background = True, color = color.blue)
            application.pause()
            mouse.locked = False

countdown = 60
def timedown():
    global countdown
    count = Text(text = 'RUN' + str(countdown), orgin = (-2, -6), color = color.white)
    count.fade_out(0, 0.6)

    countdown -= 1

    seq = invoke(timedown, delay = 1)

    if countdown == -1:
        end = Text(text = 'You won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', scale = 2, orgin = (0, 0), background = True, color = color.violet)
        application.pause()
        mouse.locked = False
        seq.kill()

timedown()
app.run()