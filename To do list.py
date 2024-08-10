#Program for to do list
import tkinter
from tkinter import*
from tkinter import messagebox
window = tkinter.Tk()
window.title("To do list")
window.geometry("400x650")
window.resizable(False,False)
window.config(bg="#AFADEF")

task_list=[]
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt","a")as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w")as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)        
                
        
def openTaskFile():
    try:
        global task_liSt
        with open("tasklist.txt","r")as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !="\n":
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file=open("tasklist.txt","w")
        file.close()
    




Label_result=Label(window,width=30,height=1,text="ALL TASK",font=("arial",20,"bold"),bg="#C2F588")
Label_result.pack()

frame=Frame(window,width=400,height=50,bg="white")
frame.place(x=0,y=140)
task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

frame1=Frame(window,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

Button(window,text="Delete",font="arial 20 bold",bg="#5a95ff",fg="#fff",bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

window.mainloop()

