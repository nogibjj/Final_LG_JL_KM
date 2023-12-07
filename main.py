from flask import Flask, redirect, url_for, render_template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configure logging
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
log_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=5)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return render_template('button.html')

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