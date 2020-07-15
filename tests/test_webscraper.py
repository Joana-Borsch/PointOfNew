from models.webscraper import Webscraper


def test_return_title():
    title = 'headline'
    webscraper = Webscraper(title)

    response = webscraper.get_title()

    assert title == response


def test_return_news_body():

    news_body = 'body'
    webscraper = Webscraper(news_body)

    response = webscraper.get_body()

    assert news_body == response




