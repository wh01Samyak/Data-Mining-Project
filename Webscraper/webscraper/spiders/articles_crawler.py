import scrapy
import csv
from webscraper import articles_getter

class ArticlesCrawler(scrapy.Spider):
    name = 'articles'
    start_urls = articles_getter.request_posts()

    def parse(self, response):
        article_title = response.css('title::text').extract()[0]

        yield {'headline': article_title}
