# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostOslUgrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    autor = scrapy.Field()
    contenido = scrapy.Field()
    list_cat = scrapy.Field()
    list_tag = scrapy.Field()
    
