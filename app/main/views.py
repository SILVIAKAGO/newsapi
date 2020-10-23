from flask import render_template, request, redirect
from . import main
from ..requests import get_articles, get_sources


@main.route('/')
def index():
    """
    View root page function that returns index page and the various news sources
    
    """
    title = 'Home- Welcome News Highlights Website'
    # Getting the news sources
    # news_sources = get_sources('sources')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    # general = get_sources('general')
    health  = get_sources('health')
    science = get_sources('science')
    sports = get_sources('sports')
    technology = get_sources('technology')
    return render_template('index.html',title = title, business = business,entertainment = entertainment,health = health,science = science, sports = sports,technology = technology)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View source page function that returns a source page and its data
    '''
    title = f"{source_id} page"
    #title = "Hello"
    articles = get_articles(source_id)
    return render_template('articles.html',title = title, articles = articles)
