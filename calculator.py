#A simple airthnatic calculator
import tkinter
from tkinter import*

window=tkinter.Tk()

window.title("Simple airthmetic calculator")
window.geometry("570x600")
window.resizable(False,False)
window.configure(bg="#084F49")
equation = ""
def show(value):
    global equation
    equation+=value
    Label_result.config(text=equation)
def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)
def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result = "error"
            equation=""
        Label_result.config(text=result)    
    

Label_result=Label(window,width=35,height=2,text="",font=("arial",40),bg="#A1C8C4")
Label_result.pack()
Button(window,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("%")).place(x=10,y=130)
Button(window,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("/")).place(x=150,y=130)
Button(window,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:clear()).place(x=290,y=130)
Button(window,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("*")).place(x=430,y=130)

Button(window,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("7")).place(x=10,y=220)
Button(window,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("8")).place(x=150,y=220)
Button(window,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("9")).place(x=290,y=220)
Button(window,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("-")).place(x=430,y=220)

Button(window,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("4")).place(x=10,y=310)
Button(window,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("5")).place(x=150,y=310)
Button(window,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("6")).place(x=290,y=310)
Button(window,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("+")).place(x=430,y=310)

Button(window,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("1")).place(x=10,y=400)
Button(window,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("2")).place(x=150,y=400)
Button(window,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("3")).place(x=290,y=400)
Button(window,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show("0")).place(x=10,y=490)

Button(window,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:calculate()).place(x=430,y=400)
Button(window,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#5F9089",command=lambda:show(".")).place(x=290,y=490)

window.mainloop()

