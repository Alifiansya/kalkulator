from tkinter import *
from turtle import color
#color palette = https://colorhunt.co/palette/f8ede3dfd3c3d0b8a87d6e83

expr = str()

calc= Tk()
calc.title("Calculator")
calc.config(background='#F8EDE3')

frame = Frame(calc)
frame.pack()


expr_field = Entry(
    frame,
    width=24
)
expr_field.grid(columnspan=3, row=0)


num_btn = list()
for i in range(1, 10):
    button = Button(
        frame,
        text=f"  {i}  ",
        fg='black',
        bg='#D0B8A8',
        command=None,
        width=5
    )
    button.grid(row=1 + (i-1) // 3, column=(i-1) % 3)
    num_btn.append(button)


calc.mainloop()