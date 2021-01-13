import random
import time
import os
from datetime import datetime
path = os.getcwd()
print('''
***********************
*PASSWORD GENERATOR v1*
***********************
''')
chars = 'abcçdefgğhıijklmnopqrsştuüvwxyzABCÇDEFĞGHIİJKLMNOPQRSTUÜVWXYZ0123456789!@£$%^&*().,?/'
length = input('Lenght? : ')
length = int(length)
print('Password is : ')
password = ''
def psw(length):
  global password
  for i in range(length):
    password += random.choice(chars)
  return(password)
print("\t" + str(psw(length)))
now = datetime.now()
current_time = now.strftime("%D-(%H:%M:%S)")
f=open("pass.txt","a+")
f.write("Time: " + str(current_time) + " : ")
f.write(password)
f.write(""" 
""")
f.close()
print("'pass.txt' has been added to the: " + str(path))
time.sleep(10)