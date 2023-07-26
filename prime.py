num =int(input("enter the num: "))
if(num < 1):
    print("not prime")
if(num>1):
    for i in range (2 , num):
        if(num%i==0):
            print("Note prime")
            break
    else:
            print("prime")
