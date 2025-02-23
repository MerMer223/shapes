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
startspeed = 12


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
    Animate(NewItems)
    return NewItems
def randomitems(no_of_items):
    ItemsToCreate = ["paperbag"]
    for i in range(no_of_items):
        name = random.choice(Nonrecycle)
        ItemsToCreate.append(name)
    return ItemsToCreate

def CreateItems(ItemsToCreate):
    NewItems = []
    for items in ItemsToCreate:
        item = Actor(items)
        NewItems.append(item)
    return NewItems

def Layout(NewItems):
    gap = len(NewItems) + 1
    gapsize = WIDTH/gap
    random.shuffle(NewItems)
    for index,item in enumerate(NewItems):
        x_pos = (index+1)*gapsize
        item.x=x_pos

def Animate(NewItems):
    global Animations
    global Currentlevel
    print(NewItems)
    for item in NewItems:
        item.anchor = ("center","bottom")
        dur = startspeed - Currentlevel
        Animation = animate(item,duration=dur,y=HEIGHT,on_finished=gameover)
        Animations.append(Animation)

def gameover():
    global Gameover
    Gameover = True


def on_mouse_down(pos):
   global Items,Currentlevel
   for item in Items:
        if item.collidepoint(pos):
            if item.image == "paperbag":
                Game_complete()
            else:
                gameover()
   
def Game_complete():
    global Currentlevel,Items,Animations,Gamecomplete
    for animation in Animations:
        if animation.running:
            animation.stop()
    if Currentlevel == Level:
        Gamecomplete = True
    else:
        Currentlevel = Currentlevel +1
        Items = []
        Animations = []



def shuffleitems():
    global Items
    if Items:
        Layout(Items)


clock.schedule_interval(shuffleitems,2)
















pgzrun.go()