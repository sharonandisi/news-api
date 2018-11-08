from flask import render_template
from app import app

#views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    message = 'News API'
    return render_template('index.html')

@app.route('/newssource/<int :source_id>')
def newssource(newssource_id):
    """
    View newssource page function that returns news source page and its data
    """
    return render_template('newssource.html', id = newssource_id)