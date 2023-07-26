
n=18
num_of_gausses=1
while(num_of_gausses<=9):
    num_gauss=int(input("enter num beetween 1 to 100\n"))
    if num_gauss<18:
        print("small")
    elif num_gauss>18:
        print("large")
    else:
        print("you win")
        print(num_of_gausses ,"num of gausses")
        break
    num_of_gausses=num_of_gausses+1

if num_of_gausses>9:
    print("game over")