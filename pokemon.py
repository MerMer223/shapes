import pgzrun
import random
WIDTH = 1000
HEIGHT = 800


ash = Actor("ash")
ash.x = random.randint(100,700)
ash.y = random.randint(100,700)
pikachu = Actor("pikachu")
pikachu.x = random.randint(100,700)
pikachu.y = random.randint(100,700)
score = 0
game = True
def draw():
    screen.blit("field (2)",(0,0))
    ash.draw()
    pikachu.draw()
    screen.draw.text(str(score),(500,20), color = "black")
    if game == False:
        screen.blit("grass",(0,0))
        screen.draw.text("Game Over",(500,400), color = "red")
        screen.draw.text("Your Score Is "+str(score),(500,430), color = "black")

def update():
    global score
    if keyboard.up and ash.y >= 20:
        ash.y -= 5
    elif keyboard.down and ash.y <= 780:
        ash.y += 5
    elif keyboard.left and ash.x >= 20:
        ash.x -= 5
    elif keyboard.right and ash.x <= 980:
        ash.x += 5
    if ash.colliderect(pikachu):
        pikachu.x = random.randint(100,700)
        pikachu.y = random.randint(100,700)
        score = score + 1

def timer():
    global game
    game = False

clock.schedule(timer,60)


pgzrun.go()