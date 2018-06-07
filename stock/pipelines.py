# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from stock.mysqldb import *

class StockPipeline(object):
    def process_item(self, item, spider):

        insert(item['type'],item['name'])


        return item
