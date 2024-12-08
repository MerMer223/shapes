import pgzrun
import random
WIDTH = 1000
HEIGHT = 800
pink_monster = Actor("pink monster")
pink_monster.x = 500
pink_monster.y = 600
def draw():
    screen.fill("black")
    pink_monster.draw()
def on_mouse_down(pos):
    print (pos)
    print(pink_monster.collidepoint(pos))
    if pink_monster.collidepoint(pos) == False:
        pink_monster.x = random.randint(0,900)
        pink_monster.y = random.randint(0,700)








pgzrun.go()