import Tkinter
mw = Tkinter.Tk()
mw.title('Hello World')

gender = Tkinter.StringVar()
gender.set('F')

male = Tkinter.Radiobutton(mw, text='Male', variable=gender, value='M')
male.pack()
female = Tkinter.Radiobutton(mw, text='Female', variable=gender, value='F')
female.pack()

def clickme():
    print "user selected", gender.get()

button = Tkinter.Button(mw, text='Click me', command = clickme)
button.pack()

mw.mainloop()