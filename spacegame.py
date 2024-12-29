import pgzrun
import random
WIDTH = 1000
HEIGHT = 800


sats = []
next = 0

lines = []
satelitenum = 10
for i in range (satelitenum):
    satelite = Actor("satelite")
    satelite.x = random.randint(100,900)
    satelite.y = random.randint(100,700)
    sats.append(satelite)


def draw():
    screen.blit("space",(0,0))
    num = 1
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


def update():
    pass

pgzrun.go()