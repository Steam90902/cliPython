import time
import subprocess as sp #Use this later as it seems more complex but worth it
import os
import matcher
import shutil
print("\n")

#print(os.getcwd()) # i forgot /
#os.mkdir("Sigma") # makes a folder
#print(os.listdir()) # lists current dir /
#os.remove("Sigma") #removes files
#print(os.listdir())
#os.rmdir("Sigma") #removes folders
#os.rename([initial name], [changed name]) #renames a file
#as.system(filename) #runs a file


def cd(item): #opens or backs out of a dir
    x = item.split(" ", 1)
    if len(x) > 1:
        if os.path.exists(x[1]):
            x = x[1]
            c = str(os.getcwd())
            o = [c, x]
            os.chdir("/".join(o))
        else:
            print("That file doesnt exist (maybe you got the name wrong?)")
    else:
        c = str(os.getcwd()).split("/")
        if len(c) >= 3:
            #print(c)
            c.pop(-1)
            os.chdir("/".join(c))
        else:
            print("You cant go any further")

def ls(): #lists the current dir
    print(os.listdir())

def search(item): #Just confirms if a file is there
    if os.path.exists(item):
        print(f"{item} is present")
    else:
        print(f"Sorry! {item} is not here!")

def run(item): #should run a file, currently not working
    x = item.split(" ", 1)
    x = x[1]
    os.system(x)

def rm(item): #removes a file NOT a folder
    x = item.split(" ", 1)
    n = x[1]
    if os.path.exists(n):
            os.remove(n)
            print(f"{n} deleted")
    else:
        print("That file doesnt exist (maybe you got the name wrong?)")

def touch(item): #creates a file 
    conf = str(input(f"confirm you want to create a file? (y/n)"))
    if conf == "yes" or conf == "y":
        x = item.split(" ", 1)
        x = x[1]
        os.system("touch {}".format(x))
    else:
        print(" ")

def cNextDir(subItem):
    i = os.getcwd()
    ko = i + "/" + subItem
    return ko

def mkdir(item): # creates a folder
    x = item.split(" ", 1)
    if len(x) == 2:
        x = x[1]
        os.mkdir(x)
    else:
        os.mkdir("Untitled")

def mv(item): # moves files 
    x = item.split(" ", 1)
    x = x[1]
    os.system("mv {}".format(x))
    
def cp(item):
    x = item.split(" ", 1)
    x = x[1]
    x = x.split(" -/- ", 1)
    st = x.pop(0)
    des = x.pop(0)
    #print(st)
    #print(des)
    if "/home" in st and "/home" in des:
        shutil.copy2(st, des)
        print("Files have been copied")
    else:
        print("No paths detected")

def rmdir(item):
    x = item.split(" ", 1)
    n = x[1]
    if os.path.exists(n):
        if len(os.listdir(cNextDir(n))) == 0:
            os.rmdir(n)
            print(f"{n} deleted")
        else:
            print(f"There may be some files inside")
    else:
        print("That folder doesnt exist (maybe you got the name wrong?)")

def wc(item):
    x = item.split(" ", 1)
    x = x[1]
    os.system("wc {}".format(x))

def findext(item):
    g = item.split(" ", 1)
    g = g[1]
    i = list(os.listdir())
    l = []
    for x in i:
        if x.endswith(g):
            l.append(x)
    print(l)


os.chdir("/home")
a = str(input(f"{os.getcwd()}/ "))
while a!= "exit":
    x = a.split()
    if x[0] == "cd":
        cd(a)
    elif x[0] == "ls":
        ls()
    elif x[0] == "run":
        run(a)
    elif x[0] == "touch":
        touch(a)
    elif x[0] == "rm":
        rm(a)
    elif x[0] == "mkdir":
        mkdir(a)
    elif x[0] == "mv":
        mv(a)
    elif x[0] == "cp":
        cp(a)
    elif x[0] == "rmdir":
        rmdir(a)
    elif x[0] == "findext":
        findext(a)
    else:
        search(a)
    a = str(input(f"{os.getcwd()}/ "))

