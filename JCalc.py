# Import modules
import tkinter
import tkinter.font as tkFont
from tkinter import *

# GUI class
class standardCalculator:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create widgets

        # Labels for expression and result
        self.expression_label = tkinter.Label()
        self.result_label = tkinter.Label()

        # Digit buttons
        self.zero_btn = tkinter.Button(text = '0')
        self.one_btn = tkinter.Button(text = '1')
        self.two_btn = tkinter.Button(text = '2')
        self.three_btn = tkinter.Button(text = '3')
        self.four_btn = tkinter.Button(text = '4')
        self.five_btn = tkinter.Button(text = '5')
        self.six_btn = tkinter.Button(text = '6')
        self.seven_btn = tkinter.Button(text = '7')
        self.eight_btn = tkinter.Button(text = '8')
        self.nine_btn = tkinter.Button(text = '9')

        # Operation buttons
        self.add_btn = tkinter.Button(text = '+')
        self.sub_btn = tkinter.Button(text = '-')
        self.mult_btn = tkinter.Button(text = '*')
        self.div_btn = tkinter.Button(text = '/')
        self.eq_btn = tkinter.Button(text = '=')
        self.dec_btn = tkinter.Button(text = '.')

        # Delete/Clear buttons
        self.del_btn = tkinter.Button(text = 'DEL')
        self.clear_btn = tkinter.Button(text = 'C')

        # Grid widgets
        self.expression_label.grid(row = 0, column = 0, rowspan = 1, columnspan = 4)
        self.result_label.grid(row = 1, column = 0, rowspan = 1, columnspan = 4)

        self.zero_btn.grid(row = 6, column = 0)
        self.one_btn.grid(row = 5, column = 0)
        self.two_btn.grid(row = 5, column = 1)
        self.three_btn.grid(row = 5, column = 2)
        self.four_btn.grid(row = 4, column = 0)
        self.five_btn.grid(row = 4, column = 1)
        self.six_btn.grid(row = 4, column = 2)
        self.seven_btn.grid(row = 3, column = 0)
        self.eight_btn.grid(row = 3, column = 1)
        self.nine_btn.grid(row = 3, column = 2)

        self.add_btn.grid(row = 6, column = 3)
        self.sub_btn.grid(row = 5, column = 3)
        self.mult_btn.grid(row = 4, column = 3)
        self.div_btn.grid(row = 3, column = 3)
        self.eq_btn.grid(row = 6, column = 2)
        self.dec_btn.grid(row = 6, column = 1)

        self.del_btn.grid(row = 2, column = 3)
        self.clear_btn.grid(row = 2, column = 2)

        tkinter.mainloop()


calc1 = standardCalculator()