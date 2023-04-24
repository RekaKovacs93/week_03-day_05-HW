from models.book import Book

book1 = Book("Diary", "Chuck Palahniuk", "fiction", "0", True)
book2 = Book("Solaris", "Stanislaw Lem", "science-fiction", "1", False)
book3 = Book("Jubiabá", "Jorje Amado", "fiction", "2", True)
book4 = Book("Ursula K Le Guin", "The Dispossessed", "science-fiction", "3", False)


books = [book1, book2, book3, book4]

def add_new_book(book):
    books.append(book)

def remove_book(book):
    books.remove(book)


#     List all Books
# * Show an individual Book
# * Add a new Book to the Library.
# * Remove a Book from the Library