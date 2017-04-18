"""
Module for scaping reddit top (front page).
"""
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime
import random

from retrieve_source import Scrape
from reddit_scraping import Reddit_Scrape

client = MongoClient('mongodb://localhost:27017/')
db = client.reddit_top_db
reddit_new_db = db.reddit_top

working = True
check_delay = 7200
html = 'http://www.reddit.com'

while working == True:
    reddit_posts = Reddit_Scrape(html)
    scrape_time = datetime.datetime.now()
    reddit_dict = reddit_posts.main_loop()
    for post,content in reddit_dict.items():
        reddit_new_db.insert_one({
            'post': post,
            'info': content,
            'time': scrape_time
        })
    time.sleep(check_delay + int(random.random()*100))
