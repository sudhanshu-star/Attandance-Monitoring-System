from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import csv
import smtplib
import urllib.request
import json
import time
from firebase import firebase
from PIL import Image, ImageDraw, ImageFont
from prettytable import PrettyTable
def send():
    import matplotlib.pyplot as plt
    import numpy as np
    import csv
    def send3():
        x=e1.get()
        count=0
        c=[]
        la=['absent','present']
        '''with open('allstudent.csv', 'r') as csvfil:
            csvreader = csv.reader(csvfil)
            for row in csvreader:
                if (len(row)!=0):
                    if x==row[0]:'''
        with open('abc.csv', 'r') as csvfil:
            csvread = csv.reader(csvfil)
            for row in csvread:
                if (len(row)!=0):
                    c.append(row[0])
                    if (x==row[1]) :
                        count+=1
        d=[]
        print(count)
        for i in range(len(c)):
            if c[i] not in d :
                d.append(c[i])
        uni=len(d)
        #count=uni-count
        uni=uni-count
        print(uni)
        print(count)
        
        m= [uni,count]
        cols=['r','g']
        plt.title("chart of "+x)
        plt.pie(m,labels=la,colors=cols,explode=[0.1,0],autopct='%1.1f%%')
        plt.show()
    def send2():
        root.destroy()
    root=Tk()
    root.geometry('400x300')
    root.title("GRAPH OF STUDENT")
    parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
    parent.pack(fill=tk.BOTH, expand=True)
    parent=Frame(root,bg='khaki')
    parent.pack()
    l=Label(root,text=" CREATED BY SUDHANSHU",font=("Comic Sans Ms", 18),height=1,bg='goldenrod')
    l.place(x=10,y=20)
    l2=Label(root,text=" ENTER STUDENT ID NO",font=("Comic Sans Ms", 10),height=1,bg='goldenrod')
    l2.place(x=10,y=100)
    e1=Entry(root,bg='khaki',width=40)
    e1.place(x=190,y=100)

    b1=Button(root,text='create graph',height=3,width=12,bg='brown2',command=send3)
    b1.place(x=120,y=150)
    b1=Button(root,text='Back',height=3,width=12,bg='yellow',command=send2)
    b1.place(x=120,y=220)

    root.mainloop()


def second():
    
    def send():
        x=e1.get()
        #print(x)
        y=x[8:10]+x[7]+x[5:7]+x[4]+x[:4]
        #print(y)
        count=0
        c=[]
        d=[]
        e=[]
        la=['absent','present']
        '''with open('allstudent.csv', 'r') as csvfil:
            csvreader = csv.reader(csvfil)
            for row in csvreader:
                if (len(row)!=0):
                    if x==row[0]:'''
        with open('abc.csv', 'r') as csvfile:
            csvread = csv.reader(csvfile)
            for row in csvread:
                if (len(row)==3):
                    #print(row)
                    #print(row[0])
                    #c.append(row[2])
                    if (x==row[0]or y ==row[0]) :
                        #print('yes')
                        c.append(row[2])
                        #print(c)
        #print(c)
        for i in range(len(c)):
            if i not in d:
                d.append(c[i])
        for i in range(len(d)):
            e.append(c.count(d[i]))
        plt.xlabel('DEPARTMENT',COLOR='RED')
        plt.ylabel('NO OF STUDENT',COLOR='GREEN')
        plt.title('GRAPH OF STUDENT DEPARTMENT WISE',COLOR='BROWN')
                             
        plt.bar(d,e)
        plt.show()
    root=Tk()
    root.geometry('400x300')
    root.title("GRAPH OF STUDENT by DEPARTMENT WISE")
    parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
    parent.pack(fill=tk.BOTH, expand=True)
    parent=Frame(root,bg='khaki')
    parent.pack()
    l=Label(root,text=" CREATED BY SUDHANSHU",font=("Comic Sans Ms", 18),height=1,bg='goldenrod')
    l.place(x=10,y=20)
    l2=Label(root,text=" ENTER DATE in yyyy-mm-dd format",font=("Comic Sans Ms", 10),height=1,bg='goldenrod')
    l2.place(x=10,y=100)
    e1=Entry(root,bg='khaki',width=40)
    e1.place(x=250,y=100)

    b1=Button(root,text='create graph',height=3,width=12,bg='brown2',command=send)
    b1.place(x=120,y=150)
    root.mainloop()

