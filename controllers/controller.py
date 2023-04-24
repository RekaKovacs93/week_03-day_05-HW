from flask import render_template, request, redirect
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
    book_cover = request.form["image"].replace(".jpeg", "")

    new_book = Book(book_title, book_author, book_genre, book_cover, False)
    add_new_book(new_book)
    return redirect("/")

@app.route("/remove/<int:index>", methods=["POST"])
def remove_books(index):
    i = int(index)
    delete = request.form.get("delete")
    if delete:
        remove_book(books[i])
    return render_template("index.html", books = books)


# @app.route("/remove/<book>", methods=["POST"])
# def remove_books(book):# book = 35book5
#     # i = int(index)
#     book = request.form.get("book")
#     print(book)
#     if book:
#         remove_book(book)
#     return render_template("index.html", books = books)



@app.route("/book/<index>")
def book(index):
    i = int(index)
    return render_template("book.html", books = books, book = books[i])



