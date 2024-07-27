import random
print("Rolling a 6-six sided die...")
outcome=random.randint(1,6)
print("Got",outcome)
if outcome<=3:
    print("Going to the park")
else:
    if outcome==4:
        print("Sweep the floor")
    else:
        print("Read a book")
print("Done!")