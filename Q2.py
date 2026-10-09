
products = {
    "apple": {"price": 100, "quantity": 10},
    "banana": {"price": 50, "quantity": 8},
    "milk": {"price": 80, "quantity": 5},
    "bread": {"price": 60, "quantity": 6},
    "rice": {"price": 120, "quantity": 10},
    "juice": {"price": 150, "quantity": 4}
}

cart = {}

def add_product(name, quantity):
    if name not in products:
        raise KeyError("Product does not exist.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if quantity > products[name]["quantity"]:
        raise ValueError("Not enough quantity available.")

    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {
            "price": products[name]["price"],
            "quantity": quantity
        }

    products[name]["quantity"] -= quantity
    print("Product added successfully.")

def calculate_total():
    total = 0
    for name in cart:
        total += cart[name]["price"] * cart[name]["quantity"]
    return total

def display_cart():
    print("\nShopping Cart")
    for name in cart:
        print(name, "Quantity:", cart[name]["quantity"],
              "Price:", cart[name]["price"] * cart[name]["quantity"])
    print("Total Bill:", calculate_total())

while True:
    print("\nAvailable Products:")
    for name in products:
        print(name, "- Price:", products[name]["price"],
              "Available:", products[name]["quantity"])

    name = input("\nEnter product name (or 'done' to finish): ").lower()

    if name == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        add_product(name, quantity)

    except KeyError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)

display_cart()
print("Thank you for shopping!")