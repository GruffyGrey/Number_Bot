# Problem 1
animals=["bird","duck","cow","pig","cat"]
print(animals)
size=(len(animals))
print(size,"animals")
first_item=animals[0]
print("First animal:",first_item)
for animal in animals:
    print(animal)
last_item=animals[len(animals)-1]
print("Last animal:",last_item)

# Porblem 2
list_2=[1,2,3,4,5,6,7,8,9,10]
if (len(list_2))>6:
    print(list_2)
    print("This list is long")
else:
    print(list_2)
    print("This list is short")

# Problem 3
list_3=[1,2,3,4]
print(list_3)
third=list_3[2]
print("Third number:",third)
one=list_3[0]
last=list_3[len(list_3)-1]
oneandlast=(one+last)
print("First + last:",oneandlast)

# Problem 4
list_4=[10,1,5,605,3485394563683958685998789784576987]
print(list_4)
for numer10 in list_4:
    if numer10>10:
        print(numer10)

# Problem 5
chores=["sweep the floor","Do the homework","walk the dog"]
print(chores)
user_value=int(input("Give me integer: "))
if user_value>len(chores):
    print("The list is not long enough")
else:
    listc=chores[user_value]
    print(listc)


# Problem 6
colors=["blue","red"]