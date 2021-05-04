from tkinter import *

expression = " "


def bt_click(item):
    global expression
    expression = expression + str(item)
    inputtext.set(expression)


def bt_clear():
    global expression
    expression = ""
    inputtext.set("")


def bt_eq():
    global expression
    result = str(eval(expression))
    inputtext.set(result)
    expression = ""


def bt_sq():
    global expression
    val = int(expression)
    sq = val*val
    inputtext.set(str(sq))
    expression = ""
def bt_del():
    global expression
    expression = expression[:-1]
    inputtext.set(expression)

window = Tk()
window.geometry("350x500")
space = "                        "
window.title(space + "CALCULATOR")
window.configure(bg='#55552b')

inputtext = StringVar()

frame = Frame(window, width=350, height=500, highlightbackground="white", highlightcolor="black", highlightthickness=2,
              bg="black")

frame.pack()

label = Label(frame, text="Result:", bg="white", fg="black", width=15).place(x=20, y=20)
field = Entry(frame, font=('arial', 20, 'bold'), textvariable=inputtext, width=20)
field.place(x=20, y=55)

button1 = Button(frame, height=2, width=8, text="0", command=lambda: bt_click(0)).place(x=20, y=130)
button2 = Button(frame, height=2, width=5, text="1", command=lambda: bt_click(1)).place(x=20, y=200)
button3 = Button(frame, height=2, width=5, text="2", command=lambda: bt_click(2)).place(x=80, y=200)
button4 = Button(frame, height=2, width=5, text="3", command=lambda: bt_click(3)).place(x=140, y=200)
button5 = Button(frame, height=2, width=5, text="4", command=lambda: bt_click(4)).place(x=200, y=200)
button6 = Button(frame, height=2, width=5, text="5", command=lambda: bt_click(5)).place(x=260, y=200)
button7 = Button(frame, height=2, width=5, text="6", command=lambda: bt_click(6)).place(x=20, y=270)
button8 = Button(frame, height=2, width=5, text="7", command=lambda: bt_click(7)).place(x=80, y=270)
button9 = Button(frame, height=2, width=5, text="8", command=lambda: bt_click(8)).place(x=140, y=270)
button10 = Button(frame, height=2, width=5, text="9", command=lambda: bt_click(9)).place(x=200, y=270)
button11 = Button(frame, height=6, width=5, text="+", command=lambda: bt_click("+")).place(x=260, y=275)
button12 = Button(frame, height=2, width=5, text="-", command=lambda: bt_click("-")).place(x=80, y=335)
button13 = Button(frame, height=2, width=5, text="*", command=lambda: bt_click("*")).place(x=140, y=335)
button14 = Button(frame, height=2, width=5, text="/", command=lambda: bt_click("/")).place(x=200, y=335)
button15 = Button(frame, height=2, width=5, text="DEL", command=bt_del).place(x=20, y=335)
button16 = Button(frame, height=2, width=12, text="CLR", command=bt_clear).place(x=20, y=400)
button17 = Button(frame, height=2, width=5, text="=", command=bt_eq).place(x=125, y=400)
button18 = Button(frame, height=2, width=5, text=".", command=lambda: bt_click(".")).place(x=185, y=400)
button19 = Button(frame, height=2, width=8, text="SQR", command=bt_sq).place(x=240, y=400)

window.mainloop()
