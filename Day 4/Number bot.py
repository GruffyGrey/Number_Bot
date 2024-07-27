# Ideas

# 001 - create a counter that adds up the number of times that the bot guesses - so in our case the bot guessed 10 times total to get the right answer

# Import of random give acces to the abilty to use RNG and the import of time gives acces to the pause feature
import random,time
win=0

# The first number in a range is decided by the user
Range1=int(input("You are going to give me a range of numbers, please provide the lowest number in the range: "))
for i in range(1000000000000000000000000000):
    # if Range1<0 or Range1==0:
    if Range1<=0:     
        print("Number to small")
        time.sleep(0.25)
        Range1=int(input("You are going to give me a range of numbers, please provide the lowest number in the range: "))
    else:
        break
time.sleep(0.5)

# The second number in a range is decided by the user
Range2=int(input("Give me a number: "))
for i in range(1000000000000000000000000000):
    if Range2<Range1 or Range2==Range1:
        print("Number to small")
        time.sleep(0.25)
        Range2=int(input("Give me a number: "))
    else:
        break
time.sleep(0.5)

# The user decides a number in the range they decided
print("Give me a number betweeen",Range1,"and",Range2,":")
Num=int(input(" "))
for i in range(1000000000000000000000000000):
    if Num<Range1 or Num>Range2:
        print("Number not in range")
        time.sleep(0.25)
        print("Give me a number betweeen",Range1,"and",Range2,":")
        Num=int(input(" "))
    else:
        break
time.sleep(0.5)
for i in range(1000000000000000000000000000):
    Game_gueses=int(input("Give me a number: "))
    if Game_gueses==0 or Game_gueses<0:
        print("Number to small")
        time.sleep(0.25)
        Game_gueses=int(input("Give me a number: "))
    else:
        break
time.sleep(0.5)

# The user is asked if they are ready to start the game
Ready=input("Ready?(Yes/No) ")

# If the user is not ready, then they will deccide the range and number all over again
for i in range(1000000000000000000000000000):
    if Ready=="No"or Ready=="no":
        time.sleep(0.5)
        Range1=int(input("Give me a number: "))
        for i in range(1000000000000000000000000000):
            if Range1<0 or Range1==0:
                print("Number too small")
                time.sleep(0.25)
                Range1=int(input("Give me a number: "))
            else:
                break
        time.sleep(0.5)
        Range2=int(input("Give me a number: "))
        for i in range(1000000000000000000000000000):
            if Range2<Range1 or Range2==Range1:
                print("Number too small")
                time.sleep(0.25)
                Range2=int(input("Give me a number: "))
            else:
                break
        time.sleep(0.5)
        print("Give me a number betweeen",Range1,"and",Range2,":")
        Num=int(input(" "))
        for i in range(1000000000000000000000000000):
            if Num<Range1 or Num>Range2:
                print("Number not in range")
                time.sleep(0.25)
                print("Give me a number betweeen",Range1,"and",Range2,":")
                Num=int(input(" "))
            else:
                break
        time.sleep(0.5)
        for i in range(1000000000000000000000000000):
            Game_gueses=int(input("Give me a number: "))
            if Game_gueses==0 or Game_gueses<0:
                print("Number too small")
                time.sleep(0.25)
                Game_gueses=int(input("Give me a number: "))
            else:
                break
        Ready=input("Ready?(Yes/No) ")
    else:

        # If the user is ready to start the game, the game will begin
        if Ready=="Yes"or Ready=="yes":
            time.sleep(0.5)
            print("A bot will begin to guess your number.")
            break
        else:
            print("Answer not recognised")
            time.sleep(0.25)
            Ready=input("Ready?(Yes/No) ")

