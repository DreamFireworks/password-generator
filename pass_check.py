import re
import getpass
print("Please Enter your password below ")
passwd = getpass.getpass()
print("Your password is {}".format(len(passwd)*"*"))

if re.match("[A-Za-z0-9]",passwd) is not None:
    print("Your password is strong")
else:
    print("You have to find a stronger password")