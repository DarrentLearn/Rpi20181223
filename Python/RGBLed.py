#import tkinter as tk
import RPi.GPIO as IO
from tkinter import *

def formInterface(form):
    'define form interface'
    
    frame = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frame, text="Relay 控制:",font=("Helvetica", 20))
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
    
    frame.pack(padx=10,pady=10, fill=X)
    
    frame2 = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frame2, text="COLOR LED 控制:",font=("Helvetica", 20))
    label1.pack(side=LEFT,padx=3,pady=3)
    
    buttonRed = Button(
        frame2,
        text="Red",
        font=("Helvetica", 20),
        bg="Red",
        padx=40,
        pady=20,
        command=buttonRed_Click
        )
    buttonRed.pack(side=LEFT, padx=3,pady=3)
    buttonGreen = Button(
        frame2,
        text="Green",
        font=("Helvetica", 20),
        bg="Green",
        padx=40,
        pady=20,
        command=buttonGreen_Click
        )
    buttonGreen.pack(side=LEFT, padx=3,pady=3)
    buttonBlue = Button(
        frame2,
        text="Blue",
        font=("Helvetica", 20),
        bg="Blue",
        padx=40,
        pady=20,
        command=buttonBlue_Click
        )
    buttonBlue.pack(side=LEFT, padx=3,pady=3)
    
    frame2.pack(padx=10,pady=10, fill=X)
    
def buttonOn_Click():
    print("ON 按下了")
    IO.output(LedPin,1)

def buttonOff_Click():
    print("OFF 按下了")
    IO.output(LedPin,0)
    
def buttonRed_Click():
    print("Red按下了")
    IO.output(LedRed,1)
    IO.output(LedGreen,0)
    IO.output(LedBlue,0)

def buttonGreen_Click():
    print("Green 按下了")
    IO.output(LedRed,0)
    IO.output(LedGreen,1)
    IO.output(LedBlue,0)

def buttonBlue_Click():
    print("Blue 按下了")
    IO.output(LedRed,0)
    IO.output(LedGreen,0)
    IO.output(LedBlue,1)

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


