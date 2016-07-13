#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
file: main.py $Id$
date: $Date$
"""
from post_osl_ugr.items import PostOslUgrItem
from scrapy import Request
from scrapy.spiders import Spider

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
                    item['list_tag'].append(c[4:])
                elif c.startswith('category-'):
                    item['list_cat'].append(c[9:])
            yield Request(article.xpath('.//@href').extract()[0], 
                callback=self.parse_post, meta={'item': item})


    def parse_post(self, response):
        item = response.meta['item']
        co = response.xpath('//section[@class="entry-content "]').extract()
        item['contenido'] = ''
        for i, j in enumerate(co):
            item['contenido'] += j.encode('utf-8', errors='replace').decode('utf-8')
        yield item
