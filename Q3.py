
books = [
    {"title": "Python Basics", "author": "John", "available": True},
    {"title": "HTML and CSS", "author": "David", "available": True},
    {"title": "Learn Java", "author": "Smith", "available": True},
    {"title": "Computer Networks", "author": "Alex", "available": True},
    {"title": "Data Structures", "author": "Robert", "available": True}
]

def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise ValueError("Book does not exist.")

def borrow_book(title):
    book = search_book(title)
    if book["available"]:
        book["available"] = False
        print("Book borrowed successfully.")
    else:
        print("Sorry, this book is already borrowed.")

def return_book(title):
    book = search_book(title)
    if not book["available"]:
        book["available"] = True
        print("Book returned successfully.")
    else:
        print("This book was not borrowed.")

def display_books():
    print("\nAvailable Books:")
    for book in books:
        if book["available"]:
            print(book["title"], "-", book["author"])

while True:
    print("\n1. Search Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            book = search_book(title)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"])

        elif choice == 2:
            title = input("Enter book title to borrow: ")
            borrow_book(title)

        elif choice == 3:
            title = input("Enter book title to return: ")
            return_book(title)

        elif choice == 4:
            display_books()

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)