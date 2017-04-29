from retrieve_source import Scrape
from bs4 import BeautifulSoup
import re


"""
Scraping file to be called every few min, pass in which html to be directed to.
"""

class Reddit_Scrape(object):
    def __init__(self, html):
        self.html = html
        self.browser = Scrape()
        self.reddit_source = self.browser.get_source(self.html, ret=True)
        self.reddit_soup = BeautifulSoup(self.reddit_source, 'html.parser')
        self.posts = self.reddit_soup.select('div.thing')
        self.subs = None
        self.post_dict = {}

    def get_comments_html(self, post):
        """
        Gets the html links to the comments section and subreddit.
        """
        if len(post.select('a.bylink')) != 0:
            section = str(post.select('a.bylink')[0])
            comments = re.findall(r"href=\"([^\"]+)\"", section)[0]
            if len(re.findall(r"\/r\/(\w+)", comments)) != 0:
                sub = re.findall(r"\/r\/(\w+)", comments)[0]
            else:
                sub = 'null'
        else:
            comments = 'null'
            sub = 'null'
        return comments, sub

    def get_titles_html(self, post):
        """
        Gets the titles of the posts.
        """
        return post.select('p.title')[0].text

    def main_loop(self):
        """
        Main dictionary compiling loop
        """
        for post in range(len(self.posts)):
            comments, sub = self.get_comments_html(self.posts[post])
            title = self.get_titles_html(self.posts[post])
            self.post_dict[post] = {'title': title, 'comments': comments, 'sub': sub}
        self.browser.shutdown()
        return self.post_dict
