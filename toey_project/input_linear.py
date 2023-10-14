from tkinter import *
window = Tk()
window.title("เครื่องคิดเลข")
expression = StringVar()
def button_click(number):
    current_expression = expression.get()
    current_expression += str(number)
    expression.set(current_expression)

def clear():
    expression.set("")


def calculate():
    try:
        result = eval(expression.get())
        expression.set(result)
    except:
        expression.set("Error")
button_1 = Button(window, text="1", command=lambda: button_click(1))
button_2 = Button(window, text="2", command=lambda: button_click(2))
button_3 = Button(window, text="3", command=lambda: button_click(3))
button_4 = Button(window, text="4", command=lambda: button_click(4))
button_5 = Button(window, text="5", command=lambda: button_click(5))
button_6 = Button(window, text="6", command=lambda: button_click(6))
button_7 = Button(window, text="7", command=lambda: button_click(7))
button_8 = Button(window, text="8", command=lambda: button_click(8))
button_9 = Button(window, text="9", command=lambda: button_click(9))
button_0 = Button(window, text="0", command=lambda: button_click(0))
button_clear = Button(window, text="Clear", command=clear)
button_equal = Button(window, text="=", command=calculate)
expression_label = Label(window, textvariable=expression)
expression_label.grid(row=0, columnspan=4)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
window.mainloop()
