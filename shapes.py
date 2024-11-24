import pgzrun
import random
WIDTH = 500
HEIGHT = 500


def draw():
  screen.fill("white")
  """"
  r1 = Rect((0,0),(50,100))
  r1.center = 250,250
  screen.draw.rect(r1,"Green")
  screen.draw.filled_rect(r1,"Green")
  r2 = Rect((0,0),(75,125))
  r2.center = 250,250
  screen.draw.rect(r2,"blue")
  r3 = Rect((0,0),(100,150))
  r3.center = 250,250
  screen.draw.rect(r3,"red")"""
  w = 100
  h = 275
  for i in range(10):
    r1 = Rect((0,0),(w,h))
    r1.center = 250,250
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    screen.draw.rect(r1,(r,g,b))
    w += 25
    h -= 25
  screen.draw.filled_circle((250,250),50,(0,0,0))
  screen.draw.line((100,100),(400,400),(255,0,255))

pgzrun.go()