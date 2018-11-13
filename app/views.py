from flask import render_template
from app import app
from .request import get_sources,get_source

#views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    # getting top headlines in sources 
    topheadlines_sources = get_sources('top-headlines')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    title = 'Home - Welcome to your online News room'
    return render_template('index.html', title = title , topheadlines_sources = top-headlines, business_sources = business, entertainment_sources = entertainment)

@app.route('/source/<int:id>')
def source(id):
    """
    View source page function that returns source page and its data
    """
    source = get_source(id)
    name = f'{source.name}'
    return render_template('source.html', name = name, source = source)