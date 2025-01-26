import pgzrun
HEIGHT = 800
WIDTH = 1000

direction = 1
shipdead = False
score = 0
aliens = []
bullets = []
spaceship = Actor("spaceship")
spaceship.x = 400
spaceship.y = 700
bullet = Actor("bullet")
alien = Actor("alien")
move = False
def alienspawn():
    for x in range(5):
        for y in range(5):
            alien = Actor("alien")
            alien.x = 100+75*x
            alien.y = 100+75*y
            aliens.append(alien)
alienspawn()
def draw():
    screen.blit("space", (0,0))
    if shipdead is False:
        spaceship.draw()
        for i in bullets:
            i.draw()
        for j in aliens:
            j.draw()
    screen.draw.text(str(score),(500,50),color = "white")
    if score == 500:
        screen.draw.text("You Win!",(500,400),color = "green")
    if shipdead == True:
        screen.draw.text("You Lose!",(500,400),color = "red")


def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = spaceship.x
        bullet.y = spaceship.y - 10
        bullets.append(bullet)

def update():
    global shipdead
    global move
    global aliens
    global score
    global direction
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
    if len(aliens) >0:
        if aliens[0].x <50 or aliens[-1].x >WIDTH-50:  
            direction = direction * -1
            move = True
    for j in aliens:
        j.x += 5 * direction
        if move == True:
            j.y += 0.7
            if j.y >= 800:
                shipdead = True
        for bullet in bullets:
            if bullet.colliderect(j):
                aliens.remove(j)
                bullets.remove(bullet)
                score = score + 1
                if len(aliens) == 0:
                    alienspawn()
        if spaceship.colliderect(j):
            shipdead = True


    
            
        
    







pgzrun.go()
