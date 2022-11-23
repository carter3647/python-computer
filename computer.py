logusr="placeholder"
username="placeholder"
cfun="placeholder"
cval2=0
cval=0
d=False
TFI="0"
T3="placeholder"
T2="placeholder"
T1="placeholder"
TF="placeholder"
L1=2
p="placeholder"
running=1
ca="placeholder"
ci="placeholder"
while L1==2 :
    username=input("username|")
    ca=input("password|")
    print("hello "+str(username))
    L1=1
while L1==0 :
    print("signed in as "+str(username))
    ci=input("password|")
    if ci==ca :
        print("signing in")
        L1=1
    if not ci==ca :
        print("incorrect")
        exit()
while running==1 :
    print("(command list|[texedit][calculator][logoff])")
    p=input("type a command|")
    if p=="texedit" :
        TF=input("edit or open|")
        if TF=="edit" :
            TFI=input("1,2 or 3|")
            if TFI=="1" :
                print("opening file")
                T1=input("type here|")
            if TFI=="2" :
                print("opening file")
                T2=input("type here|")
            if TFI=="3" :
                print("opening file")
                T3=input("type here|")
        if TF=="open" :
            TFI=input("1,2 or 3|")
            if TFI=="1" :
                print("opening file")
                print(T1)
            if TFI=="2" :
                print("opening file")
                print(T2)
            if TFI=="3" :
                print("opening file")
                print(T3)
    if p=="logoff" :
        print("warning! this will logoff your session")
        d=bool(input("logoff? True/False|"))
        if d==True :
            print("erasing data")
            import time
            time.sleep(5)
            L1=0
            running=0
            while L1==0 :
                print("signed in as "+str(username))
                ci=input("password?|")
                if ci==ca :
                    print("signing in")
                    L1=1
                if not ci==ca :
                    print("wrong")
                    exit()
        if d==False :
            print("Termination Cancelled By User")
    if p=="calculator" :
        print("welcome to the calculator")
        cfun=input("input function|")
        if cfun=="multiplication" :
            cval=float(input("var 1?|"))
            cval2=float(input("var 2?|"))
            print(cval*cval2)
        if cfun=="division" :
            cval=float(input("var 1?|"))
            cval2=float(input("var 2?|"))
            print(cval/cval2)
        if cfun=="addition" :
            cval=float(input("var 1?|"))
            cval2=float(input("var 2?|"))
            print(cval+cval2)
        if cfun=="subtraction" :
            cval=float(input("var 1?|"))
            cval2=float(input("var 2?|"))
            print(cval-cval2)
