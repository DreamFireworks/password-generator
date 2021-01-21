import keyboard
import pyautogui 
import random
import time
import os
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
path = os.getcwd()
  
lower="abcçdefgğhıijklmnopqrsştuüvwxyz"       
upper = "ABCÇDEFĞGHIİJKLMNOPQRSTUÜVWXYZ"
numbers = "0123456789"
symbols = "!@£$%^&*().,?/' "


window = Tk()
window.geometry("500x200")
window.title("Password Generator By Serhan Eraslan")
window.resizable(width=False,
                 height=False)
choices=""                 
res=[1,0,0,0]

def var_states():
   global res
   global choices
   print("{}{}{}{}".format(lower1.get(), upper1.get(), num1.get(), symb1.get()))
   res=[int(lower1.get()), int(upper1.get()), int(num1.get()), int(symb1.get())]
   if(res[0] == 1):
    choices = choices + lower
    choices="".join(choices)
   if(res[1] == 1):
    choices = choices + upper
    choices="".join(choices)
   if(res[2] == 1):
    choices = choices + numbers
    choices="".join(choices)
   if(res[3] == 1):
    choices = choices + symbols
    choices="".join(choices)
   if(res == [0,0,0,0]):
    choices = choices + lower
    choices="".join(choices)

  
def psw():
  var_states()
  global choices
  password=""
  for i in range(8):
    password += random.choice(choices)
  print(choices)
  print(password)
  now = datetime.now()
  current_time = now.strftime("%D-(%H:%M:%S)")
  f=open("pass.txt","a+")
  f.write("Time: " + str(current_time) + " : ")
  f.write(password)
  f.write("\n")
  f.close()
  messagebox.showinfo("Done","'pass.txt' has been added to the: " + str(path))

def resett():
    global choices
    global password
    choices=""
    password=""



Checkbutton(window,  variable=upper1).grid(row=3, sticky=W)
num1 = IntVar()
Checkbutton(window,  variable=num1).grid(row=4, sticky=W)
symb1 = IntVar()
Checkbutton(window,  variable=symb1).grid(row=5, sticky=W)
Button(window, text='Reset', command=resett).grid(row=8,column=1, sticky=W, pady=4)
Button(window, text='Quit', command=window.quit).grid(row=8,column=2, sticky=W, pady=4)
Button(window, text='Generate', command=psw).grid(row=7, sticky=W, pady=4)
label1 = Label(window,text="Password")
label1.grid(row=6,sticky=W, pady=4)

window.mainloop()


IntroText='''
***********************
*PASSWORD GENERATOR v1*
********Serhan Eraslan*
'''

Intro = Label(window,Text=IntroText)
Intro.place(x=5,
            y=0,
            width=190,
            height=50,
            justify="center",
            bg="#efefef")
            
            
lower1 = IntVar()
lower_box = Checkbutton(window, text="Lower Case {abc...z}", variable=lower1)
lower_box.place(row=2, sticky=W)


upper1 = IntVar()
upper_box = Checkbutton(window, text="Upper Case {ABC...Z}", variable=lower1)
upper_box.place(x=60,
            y=0,
            width=190,
            height=20,
            bg="#efefef")



num1 = IntVar()
num_box = Checkbutton(window, text="Numbers {0123456789}", variable=lower1)
num_box.place(x=85,
            y=0,
            width=190,
            height=20,
            bg="#efefef")



symb1 = IntVar()
symbl_box = Checkbutton(window, text="Symbols {!@£$%^&*().,?/'}", variable=lower1)
symbl_box.place(x=110,
            y=0,
            width=190,
            height=20,
            bg="#efefef")


























