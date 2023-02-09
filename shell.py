#the actual InfinityOS shell
while L1==2 :
    print("welcome to InfinityOS")
    print("This shell is copyrighted from data saver by konrad edward burnett")
    startin=input("would you like to make a new user or input user number|")
    if startin=="new user":
        ufile=open('usernum.dat','r')
        unum=ufile.readline()
        if unum=="":
            unum=1
        ufile.close()
        unum=int(unum)+1
        username=input("username|")
        ca=input("password|")
        print("hello "+str(username))
        print("your user number is "+str(unum))
        L1=1
    if startin=="user number":
        getusernum=input("input user number|")
        file1=open('user'+unum+'.usr','r')
        username=file1.readline()
        ca=file1.readline()
        T1=file1.readline()
        T2=file1.readline()
        T3=file1.readline()
        file1.close()
        L1=1
    while L1==0:
        print("signed in as "+str(username))
        ci=input("password|")
        if ci==ca :
            cls()
            print("loading your personal settings")
            L1=1
        if not ci==ca :
            print("incorrect")
            exit()
while L1==1 :
    print(commands)
    p=input("type a command|")
    if p=="logoff" :
        print("this will logoff your InfinityOS session")
        d=bool(input("logoff? True/False|"))
        if d==True :
            print("logging off "+str(username))
            file1=open('user'+str(unum)+'.usr','a')
            save()
            ufile=open('usernum.dat','w')
            ufile.write(str(unum))
            ufile.close()
            unum=unum+1
            L1=0
            while L1==0 :
                print("signed in as "+str(username))
                ci=input("password?|")
                if ci==ca :
                    print("loading your personal settings")
                    L1=1
    #the programs that are already included in InfinityOS
    if p=="draw something" :
        if ds==1 :
            from turtle import*
            forward(200)
            left(90)
            forward(200)
            left(90)
            forward(200)
            left(90)
            forward(200)
            right(90)
            forward(200)
            left(90)
            forward(200)
            left(90)
            forward(200)
            left(90)
            forward(200)
            penup()
            forward(200)
            forward(100)
            left(90)
            pendown()
            forward(200)
            done()
        if ds==2 :
            from turtle import*
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
            forward(100)
            left(45)
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
    if p=="build" :
        print("Welcome to the Program Editor")
        print("A quick and easy-to-use program creator.")
        bname=input("What do you want to call your program?|")
        bfile=open(bname,'a')
        print("TIP:Type 'exit editor' to exit the Program Editor")
        while True:
            btext=input("Insert Code Here:")
            if not btext=="exit editor":
                bfile.write(btext)
            else:
                break
    if p=="command prompt":
        cmd=input("Type command|")
        if cmd=="exit":
            break
        else:
            os.system(cmd)
    #The external program loader
    if p=="external":
        if setup==1:
            rep=input("How many external programs")
            for i in range(rep):
                commands2.append(input("Name of program:"))
            setup=0
        print(commands2)
        p2=input("type an external command|")
        exec(open("externalvars.py").read())
        exec(open("progs.py").read())