from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.iconbitmap('Items\calc.ico')
root.minsize(355,325)
root.maxsize(355,325)

label1=Label(root,text="Equation -->").grid(row=2,column=1)
label2=Label(root,text="Result -->").grid(row=3,column=1)

e=Entry(root,width=35,borderwidth=4,bg='#6be9cf')
f=Entry(root,width=35,borderwidth=4,bg='#5285e2')

e.grid(row=2,column=2,columnspan=6,padx=10,pady=10)
f.grid(row=3,column=2,columnspan=6,padx=10,pady=10)


def button_click(number):
    num=e.get()
    e.delete(0,END)
    e.insert(0,str(num)+str(number))

def button_clear():
    e.delete(0,END)
    f.delete(0,END)

def button_back():
    a=str(e.get())
    b=a[:-1]
    e.delete(0,END)
    e.insert(0,b)

def button_equal():
    num=str(e.get())
    num2=num.replace('(','*')
    num3=num2.replace(')','*')
    f.delete(0,END)
    try:
        ans=eval(num3)
        k=str(ans)
        if isinstance(ans,int) or isinstance(ans,float):
            f.insert(0,k)
        else:
            f.insert(0,"Error!")
    except:
        f.insert(0,"Error!")


# Defining Buttons :
button_back=Button(root,text="←",padx=19,pady=17,bg='#8a15ff',activebackground='#fbe342',activeforeground='#fa2001',command=button_back)
button_equal=Button(root,text="=",padx=20,pady=45,bg='#8080ff',activebackground='#fbe342',activeforeground='#fa2001',command=button_equal)
button_clear=Button(root,text="C",padx=19,pady=17,bg='#8a15ff',activebackground='#fbe342',activeforeground='#fa2001',command=button_clear)
button_dot=Button(root,text=".",padx=22,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click('.'))
button_diff=Button(root,text="–",padx=20,pady=17,bg='#c8c8c8',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click('-'))
button_add=Button(root,text="+",padx=18.5,pady=17,bg='#c8c8c8',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click('+'))
button_multi=Button(root,text="x",padx=20,pady=17,bg='#c8c8c8',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click('*'))
button_divide=Button(root,text="/",padx=20,pady=17,bg='#c8c8c8',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click('/'))
button_1=Button(root,text="1",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(1))
button_2=Button(root,text="2",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(2))
button_3=Button(root,text="3",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(3))
button_4=Button(root,text="4",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(4))
button_5=Button(root,text="5",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(5))
button_6=Button(root,text="6",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(6))
button_7=Button(root,text="7",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(7))
button_8=Button(root,text="8",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(8))
button_9=Button(root,text="9",padx=20,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(9))
button_0=Button(root,text="0",padx=48,pady=17,bg='#a6d62f',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(0))
button_sb1=Button(root,text='(',padx=27,pady=16,bg='#c8c8c8',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click('('))
button_sb2=Button(root,text=')',padx=27,pady=16,bg='#c8c8c8',activebackground='#fbe342',activeforeground='#fa2001',command=lambda:button_click(')'))

# Buttons on Screen :
button_1.grid(row=7 , column=2)
button_2.grid(row=7 , column=3)
button_3.grid(row=7 , column=4)

button_4.grid(row=6 , column=2)
button_5.grid(row=6 , column=3)
button_6.grid(row=6 , column=4)

button_7.grid(row=5 , column=2)
button_8.grid(row=5 , column=3)
button_9.grid(row=5 , column=4)

button_0.grid(row=8 , column=2 , columnspan=2)
button_dot.grid(row=8 , column=4)
button_add.grid(row=5 , column=6)
button_diff.grid(row=6 , column=6)
button_multi.grid(row=7 , column=6)
button_divide.grid(row=8 , column=6)
button_equal.grid(row=7 , column=7 , rowspan=2)
button_clear.grid(row=6 , column=7)
button_back.grid(row=5 , column=7)
button_sb1.grid(row=5,column=1)
button_sb2.grid(row=6,column=1)

root.mainloop()
