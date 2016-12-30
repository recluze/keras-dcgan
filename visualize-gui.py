#!/usr/bin/python

import Tkinter
from PIL import ImageTk, Image



class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent

        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)

        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        photo = ImageTk.PhotoImage(Image.open("100_0.png"))

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, image=photo)
        label.image = photo
        self.label = label 
        label.pack(side = "bottom", fill = "both", expand = "yes")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')



        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        # self.labelVariable.set(self.entryVariable.get()+" (You clicked the button)")
        img2 = ImageTk.PhotoImage(Image.open("0_0.png"))
        self.label.configure(image = img2)
        self.label.image = img2

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+" (You pressed enter)")

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('DCGAN Visualizer')
    app.mainloop()
