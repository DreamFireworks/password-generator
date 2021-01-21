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
window.geometry("220x260")
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
  passw_show.configure(state="normal")
  var_states()
  global choices
  password=""
  for i in range(int(lenght_entry.get())):
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
  passw_show.delete(1.0,100.0)
  passw_show.insert(1.0,password)
  passw_show.configure(state="disabled")
  messagebox.showinfo("Done","'pass.txt' has been added to the: " + str(path))
  

def resett():
    global choices
    global password
    choices=""
    password=""
    passw_show.insert(1.0,"Password will shown here")

IntroText='''
*******************************
*PASSWORD GENERATOR v1*
*************Serhan Eraslan****
'''

Intro = Label(window,text=IntroText,justify="center",
            bg="#eeefff",relief="groove")
Intro.place(x=5,
            y=5,
            width=210,
            height=50)
            
lenght_label = Label(window, text="Lenght")
lenght_label.place(x=5,
                   y=60,
                   height=20)           

lenght_entry=Entry(window,
              justify="center",
              bg="#dedede")
lenght_entry.insert(0, '8')
lenght_entry.place(x=120,
                   y=60,
                   width=90,
                   height=20)

            
lower1 = IntVar()
lower_box = Checkbutton(window, text="Lower Case {abc...z}",justify="left")
lower_box.place(x=5,
                y=85,
                height=20)



upper1 = IntVar()
upper_box = Checkbutton(window, text="Upper Case {ABC...Z}", variable=upper1,justify="left")
upper_box.place(x=5,
                y=110,
                height=20)



num1 = IntVar()
num_box = Checkbutton(window, text="Numbers {0123456789}", variable=num1,justify="left")
num_box.place(x=5,
              y=135,
              height=20)



symb1 = IntVar()
symbl_box = Checkbutton(window, text="Symbols {!@£$%^&*().,?/'}", variable=symb1,justify="left")
symbl_box.place(x=5,
                y=160,
                height=20)


generate = Button(window, text='Generate', command=psw,bg="#eeefff")
generate.place(x=5,
               y=185,
               width=100,
               height=30)


reset_button=Button(window, text='Reset', command=resett,bg="#eeefff")
reset_button.place(x=110,
                   y=185,
                   width=50,
                   height=30)

quit_Button= Button(window, text='Quit', command=window.quit,bg="#eeefff")
quit_Button.place(x=165,
                  y=185,
                  width=50,
                  height=30)

passw_show = Text(window)
passw_show.place(x=5,
                 y=210,
                 width=210,
                 height=40)
passw_show.configure(bg=window.cget('bg'), relief="groove")
passw_show.insert(1.0,"Password will shown here")


window.mainloop()










