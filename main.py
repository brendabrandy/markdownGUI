from Tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.bQuit = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.bQuit.pack(side=LEFT)
    self.bHeaders = Button(frame,
			text = "Headers",
			command=self.write_slogan)
    self.bEmphasis = Button(frame,
                         text="Emphasis",
                         command=self.write_slogan)
    self.bQuit.pack(side=TOP)
    self.bHeaders.pack(side=TOP)
    self.bEmphasis.pack(side=TOP)
  def write_slogan(self):
    print "Tkinter is easy to use!"

root = Tk()
app = App(root)
root.mainloop()
