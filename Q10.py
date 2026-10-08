inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter item name: ").lower()

if item in inventory:
    sold = int(input("How many items were sold? "))

    if sold <= inventory[item]:
        inventory[item] -= sold

        if inventory[item] == 0:
            del inventory[item]

        print("Sale completed")
    else:
        print("Not enough stock")
else:
    print("Item does not exist")

print("Updated inventory:")
print(inventory)    