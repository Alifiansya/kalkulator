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
    width=33
)
expr_field.grid(columnspan=4, row=0)

op_btn_sym = ['C', '<=', '%', '/', '*', '-', '+']
op_btn = dict()

for i in range(3):
    button = Button(
        frame,
        text=f"  {op_btn_sym[0]}  ",
        fg='black',
        bg='#D0B8A8',
        command=None,
        width=5
    )
    button.grid(row=1, column=i)
    op_btn.update({op_btn_sym[0]: button})
    op_btn_sym.pop(0)

for i in range(4):
    button = Button(
        frame,
        text=f"  {op_btn_sym[0]}  ",
        fg='black',
        bg='#D0B8A8',
        command=None,
        width=5
    )
    button.grid(row=i+1, column=3)
    op_btn.update({op_btn_sym[0]: button})
    op_btn_sym.pop(0)


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
    button.grid(row=2 + (i-1) // 3, column=(i-1) % 3)
    num_btn.append(button)


calc.mainloop()