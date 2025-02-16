import pgzrun
import random
WIDTH = 800
HEIGHT = 800

paperbag = Actor('paperbag')
paperbag.x = 400
paperbag.y = 30
Level = 10
Nonrecycle = ["battery","plasticbag","chips","waterbottle"]
Gameover = False
Gamecomplete = False
Currentlevel = 1
Items = []
Animations = []



def draw():
    screen.blit("reusable",(0,0))
   # paperbag.draw()
    if Gameover == True:
        screen.draw.text("You Lost",(400,400))
    elif Gamecomplete == True:
        screen.draw.text("You Win",(400,400))
    else:
        for Item in Items:
            Item.draw()

    

def update():
    global Items
   # animate(paperbag,duration = 5,y=800)
    if len(Items) == 0:
        Items = MakeItems(Currentlevel)

def MakeItems(no_of_items):
    ItemsToCreate = randomitems(no_of_items)
    NewItems = CreateItems(ItemsToCreate)
    Layout(NewItems)
    Animate(Items)
    return NewItems



def on_mouse_down(pos):
   # if paperbag.collidepoint(pos):
   pass





















pgzrun.go()