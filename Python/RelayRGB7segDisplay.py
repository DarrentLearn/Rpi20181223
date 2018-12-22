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
        command=lambda: buttonRelay_Click(1)
        )
    buttonOn.pack(side=LEFT, padx=3,pady=3)
    buttonOff = Button(
        frame,
        text="OFF",
        font=("Helvetica", 20),
        bg="RED",
        padx=40,
        pady=20,
        command=lambda: buttonRelay_Click(0)
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
    
    frame3 = Frame(form, borderwidth=1, relief=GROOVE)
    for i in range(10):
        SetDigitButton(frame3, i)
    frame3.pack(padx=10, pady=10, fill=X)

def buttonDigits_Click(n):
    print(n, "按下了")
    ShowDigit(n)

def ShowDigit(n):
    nv = font[n]
    i = 0
    for p in senvenLed:
        IO.output(p,nv[i])
        i += 1

def SetDigitButton(frame, buttonText):
    button = Button(
        frame,
        text=buttonText,
        font=("Helvetica", 30),
        bg="Blue",
        command=lambda: buttonDigits_Click(buttonText)
    )
    button.pack(side=LEFT, padx=3, pady=3)
#def buttonOn_Click():
#    print("ON 按下了")
#    IO.output(LedPin,1)

#def buttonOff_Click():
#    print("OFF 按下了")
#    IO.output(LedPin,0)

def buttonRelay_Click(flag):
    if flag == 0:
        print ("OFF 按下了")
    else:
        print ("ON 按下了")
    IO.output(RelayPin,flag)
    
def buttonRed_Click():
    print("Red 按下了")
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

RelayPin = 12
LedRed = 16
LedGreen = 20
LedBlue = 21
senvenLed = (17,4,23,24,25,27,22,18)

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(RelayPin,IO.OUT)
IO.setup(LedRed,IO.OUT)
IO.setup(LedGreen,IO.OUT)
IO.setup(LedBlue,IO.OUT)
for x in senvenLed:
    IO.setup(x,IO.OUT)

font = {
    0 :(1, 1, 1, 1, 1, 1, 0, 0),
    1 :(0, 1, 1, 0, 0, 0, 0, 0),
    2 :(1, 1, 0, 1, 1, 0, 1, 0),
    3 :(1, 1, 1, 1, 0, 0, 1, 0),
    4 :(0, 1, 1, 0, 0, 1, 1, 0),
    5 :(1, 0, 1, 1, 0, 1, 1, 0),
    6 :(1, 0, 1, 1, 1, 1, 1, 0),
    7 :(1, 1, 1, 0, 0, 1, 0, 0),
    8 :(1, 1, 1, 1, 1, 1, 1, 0),
    9 :(1, 1, 1, 0, 0, 1, 1, 0),
    10:(0, 0, 0, 0, 0, 0, 0, 0),
    }

if __name__ == '__main__':
    form = Tk()
    form.title('LED control')
    form.geometry("800x600")
    form.option_add("*Button.Background","#004A9B")
    form.option_add("*Button.Foreground","white")
    formInterface(form)
    form.mainloop()
