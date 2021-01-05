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

        # StringVars to update expression and result labels
        self.expressionVar = tkinter.StringVar()
        self.resultVar = tkinter.StringVar()

        # Create widgets
        # Labels for expression and result
        self.expression_label = tkinter.Label(bg = 'green', textvariable = self.expressionVar)
        self.result_label = tkinter.Label(bg = 'blue', textvariable = self.resultVar)

        # Digit buttons
        self.zero_btn = tkinter.Button(text = '0', command = lambda: self.update_input(self.zero_btn))
        self.one_btn = tkinter.Button(text = '1', command = lambda: self.update_input(self.one_btn))
        self.two_btn = tkinter.Button(text = '2', command = lambda: self.update_input(self.two_btn))
        self.three_btn = tkinter.Button(text = '3', command = lambda: self.update_input(self.three_btn))
        self.four_btn = tkinter.Button(text = '4', command = lambda: self.update_input(self.four_btn))
        self.five_btn = tkinter.Button(text = '5', command = lambda: self.update_input(self.five_btn))
        self.six_btn = tkinter.Button(text = '6', command = lambda: self.update_input(self.six_btn))
        self.seven_btn = tkinter.Button(text = '7', command = lambda: self.update_input(self.seven_btn))
        self.eight_btn = tkinter.Button(text = '8', command = lambda: self.update_input(self.eight_btn))
        self.nine_btn = tkinter.Button(text = '9', command = lambda: self.update_input(self.nine_btn))

        # Operation buttons
        self.add_btn = tkinter.Button(text = '+', command = lambda: self.update_input(self.add_btn))
        self.sub_btn = tkinter.Button(text = '-', command = lambda: self.update_input(self.sub_btn))
        self.mult_btn = tkinter.Button(text = '*', command = lambda: self.update_input(self.mult_btn))
        self.div_btn = tkinter.Button(text = '/', command = lambda: self.update_input(self.div_btn))
        self.eq_btn = tkinter.Button(text = '=', command = self.equals)
        self.dec_btn = tkinter.Button(text = '.', command = lambda: self.update_input(self.dec_btn))

        # Delete/Clear buttons
        self.del_btn = tkinter.Button(text = 'DEL', command = self.delete_entry)
        self.clear_btn = tkinter.Button(text = 'C', command = self.clear)

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

    # Function to update labels with button entries
    def update_input(self, btn):
        self.expressionVar.set(self.expressionVar.get() + btn['text'])
        self.get_result()

    # Function to attempt to get the result of the current expression and update
    # the results label
    def get_result(self):
        try:
            result = eval(self.expressionVar.get())
            self.resultVar.set(result)
        except:
            self.resultVar.set('')

    # Callback function for the 'clear' button
    def clear(self):
        self.resultVar.set('')
        self.expressionVar.set('')

    # Callback function for the 'delete' button
    def delete_entry(self):
        self.expressionVar.set(self.expressionVar.get()[:-1])
        self.get_result()

    # Callback function for the equal button
    def equals(self):
        try:
            result = eval(self.expressionVar.get())
            self.expressionVar.set(result)
            self.resultVar.set('')
        except:
            self.resultVar.set('Invalid input')




calc1 = standardCalculator()