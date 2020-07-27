from tkinter import *
import tkinter as tk
def send():
    root.destroy()
    import attendance
def ad():
    #root.destroy()
    import Login
root=Tk()
root.geometry('550x400')
root.title("attendance monitoring system")
parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
parent.pack(fill=tk.BOTH, expand=True)
parent=Frame(root,bg='khaki')
parent.pack()
l=Label(root,text=" WELCOME TO ATTENDANCE MONITORING",font=("Comic Sans Ms", 18),height=1,bg='goldenrod')
l.place(x=10,y=20)
img1=PhotoImage(file="attendance.png")
img2=PhotoImage(file="admin.png")
b1=Button(root,image=img1,height=150,width=150,command=send)
b1.place(x=50,y=130)
b2=Button(root,image=img2,command=ad)
b2.place(x=270,y=130)
root.mainloop()
