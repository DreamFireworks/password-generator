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
window.geometry("220x300")
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

IntroText='''
*******************************
*PASSWORD GENERATOR v1*
***********Serhan Eraslan*****
'''

Intro = Label(window,text=IntroText,justify="center",
            bg="#eeefff",relief="groove")
Intro.place(x=5,
            y=5,
            width=200,
            height=50)
            
            
lower1 = IntVar()
lower_box = Checkbutton(window, text="Lower Case {abc...z}",justify="left")
lower_box.place(x=5,
                y=60,
                height=20)



upper1 = IntVar()
upper_box = Checkbutton(window, text="Upper Case {ABC...Z}", variable=lower1,justify="left")
upper_box.place(x=5,
                y=85,
                height=20)



num1 = IntVar()
num_box = Checkbutton(window, text="Numbers {0123456789}", variable=lower1,justify="left")
num_box.place(x=5,
              y=110,
              height=20)



symb1 = IntVar()
symbl_box = Checkbutton(window, text="Symbols {!@£$%^&*().,?/'}", variable=lower1,justify="left")
symbl_box.place(x=5,
                y=130,
                height=20)


generate = Button(window, text='Generate', command=psw,bg="#eeefff")
generate.place(x=5,
               y=180,
               width=100,
               height=30)


reset_button=Button(window, text='Reset', command=resett,bg="#eeefff")
reset_button.place(x=110,
                   y=180,
                   width=30,
                   height=30)

quit_Button= Button(window, text='Quit', command=window.quit,bg="#eeefff")
quit_Button.place(x=145,
                  y=180,
                  width=50,
                  height=30)

passw_show = Label(window,text="Password will shown here", bg="#eeefff", relief="groove")
passw_show.place(x=5,
                 y=210,
                 width=190,
                 height=40)


window.mainloop()










