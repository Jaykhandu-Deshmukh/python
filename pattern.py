num=int(input("enter the num"))
num2=int(input("enter o or 1"))


if num2==0:

    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("")



if num2==1:
        for i in range(1 + num, 1, -1):
            for j in range(1 + i, 2, -1):
                print("*", end="")
            print("")



print("end")

