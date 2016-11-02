import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

LARGE_FONT = ("Verdana", 12)
filePath = []

class MP3Player(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,"CST-205-Project3")
        container.pack(side = "top", fill  = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}
        f = StartPage
        frame = f(container, self)
        self.frames[f] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        def Play():
            print("play")

        def Pause():
            print("Pause")

        def Horror():
            print("Prepare for the horror")

        def Happy():
            print("Prepare to for an uplifting happy tune.")

        def Blues():
            print("Prepare for some blues.")

        def Emo():
            print("Prepare for some emo tunes.")

        def Browse():
            global filePath
            filename = filedialog.askopenfilename()
            for i in filePath:
                filePath.append(filename)
                # filePath = filename
                file_label = ttk.Label(self,text = filePath, font = LARGE_FONT)

                file_label.place(x = 200, y = 175+i*50)

                print(filePath)

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "MP3 Player", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)



        play = ttk.Button(self,text = "Play", command = Play)
        play.place(x = 40, y = 40)

        pause = ttk.Button(self,text = "Pause", command = Pause)
        pause.place(x = 160, y = 40)

        pg = ttk.Progressbar(self, orient='horizontal',length=300, mode='determinate')
        pg.place(x = 40, y = 70)


        FileBrowse = ttk.Button(self,text = "Browse",command = Browse)
        FileBrowse.place(x = 40, y= 175)

        labelChoose = ttk.Label(self,text = "Choose a theme: ", font = LARGE_FONT)
        labelChoose.place(x = 40, y = 127)


        horror = ttk.Button(self,text = "Horror", command = Horror)
        horror.place(x = 40, y = 150)


        happy = ttk.Button(self,text = "Happy", command = Happy)
        happy.place(x = 160, y = 150)

        blues = ttk.Button(self,text = "Blues", command = Blues)
        blues.place(x = 280, y = 150)

        emo = ttk.Button(self,text = "Emo", command = Emo)
        emo.place(x = 400, y = 150)





app = MP3Player()
app.geometry("1000x400")
app.mainloop()

