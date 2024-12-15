import pgzrun
import random
WIDTH = 1000
HEIGHT = 800


bee = Actor("bee")
bee.x = random.randint(100,700)
bee.y = random.randint(100,700)
flower = Actor("flower")
flower.x = random.randint(100,700)
flower.y = random.randint(100,700)
score = 0
game = True
def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(str(score),(500,20), color = "black")
    if game == False:
        screen.blit("grass",(0,0))
        screen.draw.text("Game Over",(500,400), color = "red")
        screen.draw.text("Your Score Is "+str(score),(500,430), color = "black")

def update():
    global score
    if keyboard.up and bee.y >= 20:
        bee.y -= 5
    elif keyboard.down and bee.y <= 780:
        bee.y += 5
    elif keyboard.left and bee.x >= 20:
        bee.x -= 5
    elif keyboard.right and bee.x <= 980:
        bee.x += 5
    if bee.colliderect(flower):
        flower.x = random.randint(100,700)
        flower.y = random.randint(100,700)
        score = score + 1

def timer():
    global game
    game = False

clock.schedule(timer,60)


pgzrun.go()