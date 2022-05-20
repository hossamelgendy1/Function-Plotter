from tkinter import *
import plotter

window = Tk()
window.geometry("500x250")
window.title("Function Plotter")

main_frame = Frame(window)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

frame1 = Frame(main_frame)
frame1.pack()
label1 = Label(frame1, text='Function Expression')
e1 = Entry(frame1)
label1.pack(side=LEFT, padx=5, pady=10)
e1.pack(side=LEFT, padx=5, pady=10)

frame2 = Frame(main_frame)
frame2.pack()
label2 = Label(frame2, text='Minimum value of x')
e2 = Entry(frame2)
label2.pack(side=LEFT, padx=5, pady=10)
e2.pack(side=LEFT, padx=5, pady=10)

frame3 = Frame(main_frame)
frame3.pack()
label3 = Label(frame3, text='Maximum value of x')
e3 = Entry(frame3)
label3.pack(side=LEFT, padx=5, pady=10)
e3.pack(side=LEFT, padx=5, pady=10)

def plot():
    try:
        min = float(e2.get())
        max = float(e3.get())
        plotter.plot(min, max, e1.get())
    except ValueError:
        pass

frame4 = Frame(main_frame)
frame4.pack()
button = Button(frame4, text='Plot', command=plot)
button.pack(side=LEFT, padx=5, pady=20)





window.mainloop()