def third():
    image = Image.new('RGB', (1000,900), (191, 114,114))
    #image= Image.open("C:/Users/Sudhanshu/Desktop/team54/sudhanshu.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)
    import random
    import os
    import datetime
    import qrcode
    from tkinter import filedialog
    firebase=firebase.FirebaseApplication('https://team54-b72f8.firebaseio.com/')
    filename=''
    def upload():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(filename)
        #ima = Image.open(filename)
        #filename.save('x.bmp')
    def create_id():
        x1=e1.get()
        x2=e2.get()
        x3=e3.get()
        x4=e4.get()
        x5=e5.get()
        x6=e6.get()
        x7=e7.get()
        #rows=[x1,x2,x3,x4,x5]
        (x,y)=(50,50)
        message = 'A.C.E.T '
        company=message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=80)
        draw.text((x, y), message, fill=color, font=font)
        (x, y) = (600, 75)
        ID=''
        if x7==' ':
            idno=random.randint(10000000,90000000)
            ID = str('ID'+str(idno))
            idno=ID
        else:
            idno=x7
            ID=str(x7)
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=60)
        draw.text((x, y), ID, fill=color, font=font)
        rows=[ID,x1,x3,x2,x4,x5,x6]
        (x, y) = (50, 250)
        message = x1
        name=message
        color = 'rgb(0, 0, 0)' 
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y),'NAME:-'+ message, fill=color, font=font)
        (x, y) = (50, 350)
        message = x2
        color = 'rgb(0, 0, 0)' 
        draw.text((x, y),'D.O.B.:-'+ message, fill=color, font=font)
        (x, y) = (50, 450)
        message = x3
        color = 'rgb(0, 0, 0)'  
        draw.text((x, y),'BRANCH:-'+ message, fill=color, font=font)
        (x, y) = (50, 550)
        message = x4
        color = 'rgb(0, 0, 0)'  
        draw.text((x, y), 'MOB:-'+message, fill=color, font=font)
        (x, y) = (50, 650)
        message = x6
        color = 'rgb(255, 0, 0)'
        draw.text((x, y),'Blood group:-'+ message, fill=color, font=font)
        (x, y) = (50, 750)
        message = x5
        temp=message
        color = 'rgb(0, 0, 0)'
        draw.text((x, y),'EMAIL:-'+ message, fill=color, font=font)
        '''(x, y) = (50, 750)
        message = input('Enter Your Address: ')
        color = 'rgb(0, 0, 0)' # black color 
        draw.text((x, y), message, fill=color, font=font)'''
        image.save(str(name)+'.png')
        img = qrcode.make(str(company)+str(idno))   
        img.save(str(idno)+'.bmp')
        til = Image.open(name+'.png')
        im = Image.open(str(idno)+'.bmp') 
        til.paste(im,(600,350))
        #cookImage = PhotoImage(file = filename)
        #cookImage = ImageTk.PhotoImage(Image.open(filename))
        #ima = Image.open(filename) #25x25
        print('Done')
        #image2=cookImage.resize((100,50),Image.ANTIALIAS)
        #cookImage=ImageTk.PhotoImage(cookImage)
        #cookImage=cookImage.resize(25,25)
        width=25
        height=25
        #i = ima.resize((width, height), Image.BICUBIC)  
        #til.paste(cookImage,(600,350))
        til.save(name+'.png')
        with open('allstudent.csv', 'a') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            #csvwriter.writerow(fields) 
            csvwriter.writerow(rows)
        print(ID,x1,x2,x3,x4,x5,x6)
        result=firebase.put('all student id'+x3,ID,{"name":x1,'email':x5,'mobile no':x4,'date of birth':x2,'blood group':x6})
        print(result)
        try:
            gmailaddress = 'sudhanshubhardwaj999@gmail.com'
            gmailpassword = '2hateyou@'
            mailto = x5
            msg = 'id created'
            mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
            mailServer.starttls()
            mailServer.login(gmailaddress , gmailpassword)
            mailServer.sendmail(gmailaddress, mailto , msg)
            print(" \n Sent!")
            mailServer.quit()
        except:
            print("network error ")
        
    def bac():
        root.destroy()
        
    root=Tk()
    root.geometry('450x500')
    root.title("attendance monitoring system")
    parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
    parent.pack(fill=tk.BOTH, expand=True)
    parent=Frame(root,bg='khaki')
    parent.pack()
    l=Label(root,text=" CREATE STUDENT ID",font=("Comic Sans Ms", 28),height=1,bg='goldenrod')
    l.place(x=15,y=20)
    l2=Label(root,text='  ENTER NAME  ')
    l2.place(x=10,y=80)
    l3=Label(root,text='DATE OF BIRTH')
    l3.place(x=10,y=120)
    l4=Label(root,text='COURSE ')
    l4.place(x=10,y=160)
    l5=Label(root,text='MOBILE NO')
    l5.place(x=10,y=200)
    e1 = Entry(root,text='enter  your name',width=50 )
    e1.place(x=150,y=80)
    e2 = Entry(root,text='date of birth',width=50 )
    e2.place(x=150,y=120)
    e3 = Entry(root,text='blood group',width=50 )
    e3.place(x=150,y=160)
    e4 = Entry(root,text='mobile',width=50 )
    e4.place(x=150,y=200)
    e5 = Entry(root,text='email',width=50 )
    e5.place(x=150,y=240)
    e6 = Entry(root,text='BLOOD GROUP',width=50 )
    e6.place(x=150,y=280)
    e7 = Entry(root,text='ID NO',width=50 )
    e7.place(x=150,y=320)
    l6=Label(root,text='ENTER YOUR MAIL')
    l6.place(x=10,y=240)
    l7=Label(root,text='BLOOD GROUP')
    l7.place(x=10,y=280)
    l8=Label(root,text='Id NO')
    l8.place(x=10,y=320)
    #img1=PhotoImage(file="submit.png")
    b2=Button(root,text='submit',command=create_id,width=20,height=3,bg='pink')
    b2.place(x=130,y=400)
    b3=Button(root,text='upload image',command=upload,bg='brown',width=20,height=2)
    b3.place(x=130,y=350)
    b3=Button(root,text='BACK',command=bac,bg='GREEN',width=20,height=2)
    b3.place(x=130,y=460)

    root.mainloop()
