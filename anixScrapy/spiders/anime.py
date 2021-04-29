import scrapy
import requests
from anixScrapy.utils.anime import parse_anime


class AnimeSpider(scrapy.Spider):
    name = 'anime'
    allowed_domains = ['4anime.to']
    start_urls = ['https://4anime.to/anime/sakamichi-no-apollon/']

    def parse(self, response):
        return parse_anime(response)
