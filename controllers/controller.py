from flask import render_template, request
from app import app
from models.books_list import *

@app.route("/")
def index():
    return render_template("index.html", books = books)

@app.route("/", methods=["POST"])
def add_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    book_cover = request.form["image"]

    new_book = Book(book_title, book_author, book_genre, book_cover, False)
    add_new_book(new_book)
    return render_template("index.html", books = books)

@app.route("/remove/<int:index>", methods=["POST"])
def remove_books(index):
    i = int(index)
    delete = request.form.get("delete")
    print(delete)
    if delete:
        remove_book(books[i])
    return render_template("index.html", books = books, book = books[i])

# def remove_book(book_id):
#     for book in books:
#         if book.id == book_id:
#             remove_book(book)
#             break
#     return redirect("/")


@app.route("/book/<index>")
def book(index):
    i = int(index)
    return render_template("book.html", books = books, book = books[i])



# @app.route("/delete/<index>", methods=["POST"])
# def remove_books(index):
#     # book = request.form["book"]
#     # remove_book(book)

#     book_title = request.form["title"]
#     book_author = request.form["author"]
#     book_genre = request.form["genre"]
#     new_book = Book(book_author, book_title, book_genre)
#     remove_book(book1)
#     return render_template("index.html", books = books)

#     # return render_template("index.html", books = books, book = book)
