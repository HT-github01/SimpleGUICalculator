from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearScreen():
    global operator
    operator = ""
    text_Input.set("")

#eval() function evaluates the expression
def btnTotal():
    global operator
    total=str(eval(operator))
    text_Input.set(total)
    operator = ""


calculator = Tk()
calculator.title("Calculator")


#string operator to handle input
operator = ""
text_Input = StringVar() #Holds a string; default value ""

"""
Entry() is function similar with 
- scanf in C language
- scanner in Java
- to get user input

bd = border
bg = background color
justify = either LEFT, RIGHT or CENTER

padx = padding
fg = foreground color
"""
text_Display = Entry(calculator, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30,
                     width=20, bg="#889469", justify='right')
text_Display.grid(columnspan=4)


#calculator button
btn7 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="7", command=lambda:btnClick(7))
btn7.grid(row=1, column=0)

btn8 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="8", command=lambda:btnClick(8))
btn8.grid(row=1, column=1)

btn9 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="9", command=lambda:btnClick(9))
btn9.grid(row=1, column=2)

btnAdd = Button(calculator, padx=16, bd=8, bg="orange", fg="black", font=('arial', 20, 'bold'), text="+", command=lambda:btnClick("+"))
btnAdd.grid(row=1, column=3)


btn4 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="4", command=lambda:btnClick(4))
btn4.grid(row=2, column=0)

btn5 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="5", command=lambda:btnClick(5))
btn5.grid(row=2, column=1)

btn6 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="6", command=lambda:btnClick(6))
btn6.grid(row=2, column=2)

btnSubtract = Button(calculator, padx=16, bd=8, bg="orange", fg="black", font=('arial', 20, 'bold'), text="-", command=lambda:btnClick("-"))
btnSubtract.grid(row=2, column=3)


btn1 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="1", command=lambda:btnClick(1))
btn1.grid(row=3, column=0)

btn2 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="2", command=lambda:btnClick(2))
btn2.grid(row=3, column=1)

btn3 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="3", command=lambda:btnClick(3))
btn3.grid(row=3, column=2)

btnMultiply = Button(calculator, padx=16, bd=8, bg="orange", fg="black", font=('arial', 20, 'bold'), text="*", command=lambda:btnClick("*"))
btnMultiply.grid(row=3, column=3)


btn0 = Button(calculator, padx=16, bd=8, bg="#BFB6B4", fg="black", font=('arial', 20, 'bold'), text="0", command=lambda:btnClick(0))
btn0.grid(row=4, column=0)

btnClear = Button(calculator, padx=16, bd=8, bg="orange", fg="black", font=('arial', 20, 'bold'), text="C", command=btnClearScreen)
btnClear.grid(row=4, column=1)

btnEqual = Button(calculator, padx=16, bd=8, bg="orange", fg="black", font=('arial', 20, 'bold'), text="=", command=btnTotal)
btnEqual.grid(row=4, column=2)

btnDivide = Button(calculator, padx=16, bd=8, bg="orange", fg="black", font=('arial', 20, 'bold'), text="/", command=lambda:btnClick("/"))
btnDivide.grid(row=4, column=3)


calculator.mainloop()
