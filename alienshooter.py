import pgzrun
HEIGHT = 800
WIDTH = 1000

aliens = []
bullets = []
spaceship = Actor("spaceship")
spaceship.x = 400
spaceship.y = 700
bullet = Actor("bullet")
alien = Actor("alien")
for x in range(5):
    for y in range(5):
        alien = Actor("alien")
        alien.x = 100+75*x
        alien.y = 100+75*y
        aliens.append(alien)
def draw():
    screen.blit("space", (0,0))
    spaceship.draw()
    for i in bullets:
        i.draw()
    for j in aliens:
        j.draw()

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = spaceship.x
        bullet.y = spaceship.y - 10
        bullets.append(bullet)

def update():
    if keyboard.right and spaceship.x <= 950:
        spaceship.x += 5
    elif keyboard.left and spaceship.x >= 50:
        spaceship.x -= 5
        """"
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.x = spaceship.x
        bullet.y = spaceship.y - 10
        bullets.append(bullet)"""
    for i in bullets:
        i.y -= 5
    for j in aliens:
        j.y += 1
        if j.x >= 950:
            j.x -=10
        elif j.x <= 100:
            j.x += 10
        
    







pgzrun.go()
