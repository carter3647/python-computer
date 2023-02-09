import os
import time
c=""
upd=""
osname=""
update=1
curdir=os.getcwd
def checksysfile(f):
    if os.path.exists(f):
        try:
            os.rename(f, f)
        except OSError as e:
            update=0
checksysfile("boot.update")
if update==1:
    try:
        c=open("boot.update")
        if c.readline()=="#updated version of bootloader":
            upd=input("New version of bootloader detected. Do you want to update?(y=yes n=no)|")
            if upd=="y":
                print("Updating bootloader")
                os.system("pyinstaller boot.py --onefile>nul")
                os.chdir("%appdata%\\Roaming\\Python\\dist")
                os.system("xcopy ./boot.exe "+curdir)
    except OSError as e:
            update=0
            os.system("boot.exe")
dir=""
os.system("cls")
dir=input("Input directory of programs(default is root directory):")
if dir=="":
    dir="./"
os.chdir(dir)
os.system("dir /w")
boot=input("Choose an operating system to boot to(must end in .exe):")
os.system("cls")
osw=open("loader.py","r")
osname=osw.readline()
osw.close()
osname=osname.replace("#","")
print("Booting to "+osname+" in 5 seconds.")
time.sleep(5)
os.system("cls")
os.system(boot)