# Problem 1
import random
print("Rolling a 6-six sided die...")
num=random.randint(1,6)
print("Got:",num)
if num >=3:
    print("Play soccer")
else:
    print("Rolling again...")
    num=random.randint(1,6)
    print("Got:",num)
    if num <=2:
        print("Clean your room")
    else:
        print("Program in Python")

# Problem 2
N=7
if ((N%2)==0):
    print("even")
else:
    print("odd")

# Problem 3
x=7
y=8
z=9
if (x<y)and(x<z):
    print("x is the smallest")
else:
    print("x is NOT the smallest")