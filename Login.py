import tkinter as tk
from tkinter import *
from random import *
import nexmo
from PIL import ImageTk,Image
import random
import csv
client = nexmo.Client(key='92261992', secret='YsbKyeldHOSvI1XC')
passwords=[('sud','123')]
#root.destroy()
OTP=str(random.randint(99999,9999999))
#ch= e2.get;

def make_entry(parent, caption, width=None,**options):
    tk.Label(parent, text=caption,bg='whitesmoke',fg='purple1').pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
#def enter(event):
 #   check_password()
def check_password():
    l=[user.get(),password.get()]
    with open('password.csv', 'r') as csvfil:
                csvreader = csv.reader(csvfil)
                for rows in csvreader:
                    try: 
                        print(rows);
                        print(l)
                        if (l == rows):
                            root.destroy()
                            print('Logged in')
                            import graph
                            return
                    except:
                        print("ACCESS DENIED")
                        root.destroy()


def reset_password():
    
    print(OTP)
    client.send_message({
        'from': 'S&B company',
        'to': '917087336269',
        'text': 'YOUR OTP IS:- '+str(OTP),
    })
    print("otp sent successfully")
def voice_otp():
    text="    your one time password is   "+str(random.randint(99999,9999999))

    client = nexmo.Client(
      application_id='e0c417f0-39c5-4f9d-948b-b67eea3a895c',
      private_key='C:/Users/Sudhanshu/Downloads/private.key',
    )
    ncco = [
      {
        'action': 'talk',
        'voiceName': 'S& B COMPANY',
        'text': text
      }
    ]
    response = client.create_call({
      'to': [{
        'type': 'phone',
        'number': '917087336269'
      }],
      'from': {
        'type': 'phone',
        'number': '917087336269'
      },
      'ncco': ncco
    })

    print("CALL SEND SUCCESSFULLY")   
def change_password():
    def submit():
        ch= e2.get();
        idno=e1.get();
        new_password=e3.get();
        row=[idno,new_password]
        if(ch==str(OTP)):
            print("success");
            with open('password.csv', 'r') as csvfil:
                csvreader = csv.reader(csvfil)
                for rows in csvreader:
                    print(rows)
                    if(len(rows)!=0):
                        if(rows[0]==idno):
                            print("success2")
                            with open('password.csv', 'w') as csvfil:
                                csvwriter = csv.writer(csvfil)
                                csvwriter.writerow(row)
                                print("data written successfully")
            
        else:
            print("not success");
            print(type(OTP));
            print(type(ch));
        
    
    root=Tk()
    root.geometry('550x400')
    root.title("attendance monitoring system")
    parent = Frame(root, padx=10, pady=10,bg='darkgoldenrod')
    parent.pack(fill=tk.BOTH, expand=True)
    parent=Frame(root,bg='khaki')
    parent.pack()
    l1=Label(root,text="CHANGE OR RESET YOUR PASSWORD",font=("Comic Sans Ms", 18),height=1,bg='goldenrod')
    l1.place(x=10,y=20)
    l2=Label(root,text="HEY ADMIN PLEASE ENTER YOUR ID NO",height=2,bg='goldenrod')
    l2.place(x=10,y=80)
    e1=Entry(root,bg='goldenrod',width=40)
    e1.place(x=300,y=85)
    b1=Button(root,text="sms otp",height=3,width=20,bg='light salmon',command=reset_password)
    b1.place(x=100,y=130)
    b2=Button(root,text="call ",height=3,width=20,bg='light salmon',command=voice_otp)
    b2.place(x=250,y=130)
    l3=Label(root,text="ENTER O.T.P.",height=2,width=30,bg='goldenrod')
    l3.place(x=20,y=200)
    e2=Entry(root,bg='goldenrod',width=40)
    e2.place(x=300,y=200)
    l4=Label(root,text="ENTER NEW PASSWORD",height=2,width=30,bg='goldenrod')
    l4.place(x=20,y=270)
    e3=Entry(root,bg='goldenrod',width=40)
    e3.place(x=300,y=270)
    '''canvas = Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("submit.png"))  
    canvas.create_image(20, 20, anchor=NW, image=img)'''
    #img2=Image(file="submit.png")
    b2=Button(root,text="SUBMIT",height=3,width=30,bg="light green",command=submit)
    b2.place(x=150,y=330)
    root.mainloop()

root = tk.Tk()
root.geometry('250x270',)
root.title('log in form')
parent = tk.Frame(root, padx=10, pady=10,bg='khaki')
parent.pack(fill=tk.BOTH, expand=True)
user = make_entry(parent, "User name:", 16)
password = make_entry(parent, "Password:", 16, show="*")
b2 = tk.Button(parent, borderwidth=4, text="Login",bg='lightseagreen',fg='yellow', width=10, pady=8, command=check_password)
b2.place(x=70,y=100)
b3 = tk.Button(parent, borderwidth=4, text="fogot password",bg='lightseagreen',fg='yellow', width=15, pady=8, command=change_password)
b3.place(x=50,y=150)
user.focus_set()
parent.mainloop()
