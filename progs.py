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
        while True:
            btext=input("Insert Code Here:")
            if not btext=="exit":
                bfile.write(btext)
            else:
                break