from urllib.parse import quote
import scrapy
from stock.items import StockItem
from scrapy import Request
import logging
from stock.mysqldb import *
import copy
import re


class FootballSpider(scrapy.Spider):
    text = '黄河源股权投资基金管理(苏州工业园区)有限公司'
    text = quote(text, encoding='gb2312')
    name = 'stock'


    start_urls = ['http://data.eastmoney.com/gdfx/search.aspx?kwd=' + text]

    def start_requests(self):
        for i in range(0, 1000):
            company = select_company(i)
            if not re.match('基金代码', company):
                text = quote(company, encoding='gb2312')
                url = 'http://data.eastmoney.com/gdfx/search.aspx?kwd=' + text
                Request(url=url, callback=self.parse, meta={'name': copy.deepcopy(company)})

    def parse(self, response):
        item = StockItem()
        try:
            item['type'] = response.xpath(
                '//*[@id="page"]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/table/tbody/tr[1]/td[2]/text()').extract()[
                0]
            item['name'] = response.meta['name']
            print(item['name'],item['type'])
        except:
            logging.info('------类型不存在---------')
