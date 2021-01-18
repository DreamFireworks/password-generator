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
lower = "abcçdefgğhıijklmnopqrsştuüvwxyz"
upper = "ABCÇDEFĞGHIİJKLMNOPQRSTUÜVWXYZ"
numbers = "0123456789"
symbols = " !@£$%^&*().,?/' "
length = input('Lenght? : ')
length = int(length)
pass_arr = [0,0,0,0]
try:
    lower_ask = input("Lower case? Y or N")
    if lower_ask != "Y" or lower_ask != "N":
        raise "input error"
    if lower_ask == 'Y':
        pass_arr[0] = 1
    elif lower_ask == "N":
        pass_arr[0] = 0
except:
    print("Error")

try:
    lower_ask = input("Upper case? Y or N")
    if lower_ask != "Y" or lower_ask != "N":
        raise "input error"
    if lower_ask == 'Y':
        pass_arr[1] = 1
    elif lower_ask == "N":
        pass_arr[1] = 0
except:
    print("Error")


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
