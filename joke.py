
import pyjokes

for i in range(3):
    joke = pyjokes.get_joke()
    print(joke)
    print()

while True:
    choice = input("Do you want another joke? (yes/no): ").lower()

    if choice == "yes":
        print(pyjokes.get_joke())
    else:
        print("Thank you!")
        break
