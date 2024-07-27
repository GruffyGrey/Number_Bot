import random,time
num=32
range1=1
range2=100
bot_guess=((range2+range1)//2)
print(bot_guess)
if bot_guess>num:
        range2=bot_guess-1
else:
    if bot_guess<num:
        range1=bot_guess+1
    else:
        if bot_guess==num:
            print("bot win")
time.sleep(1)
for i in range(9):
    bot_guess=random.randint(range1,range2)
    print(bot_guess)
    if bot_guess>num:
        range2=bot_guess-1
    else:
        if bot_guess<num:
            range1=bot_guess+1
        else:
            if bot_guess==num:
                print("bot win")
                break
    time.sleep(1)