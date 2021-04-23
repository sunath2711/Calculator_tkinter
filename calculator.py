from tkinter import *

root = Tk()
root.title("Calculator")


input_box = Entry(root,width=16,borderwidth=5,font="Helvetica 24 bold",justify="right")
input_box.grid(row=0,column=0,columnspan=4)

def button_click(number):
    current = input_box.get()
    input_box.delete(0,END)
    input_box.insert(0,str(current) + str(number))



def button_clearall():
    input_box.delete(0,END)


def button_addnum():
    first_num = input_box.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    input_box.delete(0,END)

def button_subnum():
    first_num = input_box.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_num)
    input_box.delete(0, END)

def button_mulnum():
    first_num = input_box.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_num)
    input_box.delete(0, END)

def button_divnum():
    first_num = input_box.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    input_box.delete(0, END)

def button_deciadd():
    current = input_box.get()
    input_box.delete(0,END)
    input_box.insert(0,str(current) + ".")

def button_percentage():
    first_num = input_box.get()
    global f_num
    global math
    math = "percentage"
    f_num = float(first_num)
    input_box.delete(0, END)

def button_signalter():
    current = input_box.get()
    input_box.delete(0,END)
    if int(current) > 0:
        input_box.insert(0,"-"+str(current))
    else:
        input_box.insert(0,current.replace('-',''))

def button_clearlast():
    current  = input_box.get()
    input_box.delete(0,END)
    input_box.insert(0,current[:-1])

def button_equalto():
    second_num = input_box.get()
    input_box.delete(0, END)
    if math=="addition" :
        input_box.insert(0, f_num + float(second_num))
    elif math == "subtraction":
        input_box.insert(0, f_num + float(second_num))
    elif math == "multiplication":
        input_box.insert(0, f_num * float(second_num))
    elif math=="division" :
        input_box.insert(0, round(f_num / float(second_num),3))
    elif math == "percentage":
        input_box.insert(0,(f_num/float(second_num))*100)


#padx=20, pady=13
button_clear = Button(root, text="Clear all", padx=20, pady=13,width=4, command=button_clearall)
button_1 = Button(root, text="1", padx=20, pady=13,width=4, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=13, width=4,command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=13,width=4, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=13,width=4,command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=13, width=4,command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=13, width=4,command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=13, width=4,command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=13, width=4,command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=13, width=4,command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=13, width=4,command=lambda: button_click(0))
button_add = Button(root, text="+", padx=20, pady=13,width=4, command=button_addnum)
button_sub = Button(root, text="-", padx=20, pady=13,width=4, command=button_subnum)
button_mul = Button(root, text="*", padx=20, pady=13,width=4, command=button_mulnum)
button_div = Button(root, text="/", padx=20, pady=13, width=4,command=button_divnum)
button_equal = Button(root, text="=", padx=20, pady=13,width=4, command=button_equalto)
button_decimal = Button(root, text=".", padx=20, pady=13,width=4, command=button_deciadd)
button_signchange = Button(root, text="+/-", padx=20, pady=13,width=4, command=button_signalter )
button_singleclear = Button(root, text="<--", padx=20, pady=13,width=4,command=button_clearlast)
button_percentage = Button(root, text="%", padx=20, pady=13, width=4,command=button_percentage)


button_signchange.grid(row=1,column=0)
button_percentage.grid(row=1,column=1)
button_clear.grid(row=1,column=2)
button_singleclear.grid(row=1,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_div.grid(row=2,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row=4,column=3)

button_0.grid(row=5,column=0)
button_decimal.grid(row=5,column=1)
button_equal.grid(row=5,column=2)
button_sub.grid(row=5,column=3)
root.mainloop()