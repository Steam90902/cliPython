import shutil
import os
from matcher import wrongDir

def cNextDir(subItem):
    i = os.getcwd()
    ko = i + "/" + subItem
    return ko

def alreadyHere(subItem):
    if os.path.exists(subItem):
        return True
    else:
        return False

def current():
    return f"{os.getcwd()}/ "

def start():
    os.chdir("/home")

#def optDir():
    #return os.listdir()
   
#def optCmd():
    #cmd = ["cd", "ls", "search", "run", "rm", "touch", "mkdir", "mv", "cp", "rmdir", "findext"]
    #return cmd
#-----------------------------------------------------




def cd(item): #opens or backs out of a dir
    x = item.split(" ", 1)
    if len(x) > 1:
        if os.path.exists(x[1]):
            x = x[1]
            c = str(os.getcwd())
            o = [c, x]
            os.chdir("/".join(o))
        else:
            print(f"That file doesnt exist (maybe you meant {wrongDir(x[1])})")
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
    if item != "":
        if os.path.exists(item):
            print(f"{item} is present")
        else:
            print(f"Sorry! {item} is not here! Perhaps you meant {wrongDir(item)}")

def run(item): #should run a file or even a normal command
    x = item.split(" ", 1)
    if len(x) == 2:
        if shutil.which(x[1]) is None:
            print(f"No executable found for command {x[1]}")
        else:
            os.system(x[1])
    else:
        print("No arguments found")

def rm(item): #removes a file NOT a folder
    x = item.split(" ", 1)
    if len(x) == 2:
        n = x[1]
        if os.path.exists(n):
                conf = str(input(f"confirm you want to delete {n}? (y/n)"))
                if conf == "yes" or conf == "y":
                    os.remove(n)
                    print(f"{n} deleted")
        else:
            print(f"{n} doesnt exist (maybe you meant {wrongDir(x[1])})")
    else:
        print("Not enough arguments")

def touch(item): #creates a file 
    x = item.split(" ", 1)
    if len(x) == 2 and alreadyHere(x[1]) == False:
        conf = str(input(f"confirm you want to create a file? (y/n)"))
        if conf == "yes" or conf == "y":
            x = x[1]
            os.system("touch {}".format(x))
        else:
            print(" ")
    else:
        print("Not enough arguments")
 
def mkdir(item): # creates a folder
    x = item.split(" ", 1)
    conf = str(input(f"confirm you want to create a folder? (y/n)"))
    if conf == "yes" or conf == "y":
        if len(x) == 2 and alreadyHere(x[1]) == False:
            x = x[1]
            os.mkdir(x)
        elif alreadyHere("Untitled") == False and len(x) == 1:
            os.mkdir("Untitled")
        else:
            print("No file created (Name taken)")

def mv(item): # moves files 
    try:
        x = item.split(" ", 1)
        if len(x) == 2:
            x = x[1]
            x = x.split(" -/- ", 1)
            fail = "Usage: mv source -/- destination"
            st = x.pop(0)
            des = x.pop(0)
            #print(st)
            #print(des)
            if os.path.exists(st):
                os.replace(st, des)
                print("Files have been moved")
            else:
                print(f"{fail} \n Maybe you got the path wrong?")
        else:
            print(f"{fail} \n Maybe you didnt put enough arguments?")
    except:
        print("An error has occured")
    
def cp(item): #copies files 
    try:
        x = item.split(" ", 1)
        fail = "Usage: cp source -/- destination"
        if len(x) == 2:
            x = x[1]
            x = x.split(" -/- ", 1)
            st = x.pop(0)
            des = x.pop(0)
            #print(st)
            #print(des)
            if os.path.exists(st):
                shutil.copy2(st, des)
                print("Files have been copied")
            else:
                print(f"{fail} \n Maybe you got the path wrong?")
        else:
            print(f"{fail} \n Maybe you didnt put enough arguments?")
    except:
        print("An error has occured")

def rmdir(item): # removes folders
    x = item.split(" ", 1)
    n = x[1]
    if os.path.exists(n):
        conf = str(input(f"confirm you want to delete {n}? (y/n)"))
        if conf == "yes" or conf == "y":
            if len(os.listdir(cNextDir(n))) == 0:
                os.rmdir(n)
                print(f"{n} deleted")
            else:
                print(f"There may be some files inside")
    else:
        print(f"{n} doesnt exist (maybe you meant {wrongDir(n)}?)")

def findext(item): # finds files with given extension
    try:
        def ext(i):
            if x.endswith(i):
                l.append(x)
        g = item.split(" ", 1)
        if len(g) == 2:
            g = g[1]
            o = list(os.listdir())
            l = []
            if g[0] == ".":
                for x in o:
                    ext(x)
            else:
                j = "." + g
                for x in o:
                    ext(j)
            print(l)
    except:
        print("An error has occured")
