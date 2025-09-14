from rapidfuzz import process, fuzz, utils
#from Commands import optCmd, optDir
import os

def optDir():
    return os.listdir()

def optCmd():
    cmd = ["cd", "ls", "search", "run", "rm", "touch", "mkdir", "mv", "cp", "rmdir", "findext"]
    return cmd

def wrongCmd(item):
    a = process.extractOne(item, optCmd(), scorer=fuzz.WRatio, processor=utils.default_process)
    print(f"You havent typed in a viable command, did you mean ({a[0]})")

def wrongDir(item):
    a = process.extractOne(item, optDir(), scorer=fuzz.WRatio, processor=utils.default_process)
    return a[0]