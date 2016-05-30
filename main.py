from Tkinter import *


def write_slogan(myType):
    if (myType == "Head"):
	t = Text(root)
	t.pack()
    else:
	print "Other stuff"


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.bQuit = Button(frame, text="QUIT", fg="red",command=frame.quit)
        self.bQuit.pack(side=LEFT)
        self.bHeaders = Button(frame,text = "Headers",command=lambda: write_slogan("Head"))
        self.bEmphasis = Button(frame,text="Emphasis",command=lambda: write_slogan("Emph"))
        self.listbox = Listbox(frame)
        self.bQuit.pack(side=TOP)
        self.bHeaders.pack(side=TOP)
        self.bEmphasis.pack(side=TOP)
        self.listbox.pack(side=RIGHT)

root = Tk()
app = App(root)
root.mainloop()

	
