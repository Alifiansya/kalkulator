from tkinter import *
#color palette = https://colorhunt.co/palette/f8ede3dfd3c3d0b8a87d6e83

expr = str()

calc= Tk()
frame = Frame(calc)
frame.pack()
calc.title("Calculator")
calc.config(background='#F8EDE3')
num_btn = Button(
    frame,
    text='test',
    command=None
)
num_btn.grid()

calc.mainloop()