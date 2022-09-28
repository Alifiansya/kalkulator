from tkinter import *
from press_resp import *
#color palette = https://colorhunt.co/palette/f8ede3dfd3c3d0b8a87d6e83

op_btn_sym = ['C', '<=', '%', '/', '*', '-', '+']
op_btn = dict()

if __name__ == "__main__":
    calc= Tk()
    calc.title("Calculator")
    calc.config(background='#F8EDE3')
    
    frame = Frame(calc)
    frame.pack()
    equation = StringVar(frame)
    expr_field = Entry(
        frame,
        state=DISABLED,
        disabledforeground='black',
        textvariable=equation,
        width=33
    )
    expr_field.grid(columnspan=4, row=0)
    
    
    for i in range(3):
        button = Button(
            frame,
            text=f"  {op_btn_sym[i]}  ",
            fg='black',
            bg='#D0B8A8',
            width=5
        )
        button.grid(row=1, column=i)
        op_btn.update({op_btn_sym[i]: button})
    
    for i in range(4):
        button = Button(
            frame,
            text=f"  {op_btn_sym[i+3]}  ",
            fg='black',
            bg='#D0B8A8',
            command=None,
            width=5
        )
        button.grid(row=i+1, column=3)
        op_btn.update({op_btn_sym[i+3]: button})
    
    
    num_btn = list()
    for i in range(1, 10):
        button = Button(
            frame,
            text=f"  {i}  ",
            fg='black',
            bg='#D0B8A8',
            command=lambda i=i: press_num(i, equation),
            width=5
        )
        button.grid(row=2 + (i-1) // 3, column=(i-1) % 3)
        num_btn.append(button)
    
    # for 0 number
    num_btn.insert(
        0,
        Button(
            frame,
            text="  0  ",
            fg='black',
            bg='#D0B8A8',
            command=lambda:press_num(0, equation),
            width=5
        )
    )
    num_btn[0].grid(row=5, column=1)
    
    nan_btn = list()
    nan_btn.append(
        Button(
            frame,
            text="",
            fg='black',
            bg='#D0B8A8',
            command=None,
            width=5
        )
    )
    nan_btn[0].grid(row=5, column=0)
    
    dot_btn = Button(
            frame,
            text="  .  ",
            fg='black',
            bg='#D0B8A8',
            command=lambda: press_dot(equation),
            width=5
    )
    dot_btn.grid(row=5, column=2)
    
    equal_btn = Button(
        frame,
        text="  =  ",
        fg='black',
        bg='#D0B8A8',
        command=lambda: press_equal(equation),
        width=5
    )
    equal_btn.grid(row=5, column=3)

    # Adding commands op
    for i in op_btn_sym:
        if i in ['<=', 'C']:
            continue
        op_btn[i].configure(command=lambda i=i: press_op(i, equation))
    
    op_btn["<="].configure(command=lambda:press_larrow(equation))
    op_btn['C'].configure(command=lambda:press_c(equation))
    calc.mainloop()

    print(op_btn)