def four():
    def send ():
        L=[]
        x=e1.get()
        import csv
        with open('allstudent.csv', 'r') as csvfil:
            csvread = csv.reader(csvfil)
            for row in csvread:
                if(len(row)!=0):
                    #print(row[0])
                    #print("yes")
                    if (row[0]==x):
                       # print(row)
                        L=row
            try :
                print("ID NO:-",L[0])
                print("NAME:-",L[1])
                print("BRANCH:-",L[2])
                print("DATE OF BIRTH:-",L[3])
                print("PHONE NO:-",L[4])
                print("EMAIL:-",L[5])
                print("BLOOD GROUP:-",L[6])
            except:
                print("invalid user")
                
    root=Tk()
    root.geometry('400x300')
    root.title("ALL STUDENT OF A PARTICULAR DATE")
    parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
    parent.pack(fill=tk.BOTH, expand=True)
    parent=Frame(root,bg='khaki')
    parent.pack()
    l=Label(root,text=" CREATED BY SUDHANSHU",font=("Comic Sans Ms", 18),height=1,bg='goldenrod')
    l.place(x=10,y=20)
    l2=Label(root,text=" ENTER ID NO",font=("Comic Sans Ms", 10),height=1,width=25,bg='goldenrod')
    l2.place(x=10,y=100)
    e1=Entry(root,bg='khaki',width=40)
    e1.place(x=220,y=100)

    b1=Button(root,text='SUBMIT',height=3,width=12,bg='brown2',command=send)
    b1.place(x=120,y=150)

    root.mainloop()



def five():
    x = PrettyTable()
    print("******************************* DETAILS OF ALL STUDENT ARE FOLLOWING ***************************************")

    x.field_names = ['ID NO',"NAME", "BRANCH", "D.O.B", "PHONE NO","EMAIL","BLOOD GROUP"]
    #print("**ALL DEATIL ARE IN THESE FORMAT ID NO,NAME,BRANCH,DATE OF BIRTH,PHONE NO,EMAIL,BLOOD GROUP\n\n")
    with open('allstudent.csv', 'r') as csvfil:
            csvread = csv.reader(csvfil)
            for row in csvread:
                if(len(row)!=0):
                    #print("yes")
                    if(len(row)!=0):
                        if (row[0]!= ''):
                            x.add_row(row)
    print(x)

