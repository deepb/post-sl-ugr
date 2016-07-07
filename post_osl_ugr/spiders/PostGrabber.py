#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
file: main.py $Id$
date: $Date$
"""
from post_osl_ugr.items import PostOslUgrItem
from scrapy import Request
from scrapy.spiders import Spider
import re

class PostgrabberSpider(Spider):
    name = "PostGrabber"
    allowed_domains = ['osl.ugr.es']
    start_urls = [
        'http://osl.ugr.es/'
    ]
    
    def parse(self, response):
        hxs = response.xpath('//article[@id]')
        for article in hxs:
            item = PostOslUgrItem()
            item['titulo'] = article.xpath('.//a[@title]/text()').extract()
            clas = article.xpath('./@class').extract()
            item['list_cat'] = []
            item['list_tag'] = []
            for i, j in enumerate(clas):
                 cl = j.split(' ')
            for c in cl:
                #print "clase :" , c
                if c.startswith('tag-'):
                    item['list_tag'].append(c)
                elif c.startswith('category-'):
                    item['list_cat'].append(c)
            yield Request(article.xpath('.//@href').extract()[0], 
                callback=self.parse_post, meta={'item': item})
            #print item
            #yield item

    def parse_post(self, response):
        item = response.meta['item']
        item['contenido'] = response.xpath('//section[@class="entry-content "]').extract()
        yield item
