import pgzrun
import random
import time
WIDTH = 512
HEIGHT = 544
ship = Actor("ship")
ship.x = 256
ship.y = 272
enimies = ["redenemy","greenenemy","greyenemy","blueenemy"]
enemies = []
timer = 0
game = True
attack = True
health = 3
charge = 3
explosions = []
frames = ["explosion1", "explosion2", "explosion3", "explosion4", "explosion5", "explosion6"]
def draw():
    screen.clear()
    global timer,health,charge,game
    screen.blit("map",(0,0))
    ship.draw()
    screen.draw.text(f"health {health}",(10,20),color = "black")
    screen.draw.text(f"charge {charge}",(80,20),color ="black")
    if health < 1:
        screen.draw.text("Gameover",(256,272),color = "red")
        game = False
    if charge == 100:
        screen.draw.text("You Win",(256,272),color = "green")
        game = False
    if game == True:
        for explosion in explosions:
            explosion.draw()
        timer = timer +1
        print(timer)
        if timer % 80 ==0:
            makeenemies()
            timer = 0
        for enemy in enemies:
            enemy.draw()
            animate(enemy,pos=ship.pos,angle = enemy.angle_to(ship.pos) -90,duration = 2)
            if enemy.colliderect(ship):
                if attack == True:
                    health = health - 1
                explosions.append(Actor("explosion1"))
                explosions[-1].pos=enemy.pos
                enemies.remove(enemy)
                charge = charge + 1
                
def update():
    pass

def attackend():
    global attack 
    attack = True


def on_mouse_down(pos):
    global attack,game
    if attack == True:
        attack = False
    if game == True:
        animate(ship,pos = pos,angle = ship.angle_to(pos)-90,duration = 1,on_finished = attackend)

    

def makeenemies():
    enemy = Actor("greenenemy")
    enemies.append(enemy)
    enemy.image = random.choice(enimies)
    if enemy.image == "greenenemy":
        enemy.x = 0
        enemy.y = 0
    elif enemy.image == "blueenemy":
        enemy.x = 512
        enemy.y = 0
    elif enemy.image == "redenemy":
        enemy.x = 0
        enemy.y = 544
    elif enemy.image == "greyenemy":
        enemy.x = 512
        enemy.y = 544


def updateexplosion():
    global explosions
    for explosion in explosions:
        if explosion.image == "explosion1":
            explosion.image = "explosion2"
        elif explosion.image == "explosion2":
            explosion.image = "explosion3"
        elif explosion.image == "explosion3":
            explosion.image = "explosion4"
        elif explosion.image == "explosion4":
            explosion.image = "explosion5"
        elif explosion.image == "explosion5":
            explosion.image = "explosion6"
        elif explosion.image == "explosion6":
            explosions.remove(explosion)
    clock.schedule(updateexplosion,0.1)


clock.schedule(updateexplosion,0.1)












pgzrun.go()