# -*- coding: utf-8 -*-
import scrapy


class WpageSpider(scrapy.spiders):
    name = "webpage"
    allow_domains = []
    start_urls = ()

    def __init__(self):
        pass

    def parse(self, response):
        pass
