from tkinter import *
import tkinter as tk            
import urllib.request               
import json                      
import time                         
import csv              
from firebase import firebase       
from playsound import playsound     
firebase=firebase.FirebaseApplication('https://team54-b72f8.firebaseio.com/')

READ_API_KEY='JBVYHRSGFNUESU3N'
CHANNEL_ID= '812705'
fields=['time','id no']

c=[]
x=0
count=0


while True:
    TS = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)
    #data=json.loads(response.decode('utf-8'))
    a = data['created_at']
    b = data['field1']
    #print("a",a)
    a=a[:10]
    c=b[-1:-11:-1]
    c=c[::-1]
    b='ID'+b[-8:-1:+1]+b[-1]
    #print('value a',a)
    #print('value b',b)
    #print('value of c',c)
    rows=[a]
    fields = []
    with open('allstudent.csv', 'r') as csvfil:
        csvreader = csv.reader(csvfil)
        for row in csvreader:
            #print(row[])
            #print(row)
            if len(row)!=0:
                if b in row[0]:
                    #print('yes')
                    rows.append(b)
                    rows.append(row[2])
                    #print('kk',row[1],row[5])
                    with open ('abc.csv','r')as check:
                        csvrea=csv.reader(check)
                        if rows not in csvrea:
                            with open('abc.csv', 'a') as csvfile: 
                                csvwriter = csv.writer(csvfile) 
                                #csvwriter.writerow(fields) 
                                csvwriter.writerow(rows)
                                #print(rows)
                                #print(b)
                                result=firebase.put('attendace'+a,b,{"name":row[1],'email':row[5]})
                                playsound("welcome2.mp3")
                                print(result)
                                try:
                                    import smtplib 
                                    gmailaddress = 'sudhanshubhardwaj999@gmail.com'
                                    gmailpassword = '2hateyou@'
                                    print(row[5])
                                    mailto = row[5]
                                    msg = 'your ward come today'
                                    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                                    mailServer.starttls()
                                    mailServer.login(gmailaddress , gmailpassword)
                                    mailServer.sendmail(gmailaddress, mailto , msg)
                                    print(" \n email send to his parent successfully!")
                                    mailServer.quit()
                                except:
                                    print('invalid mail')
                if  c in row[0]:
                    #print('yes C')
                    rows.append(c)
                    rows.append(row[2])
                    #print(rows)
                    #print('kk',row[1],row[5])
                    with open ('abc.csv','r')as check:
                        csvrea=csv.reader(check)
                        if rows not in csvrea:
                            #print("csv")
                            with open('abc.csv', 'a') as csvfile: 
                                csvwriter = csv.writer(csvfile) 
                                #csvwriter.writerow(fields) 
                                csvwriter.writerow(rows)
                                #print(rows)
                                #print(b)
                                result=firebase.put('attendace'+a,c,{"name":row[1],'email':row[5]})
                                print(result)
                                playsound("welcome2.mp3")
                                '''import RPi.GPIO as GPIO     
                                import time                 

                                GPIO.setmode(GPIO.BOARD)     
                                GPIO.setup(11,GPIO.OUT)      

                                GPIO.output(11,1)            
                                time.sleep(1)
                                GPIO.output(11,0)
                                time.sleep(1)                
                                GPIO.cleanup()   '''   
                                print("attendance done successfully")
                                try:
                                    import smtplib #FOR SEND EMAIL
                                    gmailaddress = 'sudhanshubhardwaj999@gmail.com'
                                    gmailpassword = '2hateyou@'
                                    print(row[5])
                                    mailto = row[5]
                                    msg = 'your ward come today'
                                    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                                    mailServer.starttls()
                                    mailServer.login(gmailaddress , gmailpassword)
                                    mailServer.sendmail(gmailaddress, mailto , msg)
                                    print(" \n email send to his parent successfully!")
                                    mailServer.quit()
                                except:
                                    print('invalid mail')
                        else:
                            print("no new student come")
                            '''import RPi.GPIO as GPIO     
                            import time                 2

                            GPIO.setmode(GPIO.BOARD)     
                            GPIO.setup(13,GPIO.OUT)
                            GPIO.output(13,1)            
                            time.sleep(1)
                            GPIO.output(13,0)
                            time.sleep(1)                
                            GPIO.cleanup()'''      
           # else: print("invalid user\n scan again")

    l=[]
    q=[]
    counts=[]
    '''with open('abc.csv', 'r') as csvfil:
        csvreader = csv.reader(csvfil)
        for rows in csvreader:
            if len(rows)!=0:
                l.append(rows[1])
                if rows[1] not in q:
                    q.append(rows[1])

                l=sorted(l)
        for i in range(len(q)):
            counts.append(l.count(q[i]))'''
    #send_data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=7DOUDTFSQKET5TWW&field2="+str(100))
                
    '''print(l)
            print(q)
            print(counts)'''
       
        
            
    time.sleep(1)   

    TS.close()

