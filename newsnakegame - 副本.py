from tkinter import *
from tkinter import messagebox
import random
import os
import pickle

#   All images come from "https://www.kenney.nl/assets"
 #   Created/distributed by Kenney (www.kenney.nl)
  #  License: (Creative Commons Zero, CC0)
   # http://creativecommons.org/publicdomain/zero/1.0/
if os.stat("names.txt").st_size != 0: # Check the last number of the leaderboard ranking
    file = open("names.txt")
    for line in file:
        pass
    lastline = line
    number = int(lastline[0])
    file.close()
else: 
    number = 0
width = 2047           #game window structures
height = 1279
eleXspeed = 2             #animal initial speed
eleYspeed = 2
MonXspeed = 5
MonYspeed = 7
SXspeed = 10
SYspeed = 10
snakeMovement = 1           #decide if the snake can move
direction = "down"        # initial direction for snake             
cheat = 0                 #cheat status

def Load():   #load game
    global snakeCoords,eleCoords,monkeyCoords,RabbitCoords,PenguinCoords
    with open("save.pickle","rb") as loadfile:
            a = pickle.load(loadfile)
    snakeCoords,eleCoords,monkeyCoords,RabbitCoords,PenguinCoords,score,elex,eley,mox,moy,sx,sy,dr = a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12]
    loadfile.close()
    return snakeCoords,eleCoords,monkeyCoords,RabbitCoords,PenguinCoords,score,elex,eley,mox,moy,sx,sy,dr

def saveGame(): #save game
    global snakeCoords,eleCoords,monkeyCoords,RabbitCoords,PenguinCoords,SXspeed,SYspeed,direction
    eleXspeed = 2
    eleYspeed = 2
    MonXspeed = 5
    MonYspeed = 7
    a = [
        snakeCoords,
        eleCoords,
        monkeyCoords,
        RabbitCoords,
        PenguinCoords,
        score,
        eleXspeed,
        eleYspeed,
        MonXspeed,
        MonYspeed,
        SXspeed,
        SYspeed,
        direction

    ]
    with open("save.pickle","wb") as savefile:
        pickle.dump(a,savefile,protocol=pickle.HIGHEST_PROTOCOL)
    savefile.close()

def clearRecords(): #clear records from leaderboard
    file = open("names.txt","r+")
    file.truncate()
    file.close()
    top10.delete("score")
def leaderGoBackButton(window): #go back to main menu
    gobacktoMenu(window)
