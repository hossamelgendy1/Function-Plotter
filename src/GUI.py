from tkinter import *
import plotter

#setting up the window
window = Tk()
window.geometry("500x250")
window.title("Function Plotter")
#set background color
window.configure(background='#b3ffff')

#setting up the frames
main_frame = Frame(window, bg='#b3ffff')
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

expression_frame = Frame(main_frame, bg='#b3ffff')
expression_frame.pack()

min_value_frame = Frame(main_frame, bg='#b3ffff')
min_value_frame.pack()

max_value_frame = Frame(main_frame, bg='#b3ffff')
max_value_frame.pack()

button_frame = Frame(main_frame, bg='#b3ffff')
button_frame.pack()

exception_message_frame = Frame(main_frame, bg='#b3ffff')
exception_message_frame.pack()

#filling the frames
expression_label = Label(expression_frame, text='Function Expression', font=('Arial', 12), bg='#b3ffff')
expression_entry = Entry(expression_frame , width=25, font=('Arial', 12), border=2, justify=CENTER)
expression_label.pack(side=LEFT, padx=5, pady=10)
expression_entry.pack(side=LEFT, padx=5, pady=10)

min_label = Label(min_value_frame, text='Minimum value of x', font=('Arial', 12), bg='#b3ffff')
min_entry = Entry(min_value_frame, width=25, font=('Arial', 12), border=2, justify=CENTER)
min_label.pack(side=LEFT, padx=5, pady=10)
min_entry.pack(side=LEFT, padx=5, pady=10)

max_label = Label(max_value_frame, text='Maximum value of x', font=('Arial', 12), bg='#b3ffff')
max_entry = Entry(max_value_frame, width=25, font=('Arial', 12), border=2, justify=CENTER)
max_label.pack(side=LEFT, padx=5, pady=10)
max_entry.pack(side=LEFT, padx=5, pady=10)

exception_message_label = Label(exception_message_frame, text='', font=('Arial italic', 10), bg='#b3ffff')
exception_message_label.pack(side=LEFT, padx=5, pady=10)

#called when the plot button is pressed
def plot():
    try:
        #if the user left a field empty
        if expression_entry.get() == '':
            raise ValueError('Please, enter the function expression')
        if min_entry.get() == '':
            raise ValueError('Please, enter the minimum value')
        if max_entry.get() == '':
            raise ValueError('Please, enter the maximum value')

        #if the user entered a non-numeric value in the min or max fields
        try:
            #first remove any spaces, then convert to float
            min_value = float(min_entry.get().replace(' ', ''))
            max_value = float(max_entry.get().replace(' ', ''))
        except:
            raise ValueError('ERROR: minimum and maximum values must be numbers!')

        #if the max value is less than or equals the min value
        if (max_value <= min_value):
            raise ValueError('ERROR: minimum value is greater than the maximum value!')

        plotter.plot(min_value, max_value, expression_entry.get())
        #if any exception was raised in the plot function, the following statement wouldn't be excuted
        exception_message_label.configure(text='The function was plotted successfully')
    except ValueError as e:
        exception_message_label.configure(text=e)

button = Button(button_frame, text='Plot', width=10, border=1, font=('Arial bold',12), bg='#737373', fg='#f2f2f2', activeforeground='#f2f2f2', activebackground='#595959', command=plot)
button.pack(side=LEFT, padx=5, pady=20)

#used to keep the window active
window.mainloop()