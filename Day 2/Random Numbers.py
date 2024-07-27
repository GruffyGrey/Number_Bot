import random

for i in range(10):
    num=random.randint(0,100)
    print(num)

print("Rolling a 6-six sided die...")
outcome=random.randint(1,6)
print("Got:",outcome)