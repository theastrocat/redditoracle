"""
Main module loop for pulling the 100 most recent new posts and adding them to mongo database.
Still needs a method for excluding posts that are already in the database.
"""

import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime
import random

from retrieve_source import Scrape
from reddit_scraping import Reddit_Scrape

client = MongoClient('mongodb://localhost:27017/')
db = client.reddit_new_db
reddit_new_db = db.reddit_new

working = True
check_delay = 900
page_delay = 60

page_list = ['http://www.reddit.com/new/',
             'http://www.reddit.com/new/?count=25',
             'http://www.reddit.com/new/?count=50',
             'http://www.reddit.com/new/?count=75',
             'http://www.reddit.com/new/?count=100'
]

while working == True:
    for html in page_list:
        reddit_posts = Reddit_Scrape(html)
        scrape_time = datetime.datetime.now()
        reddit_dict = reddit_posts.main_loop()
        for post,content in reddit_dict.items():
            reddit_new_db.insert_one({
                'post': post,
                'info': content,
                'time': scrape_time
            })
        time.sleep(page_delay + int(random.random()*10))
    time.sleep(check_delay + int(random.random()*100))
