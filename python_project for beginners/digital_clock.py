from tkinter import *
from time import strftime


window = Tk()
window.geometry("300x75")
window.configure(bg="black")
space = "            "
window.title(space+"DIGITAL CLOCK")


def clock():
    time = strftime('%H:%M:%S %p')
    label = Label(frame, font=('arial', 20, 'bold'), text=time, fg="white", bg="black")
    label.place(x=65, y=20)
    label.after(1000, clock)

frame = Frame(window, width=300, height=75, highlightbackground="white", highlightcolor="black", highlightthickness=2,
              bg="black")

frame.pack()

clock()
window.mainloop()
