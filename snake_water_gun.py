
win=0
loss=0
count=0;
while count<4:

    print("select the s for snake w for water g for gun")
    user_choice = str(input(""))
    import random

    obtion = ["s", "w", "g"]
    com_choice = random.choice(obtion)

    if com_choice!=user_choice:
        print("comp choice is ",com_choice)
        if user_choice=='s' and com_choice=='w':
            print("you wuin")
            win=win+1

        elif user_choice=='w' and com_choice=='g':
            print("you win")
            win = win + 1

        elif user_choice=='g' and com_choice=='s':
            print("you win")
            win = win + 1

        else:
            print("you loss")
            loss = loss + 1

    else:
        print("match draw")
    count=count+1
    print("your choices are ", 4-count)

print("you win ", win)
print("you loss", loss)
if win>loss:
    print("finally you win")
else:
    print("finally comp win")




