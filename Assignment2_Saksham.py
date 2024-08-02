def add_book (title, author,genre) :
        return (title , author , genre)

library  = []
library_set = set()

def add_to_library(book):

                library.append(book)
                library_set.add(book)
                print(f"Book '{book[0]}'d added to the library")
        


def remove_from_library(title):
        for book in library:
                if book[0] == title:
                        library.remove(book)
                        library_set.remove(book)
                        print(f"Book '{title}'removed from the library")
                        return 
        print(f"Book '{title}' not found in the library.")

def search_book(search_term):
        results = []
        for book in library:
                if search_term in book[0] or  search_term in book[1]:
                        results.append(book) 
        return results

def list_books():
        for book in library:
                print(f"Title:{book[0]},Author:{book[1]},Genre: {book[2]}")

def categorize_books():
        genre_dict = {}
        for book in library:
                genre = book[2]
                if genre not in genre_dict:
                        genre_dict[genre] = [book]
                else:
                        genre_dict[genre].append(book)
        return genre_dict

def check_duplicates():
        if len(library) is len(library_set):
                print("Duplicate book found")
        else:
                print("No duplicate book found")

while True:
        print("\nLibrary Management System:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for books")
        print("4. List all books")
        print("5. Categorize books by genre")
        print("6. Check Duplicate")
        print("7. Exit")

        ch =  int(input("Enter choice(1-6):"))
        if ch == 1:
                title = input("Enter the title:")
                author = input("Enter the author:")
                genre = input("Enter the genre:")
                book = add_book(title,author,genre)
                add_to_library(book)

        elif ch == 2:
                title = input("Enter the title of the book to remove:")
                remove_from_library(title)

        elif ch == 3:
                search_term = input("Enter search term:")
                results = search_book(search_term)
                if results :
                        for book in results:
                                print(f"Title:{book[0]}, Author:{book[1]}, Genre:{book[2]}")
                else:
                        print("BOOK not found")

        elif ch == 4:
                  list_books()
        
        elif ch == 5:
                genre_dict = categorize_books()
                for genre, books in genre_dict.items():
                        print(f"Genre: {genre}")
                        for book in books:
                                print(f"  Title: {book[0]}, Author: {book[1]}")
        
        elif ch == 6:
                check_duplicates()

        elif ch == 7:
                print("THE END ")
                break
        
        else:
                print("Invalid choice")