# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exporters import XmlItemExporter

class XmlExportPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class HtmlExportPipeline(object):
    def __init__(self):
        self.files = {}
        self.file = None
        self.html = '<html><head><title>POSTS</title></head><body><table border="1">'

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('%s.html' % spider.name, 'w+b')

    def spider_closed(self, spider):
        self.html += '</table></body></html>'
        self.file.write(self.html)
        self.file.close()

    def process_item(self, item, spider):
        for j in item:
            self.html += '<tr>'
            if type(item[j]) is list:
                self.html += '<td>%s</td><td>' % j
                for y in item[j]:
                    self.html += ' %s ,' % y.encode('ascii', 'replace')
                self.html += '</td>'
            else:
                self.html += '<td>%s</td><td>%s</td>' % (j, item[j].encode('ascii', 'replace'))
            self.html += '</tr>'
        return item
