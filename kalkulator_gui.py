from tkinter import *
#color palette = https://colorhunt.co/palette/f8ede3dfd3c3d0b8a87d6e83

expr = str()

calc= Tk()
calc.title("Calculator")
calc.config(background='#F8EDE3')

frame = Frame(calc)
frame.pack()

num_btn = list()
for i in range(1, 10):
    button = Button(
        frame,
        text=f"  {i}  ",
        fg='black',
        bg='#D0B8A8',
        command=None
    )
    button.grid(row=(i-1) // 3, column=(i-1) % 3)
    num_btn.append(button)

calc.mainloop()