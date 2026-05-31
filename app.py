from flask import Flask, render_template, request, redirect
from library import Library

app = Flask(__name__)

library = Library()

@app.route("/")
def home():
    report = library.report()
    return render_template(
        "index.html",
        books=library.books,
        report=report
    )

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    author = request.form["author"]

    library.add_book(title, author)

    return redirect("/")

@app.route("/search")
def search():
    keyword = request.args.get("keyword", "")
    results = library.search_books(keyword)

    report = library.report()

    return render_template(
        "index.html",
        books=results,
        report=report
    )

@app.route("/issue/<title>")
def issue(title):
    library.issue_book(title)
    return redirect("/")

@app.route("/return/<title>")
def return_book(title):
    library.return_book(title)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)