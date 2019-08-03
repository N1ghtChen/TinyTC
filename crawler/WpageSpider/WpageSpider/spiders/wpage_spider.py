# -*- coding: utf-8 -*-
import scrapy


class WpageSpider(scrapy.spiders):
    name = "Wpage"
    allow_domains = []
    start_urls = ()

    def start_requests(self):
        pass

    def parse(self, response):
        pass
