from library import Library

def display_menu():
    """Display the menu options for the Library System."""
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View Available Books")
    print("5. Exit")

def main():
    # Initialize the library object
    library = Library()

    while True:
        # Display the menu
        display_menu()

        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Add a book
            isbn = input("Enter ISBN: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = input("Enter Publication Year: ")

            try:
                library.add_book(isbn, title, author, int(year))
                print(f"Book '{title}' added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            # Borrow a book
            isbn = input("Enter ISBN of the book to borrow: ")

            try:
                library.borrow_book(isbn)
                print(f"Book with ISBN {isbn} has been borrowed.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Return a book
            isbn = input("Enter ISBN of the book to return: ")

            try:
                library.return_book(isbn)
                print(f"Book with ISBN {isbn} has been returned.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            # View available books
            available_books = library.view_available_books()
            if available_books:
                print("\nAvailable Books:")
                for book in available_books:
                    print(f"{book['title']} by {book['author']} ({book['year']})")
            else:
                print("No books are currently available.")

        elif choice == '5':
            # Exit the program
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == '__main__':
    main()