def six():   
    y = PrettyTable()
    print("************************************  DETAILS OF STUDENT PRESENT ARE *********************************")
    y.field_names = ['ID NO',"NAME", "BRANCH", "D.O.B", "PHONE NO","EMAIL","BLOOD GROUP"]
    def send ():
        x=e1.get()
        import csv
        with open('abc.csv', 'r') as csvfil:
            csvread = csv.reader(csvfil)
            for row in csvread:
                if(len(row)!=0):
                    #print(row)
                    if (row[0]==x):
                        #print(row)
                        with open('allstudent.csv', 'r') as csvfi:
                            csvre=csv.reader(csvfi)
                            for rows in csvre:
                                #print(row)
                                if (len(rows)!=0):
                                    #print("yes")
                                    #print("row",row[1])
                                    #print("rows[1]",rows[0])
                                    if(row[1]==rows[0]):
                                        #print("yes")
                                        y.add_row(rows)
        print(y)
                                
                        
    root=Tk()
    root.geometry('400x300')
    root.title("ALL STUDENT OF A PARTICULAR DATE")
    parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
    parent.pack(fill=tk.BOTH, expand=True)
    parent=Frame(root,bg='khaki')
    parent.pack()
    l=Label(root,text=" CREATED BY SUDHANSHU",font=("Comic Sans Ms", 18),height=1,bg='goldenrod')
    l.place(x=10,y=20)
    l2=Label(root,text=" ENTER DATE in YYYY-MM-DD ",font=("Comic Sans Ms", 10),height=1,bg='goldenrod')
    l2.place(x=10,y=100)
    e1=Entry(root,bg='khaki',width=40)
    e1.place(x=220,y=100)

    b1=Button(root,text='SUBMIT',height=3,width=12,bg='brown2',fg="green",command=send)
    b1.place(x=120,y=150)

    root.mainloop()
def seven():
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    y = PrettyTable()
    print("***********  DETAILS OF ALL STUTENT ATTENDANCE PERCENTAGE  **************\n")
    y.field_names = ['ID NO',"NAME", "no of day present","attendance percentage"]
    import csv
    with open('allstudent.csv', 'r') as csvfil:
        csvread = csv.reader(csvfil)
        for row in csvread:
            if (len(row)!=0):
                if row[0]!='' :
                    #print(row[0])
                    count=0
                    l2.append(row[0])
                    l3.append(row[1])
                    with open("abc.csv","r") as csvf:
                        csvrea=csv.reader(csvf)
                        for rows in csvrea :
                            if (len(rows)!=0):
                                if rows[1]==row[0]:
                                    #print("yes")
                                    l1.append(rows[1])
                                    if rows[0] not in l4 :
                                        l4.append(rows[0])
    #print(l1)
    #print(l4)
    t=len(l4)
    for i in range(len(l2)):
        x=0
        x=l1.count(l2[i])
        percentage=(x/t)*100
        y.add_row([l2[i],l3[i],x,percentage])
    print(y)
root=Tk()
root.geometry('400x600')
root.title(" GRAPH ")
parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
parent.pack(fill=tk.BOTH, expand=True)
parent=Frame(root,bg='khaki')
parent.pack()
b1=Button(root,text=" GRAPH OF PARTICULAR STUDENT",bg='khaki',fg='red',height=3,width=35,command=send)
b1.place(x=90,y=20)
b2=Button(root,text=" GRAPH OF ALL DEPARTMENT",bg='khaki',fg='red',height=3,width=35,command=second)
b2.place(x=90,y=100)
b3=Button(root,text='CREATE STUDENT ID',height=3,width=35,bg='pink4',command=third)
b3.place(x=90,y=180)
b4=Button(root,text='DETAILS OF A PARTICULAR STUDENT',height=3,width=35,bg='pink4',command=four)
b4.place(x=90,y=260)
b5=Button(root,text='DETAILS OF ALL STUDENT',height=3,width=35,bg='orange red',fg='green',command=five)
b5.place(x=90,y=340)
b6=Button(root,text='DETAILS OF PRESENT  STUDENT',height=3,width=35,bg='orange red',fg='green',command=six)
b6.place(x=90,y=420)
b6=Button(root,text='PERCENTAGE OF ATTENDANCE OF ALL STUDENT',height=3,width=40,bg='tomato2',fg='yellow',command=seven)
b6.place(x=73,y=500)
root.mainloop()
