# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Fanficinfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    arturl = scrapy.Field()
    title  = scrapy.Field()
    author = scrapy.Field()
    disc   = scrapy.Field()
    info   = scrapy.Field()
