import Tkinter
mw = Tkinter.Tk()
mw.title('Hello World')

text = [ 'Art', 'Trekking']
text_v = [ Tkinter.IntVar() for i in text]

for t, t_v in zip(text, text_v):
    cb = Tkinter.Checkbutton(mw, text=t, variable=t_v)
    cb.pack()

def clickme():
    print "Hello There."
    print [ v.get() for v in text_v]

button = Tkinter.Button(mw, text='Click me', command = clickme)
button.pack()

mw.mainloop()