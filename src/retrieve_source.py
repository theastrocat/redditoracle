from bs4 import BeautifulSoup
from selenium import webdriver
import time

'''
Basic class for starting a selenium driver driver and scraping an html source.
'''

class Scrape(object):
    def __init__(self):
        self.got_source = False
        self.soup = None
        self.source = None
        self.browser = webdriver.PhantomJS()

    def get_source(self, html, ret = False, delay = 10):
        '''
        Retrieves source code from html.
        '''
        self.got_source = True
        self.browser.get(html)
        time.sleep(delay)
        self.source = self.browser.page_source
        if ret == True:
            return self.source

    def make_soup(self):
        '''
        Parses source with beautifulsoup.
        '''
        if self.got_source == True:
            self.soup = BeautifulSoup(self.source, 'html.parser')
            return self.soup
        else:
            return None

    def shutdown(self):
        '''
        Shutdown Firefox
        '''
        self.browser.quit()
