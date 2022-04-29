import subprocess
import platform
import socket
import time
import os
import touch
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Cyber Terminal [Version 1.00]")
while True:
    code = input(">>> ")
    if "echo" in str(code):
        print(code.split("echo")[1])
    if "touch" in str(code):
        a = code.split("touch ")[1]
        touch.touch(a)
    if "mkdir" in str(code):
        m = code.split("mkdir ")[1]
        os.mkdir(m)
    if "rmdir" in str(code):
        m = code.split("rmdir ")[1]
        os.rmdir(m)
    if "rm" in str(code):
        m = code.split("rm ")[1]
        os.remove(m)
    if "cat" in str(code):
        file = input()
        f = open(file, "r")
        text = f.read()
        print (text)
        
        '''text = input("What do you want to write")
        file = input()'''
        file2 = input()
        #f2 = open(file2, "r")
        #lines = ['Readme', 'How to write text files in Python']
        with open(file2, 'w') as f2:
            #f2.write('\n'.join(text))
            f2.write(text)
            f2.close()
        f.close()

        
    if "cd" in str(code):
        m = code.split("cd ")[1]
        os.chdir(path)