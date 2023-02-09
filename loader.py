#InfinityOS
import os
def checksysfile(f):
    if os.path.exists(f):
        try:
            os.rename(f, f)
        except OSError as e:
            print('Access-error on system file "' + f + '"! \n' + str(e))
            if not f=="externalvars.py" or f=="progs.py":
                print("InfinityOS cannot find "+f+". The system will be shut down.")
                os.system("./boot.exe")
print("InfinityOS is starting")
print("Loading System Enviroment...")
checksysfile("vars.py")
exec(open("./vars.py").read())
print("Loading External Program Variables...")
checksysfile(".\\externalvars.py")
exec(open("externalvars.py").read())
print("Loading Programs...")
exec(open("./progs.py").read())
print("Loading InfinityOS Shell...")
checksysfile("./shell.py")
exec(open("shell.py").read())
os.system("cls")
