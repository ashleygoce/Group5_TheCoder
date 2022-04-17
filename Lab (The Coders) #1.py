from tkinter import *

class Window(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.pack(fill=BOTH, expand=1)

    text = Label(self, text="Laboratory Activity 5")
    text.place(x=150, y=30)
    # text.pack()
    text = Label(self, text="Submitted To Mam Sayo")
    text.place(x=140, y=50)
    # text.pack()


window = Tk()
app = Window(window)
window.wm_title("Label (The Coders)")
window.geometry("430x100+10+10")
window.mainloop()