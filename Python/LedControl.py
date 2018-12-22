#import tkinter as tk
import RPi.GPIO as IO
from tkinter import *

def formInterface(form):
    'define form interface'
    frame = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frame, text="LED 控制:",font=("Helvetica", 20))
    label1.pack(side=LEFT,padx=3,pady=3)
    
    buttonOn = Button(
        frame,
        text="ON",
        font=("Helvetica", 20),
        bg="GREEN",
        padx=40,
        pady=20,
        command=buttonOn_Click
        )
    buttonOn.pack(side=LEFT, padx=3,pady=3)
    buttonOff = Button(
        frame,
        text="OFF",
        font=("Helvetica", 20),
        bg="RED",
        padx=40,
        pady=20,
        command=buttonOff_Click
        )
    buttonOff.pack(side=LEFT, padx=3,pady=3)
    
    #textbox1 = Entry(frame, text="textbox(Entry)")
    #textbox1.pack(padx=3,pady=3)
    
    #radioButton1 = Radiobutton(frame,text="radio button 1")
    #radioButton1.pack(padx=3,pady=3)
    #radioButton2 = Radiobutton(frame,text="radio button 2")
    #radioButton2.pack(padx=3,pady=3)
    
    frame.pack(padx=10,pady=10, fill=X)

def buttonOn_Click():
    print("ON 按下了")
    IO.output(LedPin,1)

def buttonOff_Click():
    print("OFF 按下了")
    IO.output(LedPin,0)

LedPin = 12
LedRed = 16
LedGreen = 20
LedBlue = 21

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(LedPin,IO.OUT)
IO.setup(LedRed,IO.OUT)
IO.setup(LedGreen,IO.OUT)
IO.setup(LedBlue,IO.OUT)

if __name__ == '__main__':
    form = Tk()
    form.title('LED control')
    form.geometry("800x600")
    form.option_add("*Button.Background","#004A9B")
    form.option_add("*Button.Foreground","white")
    formInterface(form)
    form.mainloop()

