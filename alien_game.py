import pgzrun
import random
WIDTH = 1000
HEIGHT = 800
ufo_monster = Actor("ufo monster")
ufo_monster.x = 500
ufo_monster.y = 600
def draw():
    screen.fill("black")
    ufo_monster.draw()
    screen.draw.text("The alien dodged",(500,10),color = "white")
def on_mouse_down(pos):
    print (pos)
    print(ufo_monster.collidepoint(pos))
    if ufo_monster.collidepoint(pos) == True:
        ufo_monster.x = random.randint(0,900)
        ufo_monster.y = random.randint(0,700)








pgzrun.go()
