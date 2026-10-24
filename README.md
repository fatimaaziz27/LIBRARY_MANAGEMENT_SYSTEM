

# Library Management System

A simple, menu-driven Library Management System built with Python to manage books, track borrowed books, and handle book returns.

## About

This project is a console-based application that allows users to manage a small library with a maximum capacity of **10 books**.

Users can add new books, view available books, borrow books, return borrowed books, and display the list of borrowed books.

## Features

- Display available books
- Add new books
- Assign a unique ID to each book
- Prevent duplicate book IDs
- Borrow books
- Return borrowed books
- Display borrowed books
- Track available and borrowed books
- Limit the library to 10 books
- Menu-driven interface
- Handle invalid menu choices

## Technologies Used

- Python

## Python Concepts Practiced

- Variables and data types
- Lists
- Dictionaries
- Functions
- `while` loops
- `for` loops
- Conditional statements
- User input using `input()`
- List methods such as `append()` and `remove()`
- F-strings
- List concatenation
- Boolean conditions

## How It Works

### 1. Show Available Books

Displays the books currently available in the library, including their IDs and titles.

### 2. Add a Book

Allows the user to enter a book ID and title. The system checks whether the library has reached its limit and prevents duplicate book IDs.

### 3. Borrow a Book

Allows the user to borrow an available book. The book is moved from the available books list to the borrowed books list.

### 4. Return a Book

Allows the user to return a borrowed book. The book is moved back to the available books list.

### 5. Show Borrowed Books

Displays all books that are currently borrowed. If no books are borrowed, the system displays a message.

### 6. Exit

Closes the application.

## Menu Options

| Option | Function |
|---|---|
| 0 | Exit |
| 1 | Show Available Books |
| 2 | Add Book |
| 3 | Borrow Book |
| 4 | Return Book |
| 5 | Show Borrowed Books |

## How to Run

1. Clone or download this repository.
2. Open the project folder in your code editor.
3. Make sure Python is installed.
4. Run the following command in the terminal:

```bash
python Library_Management_System.py
```

## Data Storage

The application uses Python lists and dictionaries to store book information.

- `books` stores available books.
- `borrowed_books` stores borrowed books.
- `total_books` sets the maximum library capacity to 10 books.

The data is stored in memory and is lost when the program closes.

## Purpose

This project was created to practice Python programming fundamentals by building a simple, practical library management application.

## Future Improvements

- Save book records permanently using file handling
- Connect the system to a database
- Add book search functionality
- Store borrower information
- Track borrowing dates and return deadlines
- Add overdue book tracking
- Improve input validation
- Create a graphical user interface

## Author

**Fatima Aziz**

GitHub: [fatimaaziz27](https://github.com/fatimaaziz27)

