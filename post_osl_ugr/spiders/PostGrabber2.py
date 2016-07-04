#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
file: main.py $Id$
date: $Date$
"""
#
#import scrapy
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor
#
#class PostgrabberSpider(CrawlSpider):
#    name = "PostGrabber"
#    allowed_domains = ['osl.ugr.es']
#    start_urls = [
#        'http://osl.ugr.es'
#    ]
#    rules = [
#        Rule(LinkExtractor(allow=('//', )), callback='parse_item', follow=True)
#    ]
#    
#    def parse_item(self, response):
#        if response.xpath('//article[@id]') is not None:
#            item = scrapy.Item()
#    #        item['titulo'] = response.xpath('//a').extract()
#    #        item['autor'] =
#    #        item['contenido'] = 
#            item['cat'] = response.xpath('class')
#            item['tag'] = response.xpath('class')
#            print item
#            return item
