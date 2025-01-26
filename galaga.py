import pgzrun
HEIGHT = 800
WIDTH = 1000

direction = 1
sharkdead = False
score = 0
spacemonkeys = []
waterbullets = []
spaceshark = Actor("spaceshark")
spaceshark.x = 400
spaceshark.y = 700
waterbullet = Actor("waterbullet")
spacemonkey = Actor("spacemonkey")
def alienspawn():
    for x in range(5):
        for y in range(5):
            spacemonkey = Actor("spacemonkey")
            spacemonkey.x = 100+75*x
            spacemonkey.y = 100+75*y
            spacemonkeys.append(spacemonkey)
alienspawn()
def draw():
    screen.blit("space", (0,0))
    if sharkdead is False:
        spaceshark.draw()
        for i in waterbullets:
            i.draw()
    for j in spacemonkeys:
        j.draw()
    screen.draw.text(str(score),(500,50),color = "white")
    if score == 25:
        screen.draw.text("You Win!",(500,400),color = "green")
    if sharkdead == True:
        screen.draw.text("You Lose!",(500,400),color = "red")


def on_key_down(key):
    if key == keys.SPACE:
        waterbullet = Actor("waterbullet")
        waterbullet.x = spaceshark.x
        waterbullet.y = spaceshark.y - 10
        waterbullets.append(waterbullet)

def update():
    global sharkdead
    global score
    global direction
    if keyboard.right and spaceshark.x <= 950:
        spaceshark.x += 5
    elif keyboard.left and spaceshark.x >= 50:
        spaceshark.x -= 5
        """"
    if keyboard.space:
        bullet = Actor("bullet")
        bullet.x = spaceship.x
        bullet.y = spaceship.y - 10
        bullets.append(bullet)"""
    for i in waterbullets:
        i.y -= 5
    if len(spacemonkeys) >0:
        if spacemonkeys[0].x <50 or spacemonkeys[-1].x >WIDTH-50:  
            direction = direction * -1
    for j in spacemonkeys:
        j.x += 5 * direction
        j.y += 0.6
        for bullet in waterbullets:
            if j.colliderect(bullet):
                spacemonkeys.remove(j)
                waterbullets.remove(bullet)
                score = score + 1
        if spaceshark.colliderect(j):
            sharkdead = True










pgzrun.go()