# Problem 1
interger=int(input("Give me an integer: "))
print("Previous:",(interger-1),"Next:",(interger+1))

# Problem 2
int_1=int(input("Give me an integer: "))
int_2=int(input("Give me another intger: "))
print("The sum is:",(int_1+int_2))

# Problem 3
user_age=int(input("How old are you? "))
age=13
if user_age<age:
    print("I'm older")
else:
    if user_age==age:
        print("We are the same age")
    else:
        if user_age>age:
            print("You are older")

# Problem 4
value_4=int(input("Give me an integer: "))
if value_4%10==0:
    print("Ends with 0")
else:
    print("Does not end with 0")

# Problem 5
value_5=int(input("Give me an integer: "))
if value_5%2==0:
    print("Next even:",(value_5+2))
else:
    print("Next even:",(value_5+1))
