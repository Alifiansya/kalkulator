from cgitb import text
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

def press_equal(equation):
    try:
        global text_expr
        text_expr = text_expr.lstrip('0')
        text_expr = str(eval(text_expr))
        equation.set(text_expr)
    except:
        equation.set("Error!")
        text_expr = ""

def press_c(equation):
    global text_expr
    text_expr = ""
    equation.set(text_expr)

def press_dot(equation):
    global text_expr
    text_expr += '.'
    equation.set(text_expr)

def press_larrow(equation):
    global text_expr
    if text_expr == "":
        return
    text_expr = text_expr[:-1]
    equation.set(text_expr)

