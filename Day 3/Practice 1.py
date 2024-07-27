# Problem 1
user_word=input("Give me a word: ")
if user_word=="Sun" or user_word=="sun":
    print("Shine")

# Problem 2
user_name=input("What is your name: ")
if user_name=="zachary" or user_name=="Zachary":
    print("We have the same name")
else:
    print("Nice to meet you!")

# Problem 3
value_3=5
print(value_3)
if value_3==12:
    print("Dozen")
else:
    if value_3==13:
        print("Baker's dozen")
    else:
        print("Just a number")

# Challenge
L=12
value_challenge=L%12
rugs=((L-value_challenge)/12)
if value_challenge>0:
    rugs=rugs+1
print("L =",L)
print("You need",rugs,"rugs to cover a 12 foot hallway")