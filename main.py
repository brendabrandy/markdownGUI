from Tkinter import *
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.bQuit = Button(frame, text="QUIT", fg="red",command=frame.quit)
        self.bQuit.pack(side=LEFT)
        self.bHeaders = Button(frame,text = "Headers",command=lambda: self.write_slogan("Head"))
        self.bEmphasis = Button(frame,text="Emphasis",command=lambda: self.write_slogan("Emph"))
        self.listbox = Listbox(frame)
        self.bQuit.pack(side=TOP)
        self.bHeaders.pack(side=TOP)
        self.bEmphasis.pack(side=TOP)
        self.listbox.pack(side=RIGHT)
    def write_slogan(self,myType):
        if (myType == "Head"):
	    self.listbox.insert(END,"Head")
	elif (myType == "Emph"):
	    self.listbox.insert(END,"Emph")

root = Tk()
app = App(root)
root.mainloop()
