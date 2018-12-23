import RPi.GPIO as IO
from tkinter import *

def formLayout_Relay(form):
    'Layout form relay control'    
    frameRelay = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frameRelay, text="Relay 控制:",font=("Helvetica", 20))
    label1.pack(side=LEFT,padx=3,pady=3)
    
    buttonOn = Button(
        frameRelay,
        text="ON",
        font=("Helvetica", 20),
        bg="GREEN",
        padx=40,
        pady=20,
        command=lambda: buttonRelay_Click(1)
        )
    buttonOn.pack(side=LEFT, padx=3,pady=3)
    buttonOff = Button(
        frameRelay,
        text="OFF",
        font=("Helvetica", 20),
        bg="RED",
        padx=40,
        pady=20,
        command=lambda: buttonRelay_Click(0)
        )
    buttonOff.pack(side=LEFT, padx=3,pady=3)
    
    frameRelay.pack(padx=10,pady=10, fill=X)
    
def formLayout_ColorLED(form):
    'Layout form Color LED control'
    frameColorLED = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frameColorLED, text="COLOR LED 控制:",font=("Helvetica", 20))
    label1.pack(side=LEFT,padx=3,pady=3)

    buttonsColorLeds = (Red,Green,Blue)
    for buttonColor in buttonsColorLeds:
        SetColorLedButton(buttonColor)
    
    buttonRed = Button(
        frameColorLED,
        text="Red",
        font=("Helvetica", 20),
        bg="Red",
        padx=40,
        pady=20,
        command=buttonRed_Click
        )
    buttonRed.pack(side=LEFT, padx=3,pady=3)
    buttonGreen = Button(
        frameColorLED,
        text="Green",
        font=("Helvetica", 20),
        bg="Green",
        padx=40,
        pady=20,
        command=buttonGreen_Click
        )
    buttonGreen.pack(side=LEFT, padx=3,pady=3)
    buttonBlue = Button(
        frameColorLED,
        text="Blue",
        font=("Helvetica", 20),
        bg="Blue",
        padx=40,
        pady=20,
        command=buttonBlue_Click
        )
    buttonBlue.pack(side=LEFT, padx=3,pady=3)
    
    frameColorLED.pack(padx=10,pady=10, fill=X)
    
def formLayout_Digit(form):
    'Layout form digitl Control'
    frameDigit = Frame(form, borderwidth=1, relief=GROOVE)
    for i in range(10):
        SetDigitButton(frameDigit, i)
    frameDigit.pack(padx=10, pady=10, fill=X)

def ShowDigit(n):
    nv = FontDigit[n]
    i = 0
    for p in PinSenvenLed:
        IO.output(p,nv[i])
        i += 1

def SetColorLedButton(color):
    button = Button(
        frameColorLED,
        text=color,
        font=("Helvetica", 20),
        bg=color,
        padx=40,
        pady=20,
        command=lambda: buttonColorLed_Click(color)
    )

def buttonDigits_Click(n):
    print(n, "按下了")
    ShowDigit(n)

def SetDigitButton(frame, buttonText):
    button = Button(
        frame,
        text=buttonText,
        font=("Helvetica", 30),
        bg="Blue",
        command=lambda: buttonDigits_Click(buttonText)
    )
    button.pack(side=LEFT, padx=3, pady=3)

def buttonRelay_Click(flag):
    if flag == 0:
        print ("OFF 按下了")
    else:
        print ("ON 按下了")
    IO.output(LedPin,flag)

def buttonColorLed_Click(color):
    if color == "Red":
        colorPin = PinLedRed
    elif color == "Green":
        colorPin = PinLedGreen
    elif color == "Blue":
        colorPin = PinLedBlue

    setValue = not IO.input(colorPin)
    if setValue == 1:
        setText = "點亮"
    else:
        setText = "熄滅"
    print(setText, color)
    IO.output(colorPin, setValue)

def buttonRed_Click():
    print("Red 按下了")
    IO.output(PinLedRed,1)
    IO.output(PinLedGreen,0)
    IO.output(PinLedBlue,0)

def buttonGreen_Click():
    print("Green 按下了")
    IO.output(PinLedRed,0)
    IO.output(PinLedGreen,1)
    IO.output(PinLedBlue,0)

def buttonBlue_Click():
    print("Blue 按下了")
    IO.output(PinLedRed,0)
    IO.output(PinLedGreen,0)
    IO.output(PinLedBlue,1)

PinRelay = 12
PinLedRed = 16
PinLedGreen = 20
PinLedBlue = 21
ColorLed=(["Red",PinLedRed],["Green",PinLedGreen],["Blue",PinLedBlue])
PinSenvenLed = (17,4,23,24,25,27,22,18)

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(PinRelay,IO.OUT)

for cl in ColorLed:
    IO.setup(cl[1],IO.OUT)

for x in PinSenvenLed:
    IO.setup(x,IO.OUT)

FontDigit = {
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
    formLayout_Relay(form)
    formLayout_ColorLED(form)
    formLayout_Digit(form)
    form.mainloop()
