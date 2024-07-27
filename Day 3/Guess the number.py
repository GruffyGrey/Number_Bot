import random
num=random.randint(1,100)
won=False
for i in range(6):
    user_guess=int(input("Give me a number between 1 and 100: "))
    if user_guess<num:
        print("Too small")
    else:
        if user_guess>num:
            print("Too big")
        else:
            print("You got it")
            won=True
            break
if won==True:
    print("Congrats, you won!")
else:
    print("Sorry, you lost. The number was,",num)