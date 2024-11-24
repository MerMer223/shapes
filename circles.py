import pgzrun
import random
WIDTH = 500
HEIGHT = 500

def draw():
  screen.fill("white")
  size = 250
  for i in range (10):
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    size -= 20
    screen.draw.filled_circle((250,250),size,(r,g,b))




pgzrun.go()