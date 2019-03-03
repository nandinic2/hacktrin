from flask import *
from app import app
from app.models import news_api
import json, requests

@app.route('/hacktrin')
def hacktrin():

    return render_template('hacktrin.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/news')
def news():
    news = news_api.call(requests.get("https://newsapi.org/v2/everything?q=female%20empowerment&from=2019-03-03&sortBy=popularity&apiKey=daa824d68c6d40ad906270db91cd405f").json())
    return render_template('news.html', data=news)
