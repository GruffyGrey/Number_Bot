# Problem 1
import random
def lucky_number():
    print("Today your lucky number is",(random.randint(1,100)))
lucky_number()

# Problem 2
def story(distance):
    print("In a galaxy",distance,"light years away...")
story(6)
story(5)

# Problem 3
def make_it_big(N):
    print(N*1000000)
make_it_big(1)

# Problem 5
def function5(N):
    if N>100:
        print("Too much work")
    else:
        print(N*N)
function5(150)
function5(50)

# Problem 6
def function6(Height,Base):
    print((Height*Base)/2)
function6(10,5)

# Problem 7
def function7(number_of_cats):
    for i in range(number_of_cats):
        print("=^.^=")
function7(100)

# Problem 8
def function8(a,b):
    if a>b:
        print(a,"is greater than",b)
    else:
        if b>a:
            print(b,"is greater than",a)
        else:
            print("Both number are equal to",a)
function8(10,5)

# Challenge
def functionC(A,B):
    print(A*A-(2*(B*B)))
functionC(10,5)