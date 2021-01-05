# Import modules
import tkinter
import tkinter.font as tkFont
from tkinter import *

# Class to create a button that changes color when hovered over
# Inherits from tkinter Button class
class HoverButton1(tkinter.Button):
    def __init__(self, **kw):
        tkinter.Button.__init__(self, **kw)
        self['bd'] = 1
        self['background'] = '#88b5fc'
        self.defaultBackground = self['background']
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, e):
        self['background'] = '#4287f5'

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Hover button inheriting from HoverButton1 class
# (has a different color)
class HoverButton2(HoverButton1):
    def __init__(self, **kw):
        HoverButton1.__init__(self, **kw)
        self['background'] = '#e3abff'
        self.defaultBackground = self['background']

    def on_enter(self, e):
        self['background'] = '#d278ff'

# Hover button inheriting from HoverButton1 class
# (has a different color)
class HoverButton3(HoverButton1):
    def __init__(self, **kw):
        HoverButton1.__init__(self, **kw)
        self['background'] = '#63ff9a'
        self.defaultBackground = self['background']

    def on_enter(self, e):
        self['background'] = '#00bf43'



# GUI class
class standardCalculator:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Window design/attributes
        self.main_window['background'] = '#0d0063'
        self.main_window.attributes('-alpha', 0.95)
        self.main_window.title('JCalc')
        self.main_window.minsize(250, 300)

        # Window size
        w = 350
        h = 600

        # Settings to place window in middle of screen when ran
        ws = self.main_window.winfo_screenwidth()
        hs = self.main_window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Font settings to be used with window widgets
        window_font1 = tkFont.Font(family = 'Bahnschrift', size = 20)
        window_font2 = tkFont.Font(family = 'Bahnschrift Light', size = 16)

        # StringVars to update expression and result labels
        self.expressionVar = tkinter.StringVar()
        self.resultVar = tkinter.StringVar()

        # Create widgets
        # Labels for expression and result
        self.expression_label = tkinter.Label(bg = '#0d0063', fg = '#f4f2ff', textvariable = self.expressionVar, font = ('Bahnschrift', 16), anchor = 'e')
        self.result_label = tkinter.Label(bg = '#0d0063', fg = '#f4f2ff', textvariable = self.resultVar, font = ('Bahnschrift', 46), anchor = 'e')

        # Digit buttons
        self.zero_btn = HoverButton1(text = '0', command = lambda: self.update_input(self.zero_btn), font = window_font1)
        self.one_btn = HoverButton1(text = '1', command = lambda: self.update_input(self.one_btn), font = window_font1)
        self.two_btn = HoverButton1(text = '2', command = lambda: self.update_input(self.two_btn), font = window_font1)
        self.three_btn = HoverButton1(text = '3', command = lambda: self.update_input(self.three_btn), font = window_font1)
        self.four_btn = HoverButton1(text = '4', command = lambda: self.update_input(self.four_btn), font = window_font1)
        self.five_btn = HoverButton1(text = '5', command = lambda: self.update_input(self.five_btn), font = window_font1)
        self.six_btn = HoverButton1(text = '6', command = lambda: self.update_input(self.six_btn), font = window_font1)
        self.seven_btn = HoverButton1(text = '7', command = lambda: self.update_input(self.seven_btn), font = window_font1)
        self.eight_btn = HoverButton1(text = '8', command = lambda: self.update_input(self.eight_btn), font = window_font1)
        self.nine_btn = HoverButton1(text = '9', command = lambda: self.update_input(self.nine_btn), font = window_font1)

        # Operation buttons
        self.add_btn = HoverButton2(text = '+', command = lambda: self.update_input(self.add_btn), font = window_font2)
        self.sub_btn = HoverButton2(text = '-', command = lambda: self.update_input(self.sub_btn), font = window_font2)
        self.mult_btn = HoverButton2(text = '*', command = lambda: self.update_input(self.mult_btn), font = window_font2)
        self.div_btn = HoverButton2(text = '/', command = lambda: self.update_input(self.div_btn), font = window_font2)
        self.eq_btn = HoverButton3(text = '=', command = self.equals, font = window_font2)
        self.dec_btn = HoverButton1(text = '.', command = lambda: self.update_input(self.dec_btn), font = window_font2)

        # Delete/Clear buttons
        self.del_btn = HoverButton3(text = 'DEL', command = self.delete_entry, font = window_font2)
        self.clear_btn = HoverButton3(text = 'C', command = self.clear, font = window_font2)

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

        self.zero_btn.grid(row = 6, column = 0, sticky = 'NSEW', padx = 1, pady = 1)
        self.one_btn.grid(row = 5, column = 0, sticky = 'NSEW', padx = 1, pady = 1)
        self.two_btn.grid(row = 5, column = 1, sticky = 'NSEW', padx = 1, pady = 1)
        self.three_btn.grid(row = 5, column = 2, sticky = 'NSEW', padx = 1, pady = 1)
        self.four_btn.grid(row = 4, column = 0, sticky = 'NSEW', padx = 1, pady = 1)
        self.five_btn.grid(row = 4, column = 1, sticky = 'NSEW', padx = 1, pady = 1)
        self.six_btn.grid(row = 4, column = 2, sticky = 'NSEW', padx = 1, pady = 1)
        self.seven_btn.grid(row = 3, column = 0, sticky = 'NSEW', padx = 1, pady = 1)
        self.eight_btn.grid(row = 3, column = 1, sticky = 'NSEW', padx = 1, pady = 1)
        self.nine_btn.grid(row = 3, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

        self.add_btn.grid(row = 6, column = 3, sticky = 'NSEW', padx = 1, pady = 1)
        self.sub_btn.grid(row = 5, column = 3, sticky = 'NSEW', padx = 1, pady = 1)
        self.mult_btn.grid(row = 4, column = 3, sticky = 'NSEW', padx = 1, pady = 1)
        self.div_btn.grid(row = 3, column = 3, sticky = 'NSEW', padx = 1, pady = 1)
        self.eq_btn.grid(row = 6, column = 2, sticky = 'NSEW', padx = 1, pady = 1)
        self.dec_btn.grid(row = 6, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

        self.del_btn.grid(row = 2, column = 3, sticky = 'NSEW', padx = 1, pady = 1)
        self.clear_btn.grid(row = 2, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

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
            # Formatting large numbers to scientific notation
            if (len(str(result)) > 10):
                result = "{:.5e}".format(result)
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
            # Formatting large numbers to scientific notation
            if (len(str(result)) > 10):
                result = "{:.5e}".format(result)
            self.expressionVar.set(result)
            self.resultVar.set('')
        except:
            self.resultVar.set('Invalid input')




calc1 = standardCalculator()