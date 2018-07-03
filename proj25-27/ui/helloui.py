import Tkinter
mw = Tkinter.Tk()
mw.title('Hello World')

label = Tkinter.Label(mw, text='Hello There. Am a label')
label.pack()
entry = Tkinter.Entry(mw)
entry.pack()

male = Tkinter.Radiobutton(mw, text='Male')
male.pack()
female = Tkinter.Radiobutton(mw, text='Female')
female.pack()

sports = Tkinter.Checkbutton(mw, text='Sports')
sports.pack()
politics = Tkinter.Checkbutton(mw, text='Politics')
politics.pack()
technology = Tkinter.Checkbutton(mw, text='Technology')
technology.pack()

button = Tkinter.Button(mw, text='Click me')
button.pack()

mw.mainloop()