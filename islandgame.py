import pgzrun
import random
WIDTH = 1000
HEIGHT = 800


islands = []
next = 0

lines = []
islandnum = 10
for i in range (islandnum):
    island = Actor("island")
    island.x = random.randint(100,900)
    island.y = random.randint(100,700)
    islands.append(island)


def draw():
    screen.blit("ocean",(0,0))
    num = 1
    for i in islands:
        i.draw()
        screen.draw.text(str(num), (i.x, i.y - 25))
        num = num + 1 
    for j in lines:
        screen.draw.line(j[0],j[1],"white")
def on_mouse_down(pos):
    global islandnum
    global next
    global lines
    if next < islandnum:
        if islands[next].collidepoint(pos):
            if next:
                lines.append((islands[next-1].pos,islands[next].pos))
            next = next + 1
            print(lines)


def update():
    pass

pgzrun.go()