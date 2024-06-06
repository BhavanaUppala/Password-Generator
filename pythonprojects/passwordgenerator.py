import random
import string
n=int(input("Enter number of password you required:5"))
pass_len=int(input("Enter the length of pasword:"))
char=string.ascii_letters + string.digits + string.punctuation

password=""
i=0
while i<n:
    for val in range(pass_len):
        
        password+=random.choice(char)
    print(password)
    i+=1
    password=""
