import Commands as cmd
import subprocess as sp #Use this later as it seems more complex but worth it


print("\n")

cmd.start()
a = str(input(cmd.current()))
while a!= "exit":
    x = a.split()
    if not x:
        a = str(input(cmd.current()))
        continue
    elif x[0] == "cd": #works
        cmd.cd(a)
    elif x[0] == "ls": # works
        cmd.ls()
    elif x[0] == "run": #works?
        cmd.run(a)
    elif x[0] == "touch": #works
        cmd.touch(a)
    elif x[0] == "rm":
        cmd.rm()
    elif x[0] == "mkdir":
        cmd.mkdir(a)
    elif x[0] == "mv":
        cmd.mv(a)
    elif x[0] == "cp":
        cmd.cp(a)
    elif x[0] == "rmdir":
        cmd.rmdir(a)
    elif x[0] == "findext":
        cmd.findext(a)
    else:
        cmd.search(a)
    a = str(input(cmd.current()))

