def fibb(n):
    a=0
    b=1

    if(n<0):
        print("incorrect")

    elif(n==0):
        return 0;

    elif(n==1):
        return b;
    else:
        for i in range(1, n-1):
            c=a+b
            a=b
            b=c
        return c
b=int(input("enter"))
print (fibb(b))