# Bot imedietly guesses in the middle to thin down the numbers neede by half
guess=((Range2+Range1)//2)
print(guess)
if guess==Num:
    print("I win")
    win=1
else:
    if guess>Num:
        print("Too big")
        Range2=guess-1
    else:
        if guess<Num:
            print("Too small")
            Range1=guess+1
# User is asked to continue the game or not
for i in range(1000000000000000000000000000):
    
    time.sleep(1)
    Ready2=input("Continue?(Yes/No) ")
    if Ready2=="Yes"or Ready2=="yes":
        print("continuing")
        break
    else:

# If not, then they will repeat all over
        if Ready2=="No"or Ready2=="no":
            time.sleep(0.5)
            Range1=int(input("Give me a number: "))
            for i in range(1000000000000000000000000000):
                if Range1<0 or Range1==0:
                    print("Number to small")
                    time.sleep(0.25)
                    Range1=int(input("Give me a number: "))
                else:
                    break
            time.sleep(0.5)

            # The second number in a range is decided by the user
            Range2=int(input("Give me a number: "))
            for i in range(1000000000000000000000000000):
                if Range2<Range1 or Range2==Range1:
                    print("Number to small")
                    time.sleep(0.25)
                    Range2=int(input("Give me a number: "))
                else:
                    break
            time.sleep(0.5)

            # The user decides a number in the range they decided
            print("Give me a number betweeen",Range1,"and",Range2,":")
            Num=int(input(" "))
            for i in range(1000000000000000000000000000):
                if Num<Range1 or Num>Range2:
                    print("Number not in range")
                    time.sleep(0.25)
                    print("Give me a number betweeen",Range1,"and",Range2,":")
                    Num=int(input(" "))
                else:
                    break
            time.sleep(0.5)
            for i in range(1000000000000000000000000000):
                Game_gueses=int(input("Give me a number: "))
                if Game_gueses==0 or Game_gueses<0:
                    print("Number to small")
                    time.sleep(0.25)
                    Game_gueses=int(input("Give me a number: "))
                else:
                    break
            time.sleep(0.5)

            # The user is asked if they are ready to start the game
            Ready=input("Ready?(Yes/No) ")

            # If the user is not ready, then they will deccide the range and number all over again
            for i in range(1000000000000000000000000000):
                if Ready=="No"or Ready=="no":
                    time.sleep(0.5)
                    Range1=int(input("Give me a number: "))
                    for i in range(1000000000000000000000000000):
                        if Range1<0 or Range1==0:
                            print("Number too small")
                            time.sleep(0.25)
                            Range1=int(input("Give me a number: "))
                        else:
                            break
                    time.sleep(0.5)
                    Range2=int(input("Give me a number: "))
                    for i in range(1000000000000000000000000000):
                        if Range2<Range1 or Range2==Range1:
                            print("Number too small")
                            time.sleep(0.25)
                            Range2=int(input("Give me a number: "))
                        else:
                            break
                    time.sleep(0.5)
                    print("Give me a number betweeen",Range1,"and",Range2,":")
                    Num=int(input(" "))
                    for i in range(1000000000000000000000000000):
                        if Num<Range1 or Num>Range2:
                            print("Number not in range")
                            time.sleep(0.25)
                            print("Give me a number betweeen",Range1,"and",Range2,":")
                            Num=int(input(" "))
                        else:
                            break
                    time.sleep(0.5)
                    for i in range(1000000000000000000000000000):
                        Game_gueses=int(input("Give me a number: "))
                        if Game_gueses==0 or Game_gueses<0:
                            print("Number too small")
                            time.sleep(0.25)
                            Game_gueses=int(input("Give me a number: "))
                        else:
                            break
                    Ready=input("Ready?(Yes/No) ")
                else:

                    # If the user is ready to start the game, the game will begin
                    if Ready=="Yes"or Ready=="yes":
                        time.sleep(0.5)
                        print("A bot will begin to guess your number.")
                        break
                    else:
                        print("Answer not recognised")
                        time.sleep(0.25)
                        Ready=input("Ready?(Yes/No) ")
        else:
            print("Awnswer not recognised")
            Ready2=input("Continue?(Yes/No) ")
for i in range (Game_gueses-2):

# Main game loop, bot guesses number, than decides if it was too high or too low, it will do number higher or lower depending on the awnswer
    if win==0:
        if Ready=="Yes"or Ready=="yes":
            time.sleep(1)
            guess=random.randint(Range1,Range2)
            print("Guess:",guess)
            time.sleep(1)
            if guess==Num:
                print("I win")
                win=1
                break
            else:
                if guess>Num:
                    print("Too big")
                    Range2=guess-1
                else:
                    if guess<Num:
                        print("Too small")
                        Range1=guess+1
            for i in range(1000000000000000000000000000):
                time.sleep(1)
                Ready2=input("Continue?(Yes/No) ")
                if Ready2=="Yes"or Ready2=="yes":
                    print("continuing")
                    break
                else:
                    if Ready2=="No"or Ready2=="no":
                        time.sleep(0.5)
                        Range1=int(input("Give me a number: "))
                        for i in range(1000000000000000000000000000):
                            if Range1<0 or Range1==0:
                                print("Number to small")
                                time.sleep(0.25)
                                Range1=int(input("Give me a number: "))
                            else:
                                break
                        time.sleep(0.5)

                        # The second number in a range is decided by the user
                        Range2=int(input("Give me a number: "))
                        for i in range(1000000000000000000000000000):
                            if Range2<Range1 or Range2==Range1:
                                print("Number to small")
                                time.sleep(0.25)
                                Range2=int(input("Give me a number: "))
                            else:
                                break
                        time.sleep(0.5)

                        # The user decides a number in the range they decided
                        print("Give me a number betweeen",Range1,"and",Range2,":")
                        Num=int(input(" "))
                        for i in range(1000000000000000000000000000):
                            if Num<Range1 or Num>Range2:
                                print("Number not in range")
                                time.sleep(0.25)
                                print("Give me a number betweeen",Range1,"and",Range2,":")
                                Num=int(input(" "))
                            else:
                                break
                        time.sleep(0.5)
                        for i in range(1000000000000000000000000000):
                            Game_gueses=int(input("Give me a number: "))
                            if Game_gueses==0 or Game_gueses<0:
                                print("Number to small")
                                time.sleep(0.25)
                                Game_gueses=int(input("Give me a number: "))
                            else:
                                break
                        time.sleep(0.5)

                        # The user is asked if they are ready to start the game
                        Ready=input("Ready?(Yes/No) ")

                        # If the user is not ready, then they will deccide the range and number all over again
                        for i in range(1000000000000000000000000000):
                            if Ready=="No"or Ready=="no":
                                time.sleep(0.5)
                                Range1=int(input("Give me a number: "))
                                for i in range(1000000000000000000000000000):
                                    if Range1<0 or Range1==0:
                                        print("Number too small")
                                        time.sleep(0.25)
                                        Range1=int(input("Give me a number: "))
                                    else:
                                        break
                                time.sleep(0.5)
                                Range2=int(input("Give me a number: "))
                                for i in range(1000000000000000000000000000):
                                    if Range2<Range1 or Range2==Range1:
                                        print("Number too small")
                                        time.sleep(0.25)
                                        Range2=int(input("Give me a number: "))
                                    else:
                                        break
                                time.sleep(0.5)
                                print("Give me a number betweeen",Range1,"and",Range2,":")
                                Num=int(input(" "))
                                for i in range(1000000000000000000000000000):
                                    if Num<Range1 or Num>Range2:
                                        print("Number not in range")
                                        time.sleep(0.25)
                                        print("Give me a number betweeen",Range1,"and",Range2,":")
                                        Num=int(input(" "))
                                    else:
                                        break
                                time.sleep(0.5)
                                for i in range(1000000000000000000000000000):
                                    Game_gueses=int(input("Give me a number: "))
                                    if Game_gueses==0 or Game_gueses<0:
                                        print("Number too small")
                                        time.sleep(0.25)
                                        Game_gueses=int(input("Give me a number: "))
                                    else:
                                        break
                                Ready=input("Ready?(Yes/No) ")
                            else:

                                # If the user is ready to start the game, the game will begin
                                if Ready=="Yes"or Ready=="yes":
                                    time.sleep(0.5)
                                    print("A bot will begin to guess your number.")
                                    break
                                else:
                                    print("Answer not recognised")
                                    time.sleep(0.25)
                                    Ready=input("Ready?(Yes/No) ")
                    else:
                        print("Awnswer not recognised")
                        Ready2=input("Continue?(Yes/No) ")
    else:
        break
if win==0:

# Bot endgame, it will have a higher chance to guess the number on the last try, if it lose, it will accept defeat.
    time.sleep(1)
    if Num<(Range1+10):
        Range1=Num
    else:
        Range1=Num-10
    if Num>(Range2-10):
        Range2=Num
    else:
        Range2=Num+10
    guess=random.randint(Range1,Range2)
    print("Guess:",guess)
    time.sleep(1)
    if guess==Num:
        print("I win")
        win=1
    else:
        if guess>Num:
            print("You win")
        else:
            if guess<Num:
                print("You win")
# Play again
for i in range(1000000000000000000000000000):
    win=0
    # The first number in a range is decided by the user
    Range1=int(input("Give me a number: "))
    for i in range(1000000000000000000000000000):
        if Range1<0 or Range1==0:
            print("Number to small")
            time.sleep(0.25)
            Range1=int(input("Give me a number: "))
        else:
            break
    time.sleep(0.5)
    # The second number in a range is decided by the user
    Range2=int(input("Give me a number: "))
    for i in range(1000000000000000000000000000):
        if Range2<Range1 or Range2==Range1:
            print("Number to small")
            time.sleep(0.25)
            Range2=int(input("Give me a number: "))
        else:
            break
    time.sleep(0.5)
    # The user decides a number in the range they decided
    print("Give me a number betweeen",Range1,"and",Range2,":")
    Num=int(input(" "))
    for i in range(1000000000000000000000000000):
        if Num<Range1 or Num>Range2:
            print("Number not in range")
            time.sleep(0.25)
            print("Give me a number betweeen",Range1,"and",Range2,":")
            Num=int(input(" "))
        else:
            break
    time.sleep(0.5)
    for i in range(1000000000000000000000000000):
        Game_gueses=int(input("Give me a number: "))
        if Game_gueses==0 or Game_gueses<0:
            print("Number to small")
            time.sleep(0.25)
            Game_gueses=int(input("Give me a number: "))
        else:
            break
    time.sleep(0.5)
    # The user is asked if they are ready to start the game
    Ready=input("Ready?(Yes/No) ")

    # If the user is not ready, then they will deccide the range and number all over again
    for i in range(1000000000000000000000000000):
        if Ready=="No"or Ready=="no":
            time.sleep(0.5)
            Range1=int(input("Give me a number: "))
            for i in range(1000000000000000000000000000):
                if Range1<0 or Range1==0:
                    print("Number too small")
                    time.sleep(0.25)
                    Range1=int(input("Give me a number: "))
                else:
                    break
            time.sleep(0.5)
            Range2=int(input("Give me a number: "))
            for i in range(1000000000000000000000000000):
                if Range2<Range1 or Range2==Range1:
                    print("Number too small")
                    time.sleep(0.25)
                    Range2=int(input("Give me a number: "))
                else:
                    break
            time.sleep(0.5)
            print("Give me a number betweeen",Range1,"and",Range2,":")
            Num=int(input(" "))
            for i in range(1000000000000000000000000000):
                if Num<Range1 or Num>Range2:
                    print("Number not in range")
                    time.sleep(0.25)
                    print("Give me a number betweeen",Range1,"and",Range2,":")
                    Num=int(input(" "))
                else:
                    break
            time.sleep(0.5)
            for i in range(1000000000000000000000000000):
                Game_gueses=int(input("Give me a number: "))
                if Game_gueses==0 or Game_gueses<0:
                    print("Number too small")
                    time.sleep(0.25)
                    Game_gueses=int(input("Give me a number: "))
                else:
                    break
            Ready=input("Ready?(Yes/No) ")
        else:

            # If the user is ready to start the game, the game will begin
            if Ready=="Yes"or Ready=="yes":
                time.sleep(0.5)
                print("A bot will begin to guess your number.")
                break
            else:
                print("Answer not recognised")
                time.sleep(0.25)
                Ready=input("Ready?(Yes/No) ")
    # Bot imedietly guesses in the middle to thin down the numbers neede by half
    guess=((Range2+Range1)//2)
    print(guess)
    if guess==Num:
        print("I win")
        win=1
    else:
        if guess>Num:
            print("Too big")
            Range2=guess-1
        else:
            if guess<Num:
                print("Too small")
                Range1=guess+1
    # User is asked to continue the game or not
    for i in range(1000000000000000000000000000):
        time.sleep(1)
        Ready2=input("Continue?(Yes/No) ")
        if Ready2=="Yes"or Ready2=="yes":
            print("continuing")
            break
        else:
    # If not, then they will repeat all over
            if Ready2=="No"or Ready2=="no":
                time.sleep(0.5)
                Range1=int(input("Give me a number: "))
                for i in range(1000000000000000000000000000):
                    if Range1<0 or Range1==0:
                        print("Number to small")
                        time.sleep(0.25)
                        Range1=int(input("Give me a number: "))
                    else:
                        break
                time.sleep(0.5)

                # The second number in a range is decided by the user
                Range2=int(input("Give me a number: "))
                for i in range(1000000000000000000000000000):
                    if Range2<Range1 or Range2==Range1:
                        print("Number to small")
                        time.sleep(0.25)
                        Range2=int(input("Give me a number: "))
                    else:
                        break
                time.sleep(0.5)

                # The user decides a number in the range they decided
                print("Give me a number betweeen",Range1,"and",Range2,":")
                Num=int(input(" "))
                for i in range(1000000000000000000000000000):
                    if Num<Range1 or Num>Range2:
                        print("Number not in range")
                        time.sleep(0.25)
                        print("Give me a number betweeen",Range1,"and",Range2,":")
                        Num=int(input(" "))
                    else:
                        break
                time.sleep(0.5)
                for i in range(1000000000000000000000000000):
                    Game_gueses=int(input("Give me a number: "))
                    if Game_gueses==0 or Game_gueses<0:
                        print("Number to small")
                        time.sleep(0.25)
                        Game_gueses=int(input("Give me a number: "))
                    else:
                        break
                time.sleep(0.5)

                # The user is asked if they are ready to start the game
                Ready=input("Ready?(Yes/No) ")

                # If the user is not ready, then they will deccide the range and number all over again
                for i in range(1000000000000000000000000000):
                    if Ready=="No"or Ready=="no":
                        time.sleep(0.5)
                        Range1=int(input("Give me a number: "))
                        for i in range(1000000000000000000000000000):
                            if Range1<0 or Range1==0:
                                print("Number too small")
                                time.sleep(0.25)
                                Range1=int(input("Give me a number: "))
                            else:
                                break
                        time.sleep(0.5)
                        Range2=int(input("Give me a number: "))
                        for i in range(1000000000000000000000000000):
                            if Range2<Range1 or Range2==Range1:
                                print("Number too small")
                                time.sleep(0.25)
                                Range2=int(input("Give me a number: "))
                            else:
                                break
                        time.sleep(0.5)
                        print("Give me a number betweeen",Range1,"and",Range2,":")
                        Num=int(input(" "))
                        for i in range(1000000000000000000000000000):
                            if Num<Range1 or Num>Range2:
                                print("Number not in range")
                                time.sleep(0.25)
                                print("Give me a number betweeen",Range1,"and",Range2,":")
                                Num=int(input(" "))
                            else:
                                break
                        time.sleep(0.5)
                        for i in range(1000000000000000000000000000):
                            Game_gueses=int(input("Give me a number: "))
                            if Game_gueses==0 or Game_gueses<0:
                                print("Number too small")
                                time.sleep(0.25)
                                Game_gueses=int(input("Give me a number: "))
                            else:
                                break
                        Ready=input("Ready?(Yes/No) ")
                    else:

                        # If the user is ready to start the game, the game will begin
                        if Ready=="Yes"or Ready=="yes":
                            time.sleep(0.5)
                            print("A bot will begin to guess your number.")
                            break
                        else:
                            print("Answer not recognised")
                            time.sleep(0.25)
                            Ready=input("Ready?(Yes/No) ")
            else:
                print("Awnswer not recognised")
                Ready2=input("Continue?(Yes/No) ")
    for i in range (Game_gueses-1):
    # Main game loop, bot guesses number, than decides if it was too high or too low, it will do number higher or lower depending on the awnswer
        if win==0:
            if Ready=="Yes"or Ready=="yes":
                time.sleep(1)
                guess=random.randint(Range1,Range2)
                print("Guess:",guess)
                time.sleep(1)
                if guess==Num:
                    print("I win")
                    win=1
                    break
                else:
                    if guess>Num:
                        print("Too big")
                        Range2=guess-1
                    else:
                        if guess<Num:
                            print("Too small")
                            Range1=guess+1
                for i in range(1000000000000000000000000000):
                    time.sleep(1)
                    Ready2=input("Continue?(Yes/No) ")
                    if Ready2=="Yes"or Ready2=="yes":
                        print("continuing")
                        break
                    else:
                        if Ready2=="No"or Ready2=="no":
                            time.sleep(0.5)
                            Range1=int(input("Give me a number: "))
                            for i in range(1000000000000000000000000000):
                                if Range1<0 or Range1==0:
                                    print("Number to small")
                                    time.sleep(0.25)
                                    Range1=int(input("Give me a number: "))
                                else:
                                    break
                            time.sleep(0.5)

                            # The second number in a range is decided by the user
                            Range2=int(input("Give me a number: "))
                            for i in range(1000000000000000000000000000):
                                if Range2<Range1 or Range2==Range1:
                                    print("Number to small")
                                    time.sleep(0.25)
                                    Range2=int(input("Give me a number: "))
                                else:
                                    break
                            time.sleep(0.5)

                            # The user decides a number in the range they decided
                            print("Give me a number betweeen",Range1,"and",Range2,":")
                            Num=int(input(" "))
                            for i in range(1000000000000000000000000000):
                                if Num<Range1 or Num>Range2:
                                    print("Number not in range")
                                    time.sleep(0.25)
                                    print("Give me a number betweeen",Range1,"and",Range2,":")
                                    Num=int(input(" "))
                                else:
                                    break
                            time.sleep(0.5)
                            for i in range(1000000000000000000000000000):
                                Game_gueses=int(input("Give me a number: "))
                                if Game_gueses==0 or Game_gueses<0:
                                    print("Number to small")
                                    time.sleep(0.25)
                                    Game_gueses=int(input("Give me a number: "))
                                else:
                                    break
                            time.sleep(0.5)

                            # The user is asked if they are ready to start the game
                            Ready=input("Ready?(Yes/No) ")

                            # If the user is not ready, then they will deccide the range and number all over again
                            for i in range(1000000000000000000000000000):
                                if Ready=="No"or Ready=="no":
                                    time.sleep(0.5)
                                    Range1=int(input("Give me a number: "))
                                    for i in range(1000000000000000000000000000):
                                        if Range1<0 or Range1==0:
                                            print("Number too small")
                                            time.sleep(0.25)
                                            Range1=int(input("Give me a number: "))
                                        else:
                                            break
                                    time.sleep(0.5)
                                    Range2=int(input("Give me a number: "))
                                    for i in range(1000000000000000000000000000):
                                        if Range2<Range1 or Range2==Range1:
                                            print("Number too small")
                                            time.sleep(0.25)
                                            Range2=int(input("Give me a number: "))
                                        else:
                                            break
                                    time.sleep(0.5)
                                    print("Give me a number betweeen",Range1,"and",Range2,":")
                                    Num=int(input(" "))
                                    for i in range(1000000000000000000000000000):
                                        if Num<Range1 or Num>Range2:
                                            print("Number not in range")
                                            time.sleep(0.25)
                                            print("Give me a number betweeen",Range1,"and",Range2,":")
                                            Num=int(input(" "))
                                        else:
                                            break
                                    time.sleep(0.5)
                                    for i in range(1000000000000000000000000000):
                                        Game_gueses=int(input("Give me a number: "))
                                        if Game_gueses==0 or Game_gueses<0:
                                            print("Number too small")
                                            time.sleep(0.25)
                                            Game_gueses=int(input("Give me a number: "))
                                        else:
                                            break
                                    Ready=input("Ready?(Yes/No) ")
                                else:

                                    # If the user is ready to start the game, the game will begin
                                    if Ready=="Yes"or Ready=="yes":
                                        time.sleep(0.5)
                                        print("A bot will begin to guess your number.")
                                        break
                                    else:
                                        print("Answer not recognised")
                                        time.sleep(0.25)
                                        Ready=input("Ready?(Yes/No) ")
                        else:
                            print("Awnswer not recognised")
                            Ready2=input("Continue?(Yes/No) ")
        else:
            break
    if win==0:
    # Bot endgame, it will have a higher chance to guess the number on the last try, if it lose, it will accept defeat.
        time.sleep(1)
    if Num<(Range1+10):
        Range1=Num
    else:
        Range1=Num-10
    if Num>(Range2-10):
        Range2=Num
    else:
        Range2=Num+10
        guess=random.randint(Range1,Range2)
        print("Guess:",guess)
        time.sleep(1)
        if guess==Num:
            print("I win")
            win=1
        else:
            if guess>Num:
                print("You win")
            else:
                if guess<Num:
                    print("You win")