from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.iconbitmap('Items\calc.ico')

e=Entry(root,width=35,borderwidth=4,bg='#6be9cf')
e.grid(column=0,row=0,columnspan=6,padx=10,pady=10)

def button_click(number):
    num=e.get()
    e.delete(0,END)
    e.insert(0,str(num)+str(number))

def button_dot():
    num=str(e.get())
    if "." not in num:
        e.delete(0,END)
        e.insert(0,str(num)+".")

def button_clear():
    e.delete(0,END)

def button_back():
    a=str(e.get())
    b=a[:-1]
    e.delete(0,END)
    e.insert(0,b)

def button_add():
    global num_add
    global math
    math="Add"
    num=e.get()
    num_add=float(num)
    e.delete(0,END)

def button_diff():
    global num_diff
    global math
    math="Diff"
    num=e.get()
    num_diff=float(num)
    e.delete(0,END)

def button_multi():
    global num_multi
    global math
    math="Multi"
    num=e.get()
    num_multi=float(num)
    e.delete(0,END)

def button_divide():
    global num_divide
    global math
    math="Divide"
    num=e.get()
    num_divide=float(num)
    e.delete(0,END)

def button_equal():
    num2=e.get()
    e.delete(0,END)
    if math=="Add":
        e.insert(0,num_add+float(num2))
    elif math=="Diff":
        e.insert(0,num_diff-float(num2))
    elif math=="Multi":
        e.insert(0,num_multi*float(num2))
    elif math=="Divide":
        e.insert(0,num_divide/float(num2))

# Buttons :
button_dot=Button(root, text=".", padx=22, pady=17, command=button_dot, bg='#a6d62f')
button_back=Button(root, text="←", padx=19, pady=17, command=button_back, bg='#8a15ff')
button_diff=Button(root, text="–", padx=20, pady=17, command=button_diff, bg='#c8c8c8')
button_add=Button(root, text="+", padx=18.5, pady=17, command=button_add, bg='#c8c8c8')
button_multi=Button(root, text="x", padx=20, pady=17, command=button_multi, bg='#c8c8c8')
button_equal=Button(root, text="=", padx=20, pady=45, command=button_equal, bg='#8080ff')
button_clear=Button(root, text="C", padx=19, pady=17, command=button_clear, bg='#8a15ff')
button_divide=Button(root, text="/", padx=20, pady=17, command=button_divide, bg='#c8c8c8')
button_1=Button(root, text="1", padx=20, pady=17, command=lambda: button_click(1), bg='#a6d62f')
button_2=Button(root, text="2", padx=20, pady=17, command=lambda: button_click(2), bg='#a6d62f')
button_3=Button(root, text="3", padx=20, pady=17, command=lambda: button_click(3), bg='#a6d62f')
button_4=Button(root, text="4", padx=20, pady=17, command=lambda: button_click(4), bg='#a6d62f')
button_5=Button(root, text="5", padx=20, pady=17, command=lambda: button_click(5), bg='#a6d62f')
button_6=Button(root, text="6", padx=20, pady=17, command=lambda: button_click(6), bg='#a6d62f')
button_7=Button(root, text="7", padx=20, pady=17, command=lambda: button_click(7), bg='#a6d62f')
button_8=Button(root, text="8", padx=20, pady=17, command=lambda: button_click(8), bg='#a6d62f')
button_9=Button(root, text="9", padx=20, pady=17, command=lambda: button_click(9), bg='#a6d62f')
button_0=Button(root, text="0", padx=48, pady=17, command=lambda: button_click(0), bg='#a6d62f')

# Buttons on Screen :
button_1.grid(row=5 , column=0)
button_2.grid(row=5 , column=1)
button_3.grid(row=5 , column=2)

button_4.grid(row=4 , column=0)
button_5.grid(row=4 , column=1)
button_6.grid(row=4 , column=2)

button_7.grid(row=3 , column=0)
button_8.grid(row=3 , column=1)
button_9.grid(row=3 , column=2)

button_0.grid(row=6 , column=0 , columnspan=2)
button_dot.grid(row=6 , column=2)
button_add.grid(row=3 , column=4)
button_diff.grid(row=4 , column=4)
button_multi.grid(row=5 , column=4)
button_divide.grid(row=6 , column=4)
button_equal.grid(row=5 , column=5 , rowspan=2)
button_clear.grid(row=4 , column=5)
button_back.grid(row=3 , column=5)

root.mainloop()
