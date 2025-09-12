import time
import subprocess as sp #Use this later as it seems more complex but worth it
import os

print("\n")
#print(os.getcwd()) # i forgot
#os.mkdir("Sigma") # makes a folder
#print(os.listdir()) # lists current dir
#os.remove("Sigma") #removes files
#print(os.listdir())
#os.rmdir("Sigma") #removes folders
#os.rename([initial name], [changed name]) #renames a file


def cd(cmd):
    x = cmd.split(" ", 1)
    if len(x) > 1:
        x = x[1]
        c = str(os.getcwd())
        o = [c, x]
        os.chdir("/".join(o))
    else:
        c = str(os.getcwd()).split("/")
        c.pop(-1)
        os.chdir("/".join(c))

def ls():
    print(os.listdir())




os.chdir("/home/gaba-jm")
a = str(input(os.getcwd() + "/ "))
while a!= "exit":
    x = a.split()
    if x[0] == "cd":
        cd(a)
    elif x[0] == "ls":
        ls()
    a = str(input(os.getcwd() + "/" ))

