from tkinter import *


def formInterface(form):
    'define form interface'
    frame3 = Frame(form, borderwidth=1, relief=GROOVE)
    for i in range(10):
        SetDigitButton(frame3, i)
    frame3.pack(padx=10, pady=10, fill=X)


def buttonDigits_Click(i):
    print(i, "按下了")


def SetDigitButton(frame, buttonText):
    button = Button(
        frame,
        text=buttonText,
        font=("Helvetica", 30),
        bg="Blue",
        command=lambda: buttonDigits_Click(buttonText)
    )
    button.pack(side=LEFT, padx=3, pady=3)


if __name__ == '__main__':
    form = Tk()
    form.title('LED control')
    form.geometry("800x600")
    form.option_add("*Button.Background", "#004A9B")
    form.option_add("*Button.Foreground", "white")
    formInterface(form)
    form.mainloop()
