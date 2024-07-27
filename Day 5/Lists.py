groceries=["milk","oranges","ice cream","potatoes"]
print(groceries)

ints=[1,-6,33,1000]
print(ints)

mixed_lists=[33,"cat",True]
print(mixed_lists)

num_items=len(groceries)
print("grocery list has",num_items,"item")

first_item=groceries[0]
print("First item is:",first_item)


last_item=groceries[len(groceries)-1]
print("last item is",last_item)

for food in groceries:
    print(food)