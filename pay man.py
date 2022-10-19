from tkinter import *
import math,random
from tkinter import messagebox
import os
import smtplib
import random
import time
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen




root=Tk()


root.geometry("1920x1080+-10+0")
root.title("Employee Payment Management System By Osikhena")
root.config(width=1500,height=600, bg="#342D7E")
topFrame=Frame(root,bd=10,relief=RIDGE,bg='#342D7E')
topFrame.pack(side=TOP)
Labeltitle=Label(topFrame,text='Employee Payment Management System',font=('arial',30,'bold'),fg='#8B8000',bd=9,bg='#342D7E',width=51)
Labeltitle.grid(row=0,column=0)

#Frame
menuFrame=Frame(root,bd=0,relief=RIDGE,bg="#342D7E")
menuFrame.pack(side=LEFT)

fullnameFrame=LabelFrame(menuFrame,font=('arial',19,'bold'),bd=5,relief=SUNKEN,bg="#342D7E",fg='black')
fullnameFrame.pack(side=LEFT)

jobtitleFrame=LabelFrame(menuFrame,font=('arial',19,'bold'),bd=5,relief=SUNKEN,bg="#342D7E",fg='red4')
jobtitleFrame.pack(side=LEFT)


netpayFrame=LabelFrame(menuFrame,font=('arial',19,'bold'),bd=5,relief=SUNKEN,bg="#342D7E",fg='red4')
netpayFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=10,relief=GROOVE,bg='#342D7E')
rightFrame.pack(side=RIGHT)


payslipFrame=Frame(rightFrame,bd=4,relief=GROOVE,bg="#342D7E")
payslipFrame.pack()

ButtonFrame=Frame(rightFrame,bd=3,relief=GROOVE,bg="#342D7E")
ButtonFrame.pack()

#Details

labelfullname=Label(fullnameFrame,text="Full Name",font=('arial',16,'bold'),bg='#342D7E',fg='black')
labelfullname.grid(row=0,column=0)

textfullname=Entry(fullnameFrame,font=('arial',16,'bold' ),bd=6,width=20,)
textfullname.grid(row=0,column=1,padx=40)

labeljobtitle=Label(jobtitleFrame,text="Job Title",font=('arial',16,'bold'),bg='#342D7E',fg='black')
labeljobtitle.grid(row=0,column=1)

textjobtitle=Entry(jobtitleFrame,font=('arial',16,'bold' ),bd=6,width=10,)
textjobtitle.grid(row=0,column=3, padx=40)

labelnetpay=Label(netpayFrame,text="Net Pay",font=('arial',16,'bold'),bg='#342D7E',fg='Black')
labelnetpay.grid(row=0,column=4)

textnetpay=Entry(netpayFrame,font=('arial',16,'bold' ),bd=6,width=5)
textnetpay.grid(row=0,column=5, padx=40)

labelfullname=Label(fullnameFrame,text="Full Name",font=('arial',16,'bold'),bg='#342D7E',fg='black')
labelfullname.grid(row=0,column=0)

textfullname=Entry(fullnameFrame,font=('arial',16,'bold' ),bd=6,width=20,)
textfullname.grid(row=0,column=6,padx=40)

labeljobtitle=Label(jobtitleFrame,text="Job Title",font=('arial',16,'bold'),bg='#342D7E',fg='black')
labeljobtitle.grid(row=0,column=7)

textjobtitle=Entry(jobtitleFrame,font=('arial',16,'bold' ),bd=6,width=10,)
textjobtitle.grid(row=0,column=3, padx=40)

labelnetpay=Label(netpayFrame,text="Net Pay",font=('arial',16,'bold'),bg='#342D7E',fg='Black')
labelnetpay.grid(row=0,column=4)

textnetpay=Entry(netpayFrame,font=('arial',16,'bold' ),bd=6,width=5)
textnetpay.grid(row=0,column=5, padx=40)






root.mainloop()