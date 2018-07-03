import Tkinter

def clickme():
    print "Hello There."

mw = Tkinter.Tk()
mw.title('Hello World')

button = Tkinter.Button(mw, text='Click me', command = clickme)
button.pack()

mw.mainloop()