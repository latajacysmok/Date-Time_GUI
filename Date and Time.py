import sys
import time
from tkinter import *
from datetime import date

today = date.today()

def value1():
    num1.set(today)
    return

def value2():
    today = time.asctime(time.localtime(time.time()))
    num1.set(today)
    return

root = Tk()
root.title("Data and Time")
root.geometry('450x350')
root.resizable(0, 0)
root ['bg'] = 'powder blue'
frame = Frame(root)
frame.pack()

num1 = StringVar()
radbtn = StringVar()
radbtn.set(None)

frame1 = Frame(root)
frame1.pack(side=TOP)

label1 = Label(frame1, text="\n")
label1.pack(side=TOP)
label1 = Label(frame1, text="See Current Date Below", font=('arial', 25, 'bold'), fg='Black', relief=RAISED)
label1.pack(side=TOP)
label1 = Label(frame1, text="\n")
label1.pack(side=TOP)

txtDisplay = Entry(frame1, textvariable=num1, bd=25, insertwidth=1, font=15, justify='center')
txtDisplay.pack(side=TOP)

radio1 = Radiobutton(frame1, text="Local Time", variable=radbtn, value="Local Time", command=value2).pack(side=BOTTOM)

button1 =Button(frame1, padx=16, pady=16, bd=8, text="Today Date is", bg='black', fg='white', activebackground='Gray', activeforeground="White", command=value2)
button1.pack(side=BOTTOM)
radio1 = Radiobutton(frame1, text="My Time", variable=radbtn, value="My Time", command=value1).pack(side=BOTTOM)

root.mainloop()