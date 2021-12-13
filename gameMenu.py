
from tkinter import Tk, Canvas, Button, Entry, PhotoImage, font, messagebox,ttk
from tkinter.constants import S

    window_width = 1600
    window_height = 900
    default_cursor = 'circle'
    active_cursor = 'spider'
    default_key_settings = {
        'pause': '<Escape>',
        'jump1': '<space>',
        'jump2': '<Up>',
        'cheat': '<r>',
        'boss': '<b>'}
    def __init__(self):
        self.window = Tk()
        self.window.title("Brand New Snake Game")
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height)) #
        self.window.resizable(width=False, height=False)
        self.window.attributes("-fullscreen", True)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        if screen_width != self.window_width or \
                screen_height != self.window_height:
            message = 'Notice: Your screen resolution is ' + \
                str(screen_width) + 'x' + str(screen_height) + \
                ', which is not the recommended resolution ' + \
                str(self.window_width) + 'x' + str(self.window_height) + \
                ' and your gaming experience may be affected. ' + \
                'Do you still want to play in full screen?'
            ans = messagebox.askquestion(
                title="Bad Resolution", message=message)
            if ans == 'no':
                self.window.attributes("-fullscreen", False)
                self.window.geometry(str(self.window_width) + "x" +
                                     str(self.window_height) + "+" +
                                     str((screen_width // 2) -
                                         (self.window_width // 2)) + "+" +
                                     str((screen_height // 2) -
                                         (self.window_height // 2)))
                
        self.displayMenu()
        self.window.mainloop()

    def displayMenu(self):
        self.menuCV = Canvas(
            self.window,
            width=self.window_width,
            height=self.window_height,
            cursor=self.default_cursor,
            highlightthickness=0)
        self.menuCV.create_text(
            100,
            50,
            anchor='nw',
            text='Welcome to Snake Game',
            font=("Consolas",25),
            fill='black',
            activefill='red')

        self.menuCV.place(x=0, y=0)

        self.startButton = Button(self.window, text="Start",font=("Consolas",25),width=10,bg="Yellow",cursor=self.active_cursor)
        self.quitButton = Button(self.window, text="Quit",font=("Consolas",25),width=10,bg="Red",command=lambda:self.quitgame(),cursor=self.active_cursor)
        self.startButton.pack()
        self.quitButton.pack()

    def startgame(self):
        self.startframe = ttk.Frame(self.window, padding="5 5 12 12")
        self.startframe.grid(column=0,row=0,sticky=(N,W,E,S))
        self.window.colormapwindows(0, weight=1)
        self.window.row

    def quitgame(self):

        self.window.destroy()

gamemenu()




