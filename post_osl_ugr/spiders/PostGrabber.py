#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
file: main.py $Id$
date: $Date$
"""
from post_osl_ugr.items import PostOslUgrItem
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
            self.logger.info('Categoria: %s', article.xpath('./@class/text()').re(r'(category-* )'))
            item['titulo'] = article.xpath('.//a[@title]/text()').extract()
#            item['autor'] = article.xpath('.//a[@title]/text()').extract()
#            item['contenido'] = article.xpath('.//section[@class]/text()').extract()
#            item['list_cat'] = article.xpath('cat')
#            item['list_tag'] = article.xpath('tag')
#            print item
            yield item