def leaderBoard(window): # leader board page
    global top10,a,b,c
    leadFile = open("names.txt")
    window.destroy()
    top10 = Canvas(root,width=gamewidth,height=gameheight,bg="#a4ebe7")
    top10.pack()
    top10.create_text(gamewidth/2,gameheight/6,fill="Black",font="Times 50 italic bold", text="Leader Board")
    top10.create_text(gamewidth*0.25,gameheight*0.25, text="Rankings",font="Times 30 bold",fill="black",anchor=N)
    top10.create_text(gamewidth*0.5,gameheight*0.25,text="Names",font="Times 30 bold",fill="black",anchor=N)
    top10.create_text(gamewidth*0.75,gameheight*0.25,text="Scores",font="Times 30 bold",fill="black",anchor=N)
    goBack = Button(top10,text="Go Back",font="Times 20 bold",bg="grey",command=lambda:leaderGoBackButton(top10),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star").place(relx=0.8,rely=0.8, anchor=SE)
    clear = Button(top10,text="Clear Records",font="Times 20 bold",bg="grey",command=clearRecords,background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star").place(relx=0.2,rely=0.8, anchor=SE)

    if os.stat("names.txt").st_size != 0:
        for line in leadFile:
            line = line.rstrip("\n")
            line = line.split(":")
            top10.create_text(gamewidth*0.25,gameheight*0.32+gameheight*0.32*(int(line[0])/10), text=str(line[0]),font="Times 30 bold",fill="black",anchor=N,tags=("score"))
            top10.create_text(gamewidth*0.5,gameheight*0.32+gameheight*0.32*(int(line[0])/10),text=str(line[1]),font="Times 30 bold",fill="black",anchor=N,tags=("score"))
            top10.create_text(gamewidth*0.75,gameheight*0.32+gameheight*0.32*(int(line[0])/10),text=str(line[2]),font="Times 30 bold",fill="black",anchor=N,tags=("score"))
        leadFile.close()

def rank(): #sequece ranks
    r = []
    file = open("names.txt","r")
    for line in file:
        line = line.rstrip()
        t = line.split(":")
        t[2] = int(t[2])
        t = tuple(t)
        r.append(t)

    sorted_by_third = sorted(r, key=lambda tup: tup[int(2)],reverse=True)

    file.close
    file = open("names.txt","w")
    t = []
    for i in sorted_by_third:
        listi = list(i)
        t.append(listi)
    for n in range(len(t)):
        string = ""
        t[n][0] = n+1
        string = ":".join(str(e) for e in t[n])
        file.write(string+"\n")
    file.close()

def cheatkeyRemove(e): #Reset cheat status to none
    global cheat
    cheat = 0
    root.bind("c",cheatKey)
def cheatKey(e): #Start cheating
    global cheat
    cheat = 1
    root.bind("c",cheatkeyRemove)
def username(): #let the users input their names into the leaderboard
    global number
    if os.stat("names.txt").st_size != 0:
        number += 1
    else:
        number = 1

    def submit():
        global name
        name = entry.get()
        nameFile = open("names.txt","a")
        nameFile.write(str(number)+":"+name+":"+str(score)+"\n")
        entryWindow.destroy()
        nameFile.close()
        rank()

    entryWindow = Toplevel()

    snakeD = PhotoImage(file="snakeD.png")

    entryWindow.title("Please Enter Your Name")
    entryWindow.geometry("500x450+800+450")
    entryWindow.configure(bg="#b09dd1")

    entryFrame = Frame(entryWindow,relief=SUNKEN,bg="#b09dd1")
    entryFrame.pack()

    imageButton = Button(entryWindow,image=snakeD,bg="#b09dd1",activebackground="#622fba",command=submit)
    imageButton.pack()
    label = Label(entryFrame,text="Enter your name",font=("Arial italic",25),bg="#b09dd1")
    label.pack(ipadx=10,ipady=10)
    entry = Entry(entryFrame,font=("Arial",25))
    entry.pack(side=TOP)
    entryWindow.mainloop()

def BossLeft(e): #When boss left, continue the game
    global eleYspeed,eleXspeed,MonXspeed,MonYspeed,SXspeed,SYspeed,snakeMovement,canvas,boss,bossimage
    eleXspeed = 2
    eleYspeed = 2
    MonXspeed = 5
    MonYspeed = 7
    snakeMovement = 1
    canvas.delete(bossimage)
    root.bind("<Return>",BossKey)
def BossKey(e): #make your boss feel that you are working
    global snakeD,eleYspeed,eleXspeed,MonXspeed,MonYspeed,SXspeed,SYspeed,snakeMovement,canvas,boss,bossimage
    snakeMovement = 0
    eleXspeed = 0
    eleYspeed = 0
    MonXspeed = 0
    MonYspeed = 0
    bossimage = canvas.create_image(gamewidth//2,gameheight//2,image=boss)
    root.bind("<Return>",BossLeft)
def MovePenguin(): # change the position of the Penguin
    global PenG,penX,penY
    canvas.move(PenG,(penX*(-1)), (penY*(-1)))
    penX = random.randint(400,gamewidth-400)
    penY = random.randint(250,gameheight-250)
    canvas.move(PenG,penX,penY)
def speedUP(): #increase the speed of the snake
    global SXspeed, SYspeed
    SXspeed+=5
    SYspeed+=5
def MoveEle(): #change the position of Elephant
    global Elephant,eleX,eleY
    canvas.coords(Elephant,(eleX*(-1)), (eleY*(-1)))
    eleX = random.randint(400,gamewidth-400)
    eleY = random.randint(250,gameheight-250)
    canvas.coords(Elephant,eleX,eleY)
def slowDown(): #decrease the speed of the snake
     global SXspeed, SYspeed
     if SXspeed and SYspeed > 10:
         SXspeed -=5
         SYspeed -=5

def MoveRabbit(): #change of position of the rabbit
    global Rabbit,RabX,RabY
    canvas.move(Rabbit,(RabX*(-1)), (RabY*(-1)))
    RabX = random.randint(10,gamewidth)
    RabY = random.randint(10,gameheight)
    canvas.move(Rabbit,RabX,RabY)

def collision(item,a,b): # define if two object collide and move the item
    global gameover
    if "gameover" not in locals():
        if a[0] < b[2] < a[2] and a[1] < b[1] < a[3]:
            canvas.move(item,30,30)
        elif a[2] > b[0] > a[0] and a[3] > b[3] > a[1]:
            canvas.move(item,-30,-30)
    else:
        pass
def overlapping(a,b): #define if two objects touch each other
    global gameover
    # if  a[0] < b[2] < a[2] and a[1] < b[1] < a[3] or a[2] > b[0] > a[0] and a[3] > b[3] > a[1]:
    #     return True
    if "gameover" not in locals():
        if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
            return True
        return False

def moveelephant(): #move the elephant 
    global motion,eleXspeed,eleYspeed
    def elephantmove():
        global eleXspeed,eleYspeed,motion

        canvas.move(Elephant, eleXspeed,eleYspeed)
    
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(Elephant)

        if leftPos <= 0 or rightPos >= gamewidth:
            eleXspeed = -eleXspeed
        if topPos <= 0 or bottomPos >= gameheight:
            eleYspeed = -eleYspeed
        if motion != 1:    
            root.after(10,elephantmove) 
    if motion != 1:        
        root.after(10,elephantmove)

def movemonkey():#move the monkey
    global motion,MonXspeed,MonYspeed
    def monkeymove():
        global MonXspeed,MonYspeed,motion


        canvas.move(Monkey, MonXspeed,MonYspeed)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(Monkey)

        if leftPos <= 0 or rightPos >= gamewidth:
            MonXspeed = -MonXspeed
        if topPos <= 0 or bottomPos >= gameheight:
            MonYspeed = -MonYspeed
        if motion != 1:
            root.after(8,monkeymove)
    if motion != 1:
        root.after(8,monkeymove)

def moveSnake():#move the snake and end the game if get killed
    global newimage,SXspeed,SYspeed,cheat,menuCV,snakeCoords,eleCoords,monkeyCoords,RabbitCoords,PenguinCoords,score
    if snakeMovement == 1:
        if direction == "right":
            canvas.move(image, SXspeed,0)
        elif direction == "left":
            canvas.move(image, -SXspeed,0)
        elif direction == "up":
            canvas.move(image, 0, -SXspeed)
        elif direction == "down":
            canvas.move(image, 0,SXspeed)
    else:
        canvas.move(image,0,0)
    if "gameover" not in locals():
        snakeCoords = canvas.bbox(image)
        eleCoords = canvas.bbox(Elephant)
        monkeyCoords =canvas.bbox(Monkey)
        RabbitCoords = canvas.bbox(Rabbit)
        PenguinCoords = canvas.bbox(PenG)

    if  overlapping(snakeCoords, RabbitCoords):
        MoveRabbit()
        slowDown()
        Score(10)
    if  overlapping(snakeCoords, PenguinCoords):
        MovePenguin()
        speedUP()
        Score(50)
    if cheat != 1:
        collision(image,snakeCoords,monkeyCoords)
        if "gameover" not in locals():
            if overlapping(snakeCoords, eleCoords):
                gameover = True
                endGame(canvas)
                username()
            (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(image)

            if leftPos <= 0 or rightPos >= gamewidth:
                gameover = True          

                endGame(canvas)
                username()
            if topPos <= 0 or bottomPos >= gameheight:
                gameover = True        
                endGame(canvas)
                username()
    elif cheat == 1:
        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(image)
        if leftPos < 0:
            canvas.coords(image,gamewidth-(rightPos-leftPos),topPos)
        if topPos < 0:
            canvas.coords(image,leftPos,gameheight-(bottomPos-topPos))
        if rightPos > gamewidth:
            canvas.coords(image,0,topPos)
        if bottomPos > gameheight:
            canvas.coords(image,leftPos,0)
        if overlapping(snakeCoords, eleCoords):
            MoveEle()
            Score(100)
    if "gameover" not in locals() and motion != 1:
        root.after(25, moveSnake)

def newimage(image): # change the image of the snake
    global coords
    image = canvas.create_image(coords[0],coords[1],anchor=NW,image=image)
    return image
def left(e): #left key bind event
    global direction,coords,image,gameover
    coords = canvas.coords(image)
    canvas.delete(image)
    image = newimage(snakeL)
    coords = []
    direction = "left"
    return image
def right(e):#right key bind event
    global direction,coords,image,gameover
    coords = canvas.coords(image)
    canvas.delete(image)
    image = newimage(snakeR)
    coords = []
    direction = "right"
    return image
def up(e):  #up key bind event
    global direction,coords,image,gameover
    coords = canvas.coords(image)
    canvas.delete(image)
    image = newimage(snakeU)
    coords = []
    direction = "up"
    return image
def down(e): #down key bind event
    global direction,coords,image,gameover
    coords = canvas.coords(image)
    canvas.delete(image)
    image = newimage(snakeD)
    coords = []
    direction = "down"
    return image
def Score(s): #change the display score value 
    global score
    score+=s
    txt = "Score: " + str(score)
    canvas.itemconfigure(scoreText,text=txt)
def esc(e): # <Escape> button bind event, stop the game and go to stop Menu
    stopMenu()
def ContinueGame(): # Game continue
    global eleYspeed,eleXspeed,MonXspeed,MonYspeed,SXspeed,SYspeed,snakeMovement,stopmenu
    root.bind("<Escape>",esc)
    canvas.pack()
    snakeMovement = 1
    eleXspeed = 2
    eleYspeed = 2
    MonXspeed = 5
    MonYspeed = 7
    stopmenu.destroy()

def quitGame(root): #Quit the game
    # str = ""
    # openfile = open('save.pickle', 'wb')
    # pickle.dump(str, openfile)
    # openfile.close()

    root.destroy()
def stopMenu(): # Menu displayed when game stops
    global eleYspeed,eleXspeed,MonXspeed,MonYspeed,SXspeed,SYspeed,snakeMovement,stopmenu,canvas
    root.unbind("<Escape>")
    canvas.pack_forget()
    snakeMovement = 0


    eleXspeed = 0
    eleYspeed = 0
    MonXspeed = 0
    MonYspeed = 0
    stopmenu = Canvas(root,width=gamewidth,height=gameheight,bg="#eda4d1")
    stopmenu.place(x=(gamewidth//2),y=(gameheight//2))
    stopmenu.pack()
    continueB = Button(stopmenu, text = "Continue", font=("Times",25),width=8,command=ContinueGame,background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    saveB = Button(stopmenu, text = "Save", font=("Times",25),width=8,command=saveGame,background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    quitB = Button(stopmenu, text = "Quit", font=("Times",25),width=8,command=lambda:gobacktoMenu(stopmenu),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    
    continueB.place(relx=0.5,rely=0.4,anchor=CENTER)
    saveB.place(relx=0.5,rely=0.5,anchor=CENTER)
    quitB.place(relx=0.5,rely=0.6,anchor=CENTER)

def MainMenu(): # Main Menu of the Game
    global mainWindow,menuCV,root,gamewidth,gameheight,boss
    root = Tk()
    root.title("Brank New Snake Game")
    root.iconphoto(True,PhotoImage(file="snakeD.png"))
    boss = PhotoImage(file="bossImage.png")
    ws = root.winfo_screenwidth() #computers screen size
    hs = root.winfo_screenheight()
    x = str((ws//2)-(width//2))
    y = str((hs//2)-(height//2))
    root.bind("<Return>",BossKey)
    root.geometry(str(ws)+"x"+str(hs))
    root.attributes("-fullscreen", True)
    root.configure(cursor="plus")
    if ws != width or hs != height:
        message = 'Warning: Your screen resolution is ' + str(ws) + 'x' + str(hs) + ', which is not the recommended resolution ' + str(width) + 'x' + str(height) +  ' and your gaming experience may be affected. ' + 'Do you still want to play in full screen?'
        ans = messagebox.askquestion(title="Bad Resolution", message=message)
        if ans == 'no':
            root.attributes("-fullscreen", False)
            root.geometry(str(width)+"x"+str(height)+"+"+x+"+"+y)
            menuCV = Canvas(root, width = width, height = height, highlightthickness=10, highlightbackground="#f20c18",background="#cdebb2")
            menuCV.pack(fill="both",expand=True)
            gamewidth,gameheight = width,height
            menuCV.create_text(
            gamewidth//2,
            gameheight//4.5,
            anchor='center',
            text='Welcome to Hunter Mr. Snake',
            font="Times 50 bold",
            fill='black',
            activefill='red')
            MenuButtons(menuCV)
        else:
            gamewidth,gameheight =ws,hs
            menuCV = Canvas(root,width=gamewidth,height=gameheight,highlightthickness=10, highlightbackground="#f20c18",background="#cdebb2")
            menuCV.pack(fill = "both", expand = True)
            menuCV.create_text(
            gamewidth//2,
            gameheight//4.5,
            anchor='center',
            text='Welcome to Hunter Mr. Snake',
            font="Times 50 bold",
            fill='black',
            activefill='red')
            MenuButtons(menuCV)
    root.mainloop()

def gobacktoMenu(window): #Go back to the main Menu
    global gamewidth,gameheight,menuCV,motion
    motion = 1
    #canvas.quit()
    #canvas.pack_forget
    window.destroy()
    menuCV = Canvas(root,width=gamewidth,height=gameheight,highlightthickness=10, highlightbackground="#f20c18",background="#cdebb2")
    menuCV.create_text(
            gamewidth//2,
            gameheight//4.5,
            anchor='center',
            text='Welcome to Hunter Mr. Snake',
            font="Times 50 bold",
            fill='black',
            activefill='red')
    menuCV.focus_force()
    menuCV.pack()
    MenuButtons(menuCV)
    
def MenuButtons(menuCV): # Button displayed on the Main Menu
    global boss
    start = Button(menuCV,text="New Game",font=("Times 20 bold"),width=8,command=lambda:createWindow(menuCV),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    leader = Button(menuCV,text="Top 10",bg="yellow",font=("Times 20 bold"),width=8,command=lambda:leaderBoard(menuCV),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    load = Button(menuCV,text="Load",bg="yellow",font=("Times 20 bold"),width=8,command=lambda:createWindow(menuCV),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    quit = Button(menuCV,text="Quit",bg="yellow",font=("Times 20 bold"),width=8,command=lambda:quitGame(root),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    start.place(relx=0.5,rely=0.4,anchor=CENTER)
    leader.place(relx=0.5,rely=0.5,anchor=CENTER)
    load.place(relx=0.5,rely=0.6,anchor=CENTER)
    quit.place(relx=0.5,rely=0.7,anchor=CENTER)
    with open("save.pickle","rb") as f:
        b = pickle.load(f)
    if not isinstance(b,list):
        load.configure(state=DISABLED)

def endGame(window): # after game ends, the endgame menu will be displayed
    global  root,direction
    direction = "down"
    # canvas.destroy()
    window.destroy()
    endgame = Canvas(root,width = gamewidth, height = gameheight,highlightthickness=10, highlightbackground="#f20c18",background="black")
    endgame.pack()
    endgame.focus_force()
    again_button = Button(endgame,text="Start Again",font="Times 20 bold",width=10,command=lambda:createWindow(endgame),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    quit_button = Button(endgame,text="Quit",font="Times 20 bold",width=10,command=lambda:quitGame(root),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    backToMenu = Button(endgame,text="Back To Menu",font="Times 20 bold",width=10,command=lambda:gobacktoMenu(endgame),background='#e5eb3b',
            activebackground='lightblue',
            foreground='black',
            cursor="star")
    endgame.create_text(gamewidth/2,gameheight/4,fill="white",font="Times 50 italic bold", text="Game Over!")
    again_button.place(relx=0.5,rely=0.4,anchor=CENTER)
    backToMenu.place(relx=0.5,rely=0.5,anchor=CENTER)
    quit_button.place(relx=0.5,rely=0.6,anchor=CENTER)

def createWindow(window): # Start the game
    global canvas, gameheight,gamewidth,root,ws,hs,snakeD,snakeL,snakeR,snakeU,x,y,image,Elephant,Monkey,Rabbit,scoreText,score,RabX,RabY,menuCV,root,eleXspeed,eleYspeed,MonXspeed,MonYspeed,SXspeed,SYspeed,snakeMovement,PenG,penX,penY,boss,direction,eleX,eleY,MonX,MonY,cheat,motion,elephant,rabbit,monkey,penguin
    motion = 0
    window.destroy()
    snakeMovement = 1
    SXspeed = 10
    SYspeed = 10
    eleXspeed = 2
    eleYspeed = 2
    MonXspeed = 5
    MonYspeed = 7
    cheat =  0
    direction = "down"
    root.focus_force()
    root.bind("<Left>",left)
    root.bind("<Right>",right)
    root.bind("<Up>", up)
    root.bind("<Down>", down)
    root.bind("<Escape>", esc)
    root.bind("c",cheatKey)
    ws = root.winfo_screenwidth() #computers screen size
    hs = root.winfo_screenheight()
    x = str((ws//2)-(gamewidth//2))
    y = str((hs//2)-(gameheight//2))

    canvas = Canvas(root, width = gamewidth, height = gameheight, highlightthickness=10, highlightbackground="#f20c18",background="#37d4a5")
    canvas.pack()

    snakeD = PhotoImage(file="snakeD.png").subsample(3)
    snakeL = PhotoImage(file="snakeL.png").subsample(3)
    snakeR = PhotoImage(file="snakeR.png").subsample(3)
    snakeU = PhotoImage(file="snakeU.png").subsample(3)
    elephant = PhotoImage(file="elephant.png").subsample(2)
    rabbit = PhotoImage(file="rabbit.png").subsample(4)
    monkey = PhotoImage(file="monkey.png").subsample(3)
    penguin = PhotoImage(file="penguin.png").subsample(3)
    # image = canvas.create_image(40,40, anchor=NW, image=snakeD)
    ###
    penX = random.randint(200,gamewidth-100)
    penY = random.randint(200,gameheight-100)
    #PenG = canvas.create_image(penX,penY,image=penguin)
    ###Create Elephant###
    eleX = random.randint(200,gamewidth-100)
    eleY = random.randint(200,gameheight-100)
    #Elephant = canvas.create_image(eleX,eleY,image=elephant)

    ###Create Monkey###
    MonX = random.randint(50,gamewidth-50)
    MonY = random.randint(50,gameheight-50)
    #Monkey = canvas.create_image(MonX,MonY,image=monkey)
    ###
    RabX = random.randint(20,gamewidth-10)
    RabY = random.randint(20,gameheight-10)
    with open("save.pickle","rb") as fs:
        b = pickle.load(fs)
    score = 0
    if isinstance(b,list):
        a,b,c,d,e,f,g,h,i,j,k,l,m  = Load()
        PenG = canvas.create_image(e[0],e[1],image=penguin)
        image = canvas.create_image(a[0],a[1], anchor=NW, image=snakeD)
        Elephant = canvas.create_image(b[0],b[1],image=elephant)
        Monkey = canvas.create_image(c[0],c[1],image=monkey)
        Rabbit = canvas.create_image(d[0],d[1],image=rabbit)
        score = f
        eleXspeed = g
        eleYspeed = h
        MonXspeed = i
        MonYspeed = j
        SXspeed = k
        SYspeed = l
        direction = m
        strings = ""
        openfile = open('save.pickle', 'wb')
        pickle.dump(strings, openfile)
        openfile.close()

    else:
        PenG = canvas.create_image(penX,penY,image=penguin)
        image = canvas.create_image(40,40, anchor=NW, image=snakeD)
        Elephant = canvas.create_image(eleX,eleY,image=elephant)
        Monkey = canvas.create_image(MonX,MonY,image=monkey)
        Rabbit = canvas.create_image(RabX,RabY,image=rabbit)
    fs.close()

    txt = "Score:" + str(score)
    scoreText = canvas.create_text(gamewidth//2 , 30 , fill="Blue", font="Times 20 italic bold", text=txt)

    moveSnake()
    movemonkey()
    moveelephant()

    root.mainloop()

MainMenu()
