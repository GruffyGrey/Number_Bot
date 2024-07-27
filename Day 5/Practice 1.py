# Problem 1
value_1=10
value_1a=100
print(value_1,value_1a)
if value_1>100 and value_1a>100:
    print("Both numbers are greater than 100")
else:
    print("I wanted both to be greater than 100")

# Problem 2
username=input("Username: ")
pasword=input("Password: ")
if username=="student"and pasword=="python":
    print("Welcome back")
else:
    print("Access denied")

# Problem 3
fav_pet=input("What is your favorite pet: ")
if fav_pet=="cat"or fav_pet=="dog":
    print("The best pet")
else:
    print("Nice animal")

# Problem 4
value4=100
value4a=10000
print(value4,value4a)
if value4>100 or value4a>100:
    print("At lest one number is greater than 100")
else:
    print("I wanted at leaste one number to be greater than 100")

# Problem 5
value_5=int(input("Give me a positive 2-digit integer: "))
if value_5>99 or value_5<10:
    print("That is not what i wanted")
else:
    print("Thanks")





# Challenge
value_chal=100
value_chal_a=1000
if (value_chal>100 and value_chal_a<100)and not(value_chal_a>100 and value_chal<100):
    print("Exactly one number is greater than 100")
else:
    if (value_chal_a>100 and value_chal<100)and not(value_chal>100 and value_chal_a<100):
        print("Exactly one number is greater than 100")
    else:
        print("I wanted exactly one number to be greater than 100")