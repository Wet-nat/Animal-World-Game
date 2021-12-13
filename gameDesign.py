from tkinter import *
from tkinter import messagebox,ttk
import random
from tkinter import font
def MainMenu():
    mainWindow = Tk()
    mainWindow.title("Brank New Snake Game")
    ws = mainWindow.winfo_screenwidth() #computers screen size
    hs = mainWindow.winfo_screenheight()
    x = str((ws//2)-(width//2))
    y = str((hs//2)-(height//2))

    mainWindow.geometry(str(ws)+"x"+str(hs))
    # mainWindow.attributes("-fullscreen", True)
    # if ws != width or hs != height:
    #     message = 'Warning: Your screen resolution is ' + str(ws) + 'x' + str(hs) + ', which is not the recommended resolution ' + str(width) + 'x' + str(height) +  ' and your gaming experience may be affected. ' + 'Do you still want to play in full screen?'
    #     ans = messagebox.askquestion(title="Bad Resolution", message=message)
    #     if ans == 'No':
    #         mainWindow.attributes("-fullscreen", False)
    #         mainWindow.geometry(str(width)+"x"+str(height)+"+"+x+"+"+y)
    #         canvas = Canvas(mainWindow, width = width, height = height,highlightthickness=10, highlightbackground="#f20c18",background="#cdebb2")
    #         canvas.pack()
    #         gamewidth,gameheight = width,height
    
    start = Button(mainWindow,text="Start",bg="yellow",font=("Times 20 bold"),width=8)
    leader = Button(mainWindow,text="Top 10",bg="yellow",font=("Times 20 bold"),width=8)
    quit = Button(mainWindow,text="quit",bg="yellow",font=("Times 20 bold"),width=8)
    start.place(relx=0.5,rely=0.4,anchor=CENTER)
    leader.place(relx=0.5,rely=0.5,anchor=CENTER)
    quit.place(relx=0.5,rely=0.6,anchor=CENTER)
    
    mainWindow.mainloop()


width = 1600
height = 900

MainMenu()