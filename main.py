from flask import Flask, redirect, url_for, render_template, request
import logging
from logging.handlers import RotatingFileHandler
from recommend import recommend

app = Flask(__name__)

# Configure logging
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
log_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=5)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

genres = ["Art", "Biography", "Business", "Chick Lit", "Children's", "Christian", "Classics",
          "Comics", "Contemporary", "Cookbooks", "Crime", "Ebooks", "Fantasy", "Fiction",
          "Gay and Lesbian", "Graphic Novels", "Historical Fiction", "History", "Horror",
          "Humor and Comedy", "Manga", "Memoir", "Music", "Mystery", "Nonfiction", "Paranormal",
          "Philosophy", "Poetry", "Psychology", "Religion", "Romance", "Science", "Science Fiction",
          "Self Help", "Suspense", "Spirituality", "Sports", "Thriller", "Travel", "Young Adult"]






@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return render_template('home.html', genres=genres)

@app.route('/recommendations', methods=['POST'])
def show_recommendations():
    selected_genre = request.form.get('genre')  # Assuming you have a form field named 'genre'
    recommended_books = recommend(selected_genre)
    return render_template('recommendations.html', books=recommended_books)



@app.route('/article', methods=['GET'])
def show_article():
    app.logger.info('Article page accessed')
    return render_template('article.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


"""
<form action="{{ url_for('show_article') }}" method="post">
    <button type="submit">Go to Article</button>
</form>
"""