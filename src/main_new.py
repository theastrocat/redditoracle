"""
Main module loop for pulling the 100 most recent new posts and adding them to mongo database.
Hitting a memory error on
"""
import time
from pymongo import MongoClient
import datetime
import random

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
        print "Scraping {}".format(html)
        reddit_posts = Reddit_Scrape(html)
        scrape_time = datetime.datetime.now()
        reddit_dict = reddit_posts.main_loop()
        print "Inserting to DB..."
        for post,content in reddit_dict.items():
            reddit_new_db.insert_one({
                'post': post,
                'info': content,
                'time': scrape_time
            })
        wait1 = page_delay + int(random.random()*10)
        print "Inserted. Waiting {} seconds.".format(wait1)
        time.sleep(wait1)
    wait2 = check_delay + int(random.random()*100)
    print "Finished set, waiting {} seconds to start again.".format(wait2)
    time.sleep(wait2)
