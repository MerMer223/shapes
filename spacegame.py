import pgzrun
import random
import time
WIDTH = 1000
HEIGHT = 800


sats = []
next = 0

lines = []
satelitenum = 10
start = 0
total = 0
for i in range (satelitenum):
    satelite = Actor("satelite")
    satelite.x = random.randint(100,900)
    satelite.y = random.randint(100,700)
    sats.append(satelite)

start = time.time()
def draw():
    global start
    global total
    screen.blit("space",(0,0))
    num = 1
    if next < satelitenum:
        total = time.time()-start
    screen.draw.text(str(round(total,2)),(500,30))
    for i in sats:
        i.draw()
        screen.draw.text(str(num), (i.x, i.y - 25))
        num = num + 1 
    for j in lines:
        screen.draw.line(j[0],j[1],"white")
def on_mouse_down(pos):
    global satelitenum
    global next
    global lines
    if next < satelitenum:
        if sats[next].collidepoint(pos):
            if next:
                lines.append((sats[next-1].pos,sats[next].pos))
            next = next + 1
            print(lines)
        else:
                lines = []
                next = 0


def update():
    pass

pgzrun.go()