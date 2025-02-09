import pgzrun
WIDTH = 800
HEIGHT = 1000
titlebox = Rect((0,0),(800,100))
questionbox = Rect((20,120),(610,100))
option1 = Rect((20,240),(300,250))
option2 = Rect((330,240),(300,250))
option3 = Rect((20,500),(300,250))
option4 = Rect((330,500),(300,250))
skipbox = Rect((660,200),(100,100))
timerbox = Rect((660,400),(100,100))
resetbox = Rect((660,600),(100,100))
timeleft = 15
questions = []
answerboxes = [option1,option2,option3,option4]
game = False
score = 0
def draw():
    screen.fill("black")
    screen.draw.filled_rect(titlebox, "purple")
    screen.draw.textbox("Welcome To Quizmaster",titlebox,color = "black")
    screen.draw.filled_rect(questionbox, "purple")
    screen.draw.textbox(question[0].strip(),questionbox,color = "black")
    screen.draw.filled_rect(option1, "red")
    screen.draw.textbox(question[1].strip(),option1,color = "black")
    screen.draw.filled_rect(option2, "blue")
    screen.draw.textbox(question[2].strip(),option2,color = "black")
    screen.draw.filled_rect(option3, "yellow")
    screen.draw.textbox(question[3].strip(),option3,color = "black")
    screen.draw.filled_rect(option4, "green")
    screen.draw.textbox(question[4].strip(),option4,color = "black")
    screen.draw.filled_rect(skipbox, "darkgreen")
    screen.draw.textbox("Skip",skipbox,color = "black")
    screen.draw.filled_rect(timerbox, "orange")
    screen.draw.textbox(str(timeleft),timerbox,color = "black")
    screen.draw.filled_rect(resetbox,"darkred")
    screen.draw.textbox("Reset",resetbox,color = "black")



def update():
    titlebox.x -= 1
    if titlebox.right < 0:
        titlebox.left = WIDTH


def read_file():
    global questions
    file = open("questions.txt","r")
    for line in file:
        questions.append(line)

def read_question():
    return questions.pop(0).split("|")

read_file()
question = read_question()

def gameover():
    global timeleft,game
    global question
    question = ["Gameover",'-','-','-','-',5]
    timeleft = 0
    game = True


def update_time():
    global timeleft
    if timeleft:
        timeleft -=1
    else:
        gameover()

clock.schedule_interval(update_time,1)


def on_mouse_down(pos):
    global question,score,timeleft,questions,game
    index = 1
    for box in answerboxes:
        if box.collidepoint(pos): 
            if index is int(question[5]):
                score = score + 1
                if questions:
                    question = read_question()
                    timeleft = 15
                else:
                        question = [f"You score{score}",'-','-','-','-',0]
                        timeleft = 0
                        game = True
            else:    
                    gameover()
        index += 1

    if skipbox.collidepoint(pos):
        if questions:
            question = read_question()
            timeleft = 15
    if resetbox.collidepoint(pos):
        questions = []
        read_file()
        timeleft = 15 
        score = 0
        game = False  
        question = read_question()    






















pgzrun.go()