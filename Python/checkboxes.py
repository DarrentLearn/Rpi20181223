# https://www.reddit.com/r/learnpython/comments/6dbhc7/array_of_checkboxes/
import tkinter as tk
from tkinter import ttk

class CheckBoxes(tk.Tk):
    def __init__(self, rows=10, columns=10, **kwargs):
        tk.Tk.__init__(self, **kwargs)

        self.btns = []
        self.selected = [False] * (rows * columns)

        for row in range(rows):
            for column in range(columns):
                cbtn = ttk.Checkbutton(self, command=self.update)
                cbtn.state(('!alternate',)) # unchecked by default
                cbtn.grid(row=row, column=column)
                self.btns.append(cbtn)

        btn = ttk.Button(self, text="Submit", command=self.destroy) # closes the window - same effect as clicking the 'X'
        btn.grid(columnspan=columns)

    def update(self):
        self.selected = [btn.instate(('selected',)) for btn in self.btns]

btn_box = CheckBoxes(5, 5) # make a 5x5 grid
btn_box.mainloop() # this will block until the window is closed
print(btn_box.selected) # prints the resulting list of selected checkboxes