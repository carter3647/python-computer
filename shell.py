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