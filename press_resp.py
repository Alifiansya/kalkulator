from tkinter import *

text_expr = ""
def press_num(num, equation):
    global text_expr
    text_expr += str(num)
    equation.set(text_expr)

def press_op(op, equation):
    global text_expr
    text_expr += op
    equation.set(text_expr)

def press_enter(equation):
    try:
        global text_expr
        text_expr = str(eval(text_expr))
        equation.set(text_expr)
    except:
        equation.set("Error!")
        text_expr = ""


