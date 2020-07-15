from flask import Flask
New = Flask(__name__)


class Webscraper:

    def __init__(self, title='headline', news_body='body'):
        self.title = title
        self.news_body = news_body

    def get_title(self):
        return self.title

    def get_body(self):
        return self.news_body
