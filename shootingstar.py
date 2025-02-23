import pgzrun
import random
WIDTH = 800
HEIGHT = 800

shootingstar = Actor('shootingstar')
shootingstar.x = 400
shootingstar.y = 30
Level = 10
Threat = ["asteroid","comet"]
Gameover = False
Gamecomplete = False
Currentlevel = 1
Items = []
Animations = []



def draw():
    screen.blit("space",(0,0))
   # shootingstar.draw()
    if Gameover == True:
        screen.draw.text("You Lost",(400,400))
    elif Gamecomplete == True:
        screen.draw.text("You Win",(400,400))
    else:
        for Item in Items:
            Item.draw()

    

def update():
    global Items
   # animate(shootingstar,duration = 5,y=800)
    if len(Items) == 0:
        Items = MakeItems(Currentlevel)

def MakeItems(no_of_items):
    ItemsToCreate = randomitems(no_of_items)
    NewItems = CreateItems(ItemsToCreate)
    Layout(NewItems)
    Animate(Items)
    return NewItems



def on_mouse_down(pos):
   # if shootingstar.collidepoint(pos):
   pass





















pgzrun.go()