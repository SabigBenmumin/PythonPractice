from tkinter import *
figgure = Tk()
figgure.title("Calculater")
expression = StringVar()

def Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def button_click(number):
        current_expression = expression.get()
        current_expression += str(number)
        expression.set(current_expression)

    def piont_press(self, num):
        temp2 = str(num)
        temp2 == '.'
        self.current = temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())
        self.display(self.current)


    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)


    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False


    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
       

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum=Calc()
root =Tk()
calc=Frame(root)
calc.grid()

root.title('Calculator_by_Patcharaporn')
text_box=Entry(calc,justify=RIGHT)
text_box.grid(row=0,column=0,columnspan=3,pady=5)
text_box.insert(0,'0')

def Number():
    try:
        result = eval(expression.get())
        expression.set(result)
    except:
        expression.set("Error")
button_1 = Button(calc, text="1")
button_1['command']=lambda: Calc.button_click(1)
button_1.grid(row=1, column=0)
button_2 = Button(calc, text="2")
button_2['command']=lambda: sum.button_click(2)
button_2.grid(row=1, column=1)
button_3 = Button(calc, text="3")
button_3['command']=lambda: sum.button_click(3)
button_3.grid(row=1, column=2)
button_4 = Button(calc, text="4")
button_4['command']=lambda: sum.button_click(4)
button_4.grid(row=2, column=0)
button_5 = Button(calc, text="5")
button_5['command']=lambda: sum.button_click(5)
button_5.grid(row=2, column=1)
button_6 = Button(calc, text="6")
button_6['command']=lambda: sum.button_click(6)
button_6.grid(row=2, column=2)
button_7 = Button(calc, text="7")
button_7['command']=lambda: sum.button_click(7)
button_7.grid(row=3, column=0)
button_8 = Button(calc, text="8")
button_8['command']=lambda: sum.button_click(8)
button_8.grid(row=3, column=1)
button_9 = Button(calc, text="9")
button_9['command']=lambda: sum.button_click(9)
button_9.grid(row=3, column=2)
#operation
button_0=Button(calc,text='0')
button_0['command']=lambda:sum.button_click(0)
button_0.grid(row=4, column=1)
button_00=Button(calc,text='00')
button_00['command']=lambda:sum.button_click(00)
button_00.grid(row=4, column=2)

divide=Button(calc,text='/')
divide['command']=lambda:sum.operation('divide')
divide.grid(row=1,column=3)

add=Button(calc,text='+')
add['command']=lambda:sum.operation('add')
add.grid(row=3,column=3)

minus=Button(calc,text='-')
minus['command']=lambda:sum.operation('minus')
minus.grid(row=4,column=3)

times=Button(calc,text='X')
times['command']=lambda:sum.operation('times')
times.grid(row=2,column=3)

neg=Button(calc,text='+/-')
neg['command']=sum.sign
neg.grid(row=5,column=0)

piont=Button(calc,text='.')
piont['command'] = lambda: sum.piont_press('.')
piont.grid(row=4,column=0)

clear=Button(calc,text='C')
clear['command']=sum.cancel
clear.grid(row=4, column=1)

allclear=Button(calc,text='AC')
allclear['command']=sum.all_cancel
allclear.grid(row=5,column=2)

equals=Button(calc,text='=')
equals['command']=sum.calc_total
equals.grid(row=5, column=3)

root.mainloop()

