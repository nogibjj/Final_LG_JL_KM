from flask import Flask, render_template, request


from recommend import recommend

app = Flask(__name__)


genres = [
    "Art",
    "Biography",
    "Business",
    "Chick-Lit",
    "Christian",
    "Classics",
    "Comics",
    "Contemporary",
    "Cookbooks",
    "Crime",
    "Ebooks",
    "Fantasy",
    "Fiction",
    "Graphic-Novels",
    "Historical-Fiction",
    "History",
    "Horror",
    "Manga",
    "Memoir",
    "Music",
    "Mystery",
    "Nonfiction",
    "Paranormal",
    "Philosophy",
    "Poetry",
    "Psychology",
    "Religion",
    "Romance",
    "Science",
    "Science-Fiction",
    "Self-Help",
    "Suspense",
    "Spirituality",
    "Sports",
    "Thriller",
    "Travel",
    "Young-Adult",
]


@app.route("/")
def home():
    return render_template("home.html", genres=genres)


@app.route("/recommendations", methods=["GET", "POST"])
def show_recommendations():
    selected_genre = request.form.get("genre")
    selected_quantity = request.form.get("quantity")
    error_message = None

    # Usere must select a genre and quantity
    if selected_genre is None or selected_quantity is None:
        error_message = "Invalid form data"
    else:
        try:
            selected_quantity = int(selected_quantity)
            if selected_quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
        except ValueError as e:
            error_message = str(e)

    # If there is an error, return to home page
    if error_message:
        return render_template("home.html", genres=genres, error_message=error_message)

    # type recommended_books is a pandas dataframe
    recommended_books = recommend(selected_quantity, selected_genre)

    # If there are no recommendations, return to home page
    if recommended_books is None:
        error_message = "No recommendations available. Please try again."
        return render_template("home.html", genres=genres, error_message=error_message)

    return render_template("recommendations.html", books=recommended_books)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
