import scrapy
import requests
from anixScrapy.utils.anime import parse_anime


class AnimesSpider(scrapy.Spider):
    name = 'animes'
    allowed_domains = ['4anime.to']
    start_urls = ['https://4anime.to/hall-of-fame/']

    def parse(self, response):
        links = response.css('#headerDIV_3 a::attr("href")').getall()

        for link in links:
            yield scrapy.Request(url=link, callback=self.anime)

    def anime(self, response):
        return parse_anime(response)

