from tkinter import *
window = Tk()
window.geometry("400x300+20+10")
window.title('Semestral Grade')

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window,text="Semestral Grade", fg = "blue", bg = "yellow")
        self.lbl1.place(relx=0.50,y=50,anchor="center")
        self.lbl2 = Label(window,text="Enter Prelim Grade:")
        self.lbl2.place(x=50,y=80)
        self.txtfld2 = Entry(window,bd=3)
        self.txtfld2.place(x=180,y=80)
        self.lbl3 = Label(window,text="Enter Midterm Grade:")
        self.lbl3.place(x=50,y=120)
        self.txtfld3=Entry(window,bd=3)
        self.txtfld3.place(x=180,y=120)
        self.lbl4 = Label(window, text="Enter Final Grade:")
        self.lbl4.place(x=50, y=160)
        self.txtfld4=Entry(window,bd=3)
        self.txtfld4.place(x=180,y=160)



        self.btn1=Button(window,text="Compute",command=self.add)
        self.btn1.place(x=200,y=208, anchor="center")


        self.lbl5=Label(window,text="Result")
        self.lbl5.place(x=50,y=230)
        self.txtfld5=Entry(window,bd=4)
        self.txtfld5.place(x=180,y=230)


    def add(self):
        self.txtfld5.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        num3=int(self.txtfld4.get())
        answer = (num1*0.3)+(num2*0.30)+(num3*0.4)
        self.txtfld5.insert(END,answer)

mywin = MyWindow(window)

window.mainloop()
