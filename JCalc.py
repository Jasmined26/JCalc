# Import modules
import tkinter
import tkinter.font as tkFont
from tkinter import *

# GUI class
class standardCalculator:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Window size
        w = 350
        h = 600

        self.main_window.geometry('%dx%d' % (w, h))

        # Create widgets
        # Labels for expression and result
        self.expression_label = tkinter.Label(bg = 'green')
        self.result_label = tkinter.Label(bg = 'blue')

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

        # Configure column weights
        self.main_window.columnconfigure(0, weight = 3)
        self.main_window.columnconfigure(1, weight = 3)
        self.main_window.columnconfigure(2, weight = 3)
        self.main_window.columnconfigure(3, weight = 3)

        # Configure row weights
        self.main_window.rowconfigure(0, weight = 1)
        self.main_window.rowconfigure(1, weight = 3)
        self.main_window.rowconfigure(2, weight = 3)
        self.main_window.rowconfigure(3, weight = 3)
        self.main_window.rowconfigure(4, weight = 3)
        self.main_window.rowconfigure(5, weight = 3)
        self.main_window.rowconfigure(6, weight = 3)

        # Grid widgets
        self.expression_label.grid(row = 0, column = 0, rowspan = 1, columnspan = 4, sticky = 'NSEW')
        self.result_label.grid(row = 1, column = 0, rowspan = 1, columnspan = 4, sticky = 'NSEW')

        self.zero_btn.grid(row = 6, column = 0, sticky = 'NSEW')
        self.one_btn.grid(row = 5, column = 0, sticky = 'NSEW')
        self.two_btn.grid(row = 5, column = 1, sticky = 'NSEW')
        self.three_btn.grid(row = 5, column = 2, sticky = 'NSEW')
        self.four_btn.grid(row = 4, column = 0, sticky = 'NSEW')
        self.five_btn.grid(row = 4, column = 1, sticky = 'NSEW')
        self.six_btn.grid(row = 4, column = 2, sticky = 'NSEW')
        self.seven_btn.grid(row = 3, column = 0, sticky = 'NSEW')
        self.eight_btn.grid(row = 3, column = 1, sticky = 'NSEW')
        self.nine_btn.grid(row = 3, column = 2, sticky = 'NSEW')

        self.add_btn.grid(row = 6, column = 3, sticky = 'NSEW')
        self.sub_btn.grid(row = 5, column = 3, sticky = 'NSEW')
        self.mult_btn.grid(row = 4, column = 3, sticky = 'NSEW')
        self.div_btn.grid(row = 3, column = 3, sticky = 'NSEW')
        self.eq_btn.grid(row = 6, column = 2, sticky = 'NSEW')
        self.dec_btn.grid(row = 6, column = 1, sticky = 'NSEW')

        self.del_btn.grid(row = 2, column = 3, sticky = 'NSEW')
        self.clear_btn.grid(row = 2, column = 2, sticky = 'NSEW')

        tkinter.mainloop()


calc1 = standardCalculator()