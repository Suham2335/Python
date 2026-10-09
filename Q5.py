
menu = {
    "momo": 150,
    "pizza": 350,
    "burger": 250,
    "chowmein": 180,
    "fried rice": 200,
    "sandwich": 150,
    "pasta": 300,
    "coke": 80
}

order = []

def display_menu():
    print("\nRestaurant Menu")
    for item, price in menu.items():
        print(item, "- Rs.", price)

def add_item(item, quantity):
    if item not in menu:
        raise KeyError("Food item does not exist.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    order.append({
        "item": item,
        "price": menu[item],
        "quantity": quantity
    })
    print("Item added successfully.")

def calculate_bill():
    subtotal = 0
    for item in order:
        subtotal += item["price"] * item["quantity"]

    tax = subtotal * 0.13
    total = subtotal + tax
    return subtotal, tax, total

def display_order():
    print("\nFinal Order")
    for item in order:
        amount = item["price"] * item["quantity"]
        print(item["item"], "x", item["quantity"], "= Rs.", amount)

    subtotal, tax, total = calculate_bill()
    print("Subtotal: Rs.", subtotal)
    print("Tax (13%): Rs.", tax)
    print("Final Bill: Rs.", total)

while True:
    display_menu()
    item = input("\nEnter food item (or 'done' to finish): ").lower()

    if item == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)

    except KeyError as e:
        print("Error:", e)

    except ValueError as e:
        print("Invalid input:", e)

if order:
    display_order()
else:
    print("No items ordered.")