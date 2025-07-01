library = []

def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the name of the author of the book: ").strip()
    year_of_publication = int(input("Enter the year of publication of the book: "))
    isbn = input("Enter the Book ISBN: ").strip()
    library.append({"title": title, "author": author, "year_of_publication": year_of_publication, "isbn": isbn, "available": True})
    return f"Book {title} by {author} added successfully"


def view_books():
    for book in library:
        print(all(f"{book["title"]} by {book["author"]}, published on {book["year_of_publication"]}, ISBN: {book["isbn"]}, Available: {book["available"]}"))
    return list(library)

def update_book():
        isbn = input("Enter the book ISBN: ")
        for book in library:
         if book["isbn"] == isbn:
            print("Book Found, Enter new value or press Enter to keep existing:")
            new_title = input(f"New title (current: {book['title']}): ") or book['title']
            new_author = input(f"New author (current: {book['author']}): ") or book['author']
            new_year_input = input(f"New year (current: {book['year_of_publication']}): ") 
            new_isbn_input = input(f"New Isbn (current: {book["isbn"]}):")
            new_year = int(new_year_input) if new_year_input else book['year']
            new_isbn = int(new_isbn_input) if new_isbn_input else book["isbn"]
            new_available_input = input(f"Is it available? (yes/no, current: {book['available']}): ")
            new_available = book['available']
            if new_available_input.lower() == "yes":
                new_available = True
            elif new_available_input.lower() == "no":
                new_available = False

            book['title'] = new_title
            book['author'] = new_author
            book['year'] = new_year
            book['isbn'] = new_isbn
            book['available'] = new_available
            print("book updated successfully")
            return
        print("Book with isbn not found")
        return add_book()

def delete_book():
    isbn_pasted = input("Enter the book ISBN: ")
    for book in library:
        if book["isbn"] == isbn_pasted:
            library.remove(book)
            return f"Book with the ISBN: {isbn_pasted} successfully deleted"
    return f"Book entered is not in library"

def search_book():
    find_title = input("Enter the title of the book: ").strip().lower()
    for book in library:
        if book["title"] == find_title:
            return f"Book {find_title} available in library"
    return f"Book {find_title} not found"


def borrow_book():
    isbn_pasted = input("Enter the book ISBN: ")
    for book in library:
        if book["isbn"] == isbn_pasted:
            if book["available"]:
                book["available"] = False
                print(f"You have successfully borrowed '{book['title']}'.")
            else:
                print(f"The book '{book['title']}' is already borrowed.")
            return
        

def return_book():
    isbn_pasted = input("Enter the book ISBN: ")
    for book in library:
        if book["isbn"] == isbn_pasted:
            if not book["available"]:
                book["available"] = True
                print(f"You have returned book '{book["title"]}' successfully.")
            else:
                print(f"book '{book["title"]}' was not borrowed")
            return
    return f"Book with ISBN was not found"


   





            


menu = """
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit
"""

print("Welcome to our Library")

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()
    if choice == "8":
        print("Thanks for checking. Goodbye👋!")
        break

    if choice not in "12345678":
        print("invalid choice. input from 1-8.")
        continue

    
    if choice == "1":
        print(add_book())
    elif choice == "2":
        print(view_books())
    elif choice == "3":
        print(update_book())
    elif choice == "4":
        print(delete_book())
    elif choice == "5":
        print(search_book())
    elif choice == "6":
        print(borrow_book())
    elif choice == "7":
        print(return_book())

    
   