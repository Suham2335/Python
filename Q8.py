email = input("Enter your email: ")

if "@" in email and "." in email and " " not in email and email[0] != "@":
    print("Valid email")
else:
    print("Invalid email")