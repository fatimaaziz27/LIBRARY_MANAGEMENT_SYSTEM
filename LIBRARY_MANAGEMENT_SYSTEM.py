# Library details
total_books = 10
books = []
borrowed_books = []

# Function to show available books
def show_books():
    print(f"\nAvailable books: {len(books)}")
    for book in books:
        print(f"Book ID: {book['id']}, Title: {book['title']}")
    print()

# Function to add a book
def add_book():
    if len(books) + len(borrowed_books) >= total_books:
        print("Library book limit reached!\n")
        return

    book_id = input("Enter book ID: ")

    for book in books + borrowed_books:
        if book["id"] == book_id:
            print("Book ID already exists!\n")
            return

    title = input("Enter book title: ")

    books.append({"id": book_id, "title": title})
    print("Book added successfully!\n")

# Function to borrow a book
def borrow_book():
    book_id = input("Enter book ID to borrow: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            borrowed_books.append(book)
            print(f"Book '{book['title']}' borrowed successfully!\n")
            return

    print("Book not found or already borrowed!\n")

# Function to return a book
def return_book():
    book_id = input("Enter book ID to return: ")

    for book in borrowed_books:
        if book["id"] == book_id:
            borrowed_books.remove(book)
            books.append(book)
            print(f"Book '{book['title']}' returned successfully!\n")
            return

    print("Borrowed book not found!\n")

# Function to display borrowed books
def show_borrowed_books():
    if not borrowed_books:
        print("No books are currently borrowed.\n")
    else:
        print("\n--- Borrowed Books ---")
        for book in borrowed_books:
            print(f"Book ID: {book['id']}, Title: {book['title']}")
        print()

# Main loop
while True:
    print("0. Exit")
    print("1. Show Available Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Borrowed Books")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting Library Management System...")
        break
    elif choice == "1":
        show_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        show_borrowed_books()
    else:
        print("Invalid choice, try again.\n")
