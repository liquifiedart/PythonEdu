from tkinter import *
from tkinter import ttk

class CalculatorApp:

    root = Tk()

    label_calc_entry = ttk.Label(root, text='', width=50)
    label_calc_comment = ttk.Label(root, text='', width=50)

    button1 = ttk.Button(root, text='1')
    button2 = ttk.Button(root, text='2')
    button3 = ttk.Button(root, text='3')
    button4 = ttk.Button(root, text='4')
    button5 = ttk.Button(root, text='5')
    button6 = ttk.Button(root, text='6')
    button7 = ttk.Button(root, text='7')
    button8 = ttk.Button(root, text='8')
    button9 = ttk.Button(root, text='9')
    button0 = ttk.Button(root, text='0')

    button_plus = ttk.Button(root, text='+')
    button_minus = ttk.Button(root, text='-')
    button_multiply = ttk.Button(root, text='*')
    button_divide = ttk.Button(root, text='/')

    button_equals = ttk.Button(root, text='=')

    operator_list = ['+', '-', '/', '*']

    prior_value = ''


    def __init__(self):

        self.button1.config(command = lambda: self.add_inputs(self.button1['text']))
        self.button2.config(command = lambda: self.add_inputs(self.button2['text']))
        self.button3.config(command = lambda: self.add_inputs(self.button3['text']))
        self.button4.config(command = lambda: self.add_inputs(self.button4['text']))
        self.button5.config(command = lambda: self.add_inputs(self.button5['text']))
        self.button6.config(command = lambda: self.add_inputs(self.button6['text']))
        self.button7.config(command = lambda: self.add_inputs(self.button7['text']))
        self.button8.config(command = lambda: self.add_inputs(self.button8['text']))
        self.button9.config(command = lambda: self.add_inputs(self.button9['text']))
        self.button0.config(command = lambda: self.add_inputs(self.button0['text']))

        self.button_plus.config(command = lambda: self.add_inputs(self.button_plus['text']))
        self.button_minus.config(command = lambda: self.add_inputs(self.button_minus['text']))
        self.button_multiply.config(command = lambda: self.add_inputs(self.button_multiply['text']))
        self.button_divide.config(command = lambda: self.add_inputs(self.button_divide['text']))

        self.button_equals.config(command = self.calculate_value)


    def run_app(self):

        self.label_calc_comment.grid(row = 0, column = 0,columnspan = 4)
        self.label_calc_comment.config( background = 'green')
        self.label_calc_comment.config( justify = CENTER)

        self.label_calc_entry.grid(row = 1, column = 0,columnspan = 4)
        self.label_calc_entry.config( background = 'red')
        self.label_calc_entry.config( justify = CENTER)

        self.button1.grid(row = 2, column = 0) #,sticky=N+S+E+W)
        self.button2.grid(row = 2, column = 1) #,,sticky=N+S+E+W)
        self.button3.grid(row = 2, column = 2) #,,sticky=N+S+E+W)
        self.button4.grid(row = 3, column = 0) #,,sticky=N+S+E+W)
        self.button5.grid(row = 3, column = 1) #,,sticky=N+S+E+W)
        self.button6.grid(row = 3, column = 2) #,,sticky=N+S+E+W)
        self.button7.grid(row = 4, column = 0) #,,sticky=N+S+E+W)
        self.button8.grid(row = 4, column = 1) #,,sticky=N+S+E+W)
        self.button9.grid(row = 4, column = 2) #,,sticky=N+S+E+W)
        self.button0.grid(row = 5, column = 1) #,,sticky=N+S+E+W)
        self.button_equals.grid(row = 5, column = 2)

        self.button_plus.grid(row = 2, column = 3)
        self.button_minus.grid(row = 3, column = 3)
        self.button_multiply.grid(row = 4, column = 3)
        self.button_divide.grid(row = 5, column = 3)



        self.root.mainloop()

    def add_inputs(self,value):
        if len(self.label_calc_entry.cget('text')) > 0:
            if value in self.operator_list and self.prior_value in self.operator_list:
                #self.label_calc_entry.config(text = self.label_calc_entry.cget('text')[0:-1] + value)
                self.label_calc_entry.config(text=self.label_calc_entry['text'][0:-1] + value)
            else:
                self.label_calc_entry.config(text=self.label_calc_entry['text'] + value)
                self.prior_value = value
        else:
            self.label_calc_entry.config(text = self.label_calc_entry['text'] + value)
            self.prior_value = value

    def calculate_value(self):
        if self.label_calc_entry.cget('text')[-1] in self.operator_list:
            self.label_calc_comment.config(text='Please enter a valid expression')
        else:
            self.label_calc_comment.config(text='Result: ' + str(eval(self.label_calc_entry['text'])))
            self.label_calc_entry.config(text='')



def main():

    calc_app = CalculatorApp()
    calc_app.run_app()


if __name__ == "__main__": main()
