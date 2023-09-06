from tkinter import *
from tkinter import messagebox

def login():
    sername=entry1.get()
    password=entry2.get()

    if (username=="" and password==" "):
        messagebox.showinfo("","Blanck Not Allowed")

    elif (username=="praivet" and password=="admin"):
        messagebox.showinfo("","login succsess")

    else:
        messagebox.showinfo("","invalied username and password")
root=Tk()
root.title("Loging")
root.geometry("300x200")

global entry1
global entry2

Label(root,text="Usarname").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=80)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=80)

Button(root,Text="Login",command=login,heght=3,width=13,bd=6).palce(x=100,y=120)  

root.mainloop()
