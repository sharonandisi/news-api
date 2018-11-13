from flask import render_template
from app import app
from .request import get_sources,get_source,search_source

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
    search_source = request.args.get(source_query)
    if search_source:
        return redirect(url_for('search',source_name=search_source))
    else:
        return render_template('index.html', title = title , topheadlines_sources = top-headlines, business_sources = business, entertainment_sources = entertainment)

@app.route('/source/<int:id>')
def source(id):
    """
    View source page function that returns source page and its data
    """
    source = get_source(id)
    name = f'{source.name}'
    return render_template('source.html', name = name, source = source)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split("")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    name = f'search results for {source_name}'
    return render_template('search.html', sources = searched_sources)

@app.route('/source/comment/new/<int:id>', methods = ['GET', 'POST'])
def new_comment(id):
    form = CommentForm()
    movie = get_source(id)

    if form.validate_on_submit():
        name = form.name.data
        comment = form.comment.data
        new_comment = Comment(source.id,name,urlToImage,comment)
        new_comment.save_comment()
        return redirect(url_for('source',id = source.id))

        name = f'{source.name} comment'
        return render_template('new_comment.html',name = name, comment_form=form, source=source)