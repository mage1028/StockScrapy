from urllib.parse import quote
import scrapy
from stock.items import StockItem
from scrapy import Request
import logging
from stock.mysqldb import *
import copy
import re


class FootballSpider(scrapy.Spider):

    name = 'stock'


    def start_requests(self):

        companys = select_company()
        for i in range(1, len(companys)):
            company = companys[i][0]
            if not re.match('基金代码',company):
                try:


                    text = quote(company, encoding='gb2312')
                    url = 'http://data.eastmoney.com/gdfx/search.aspx?kwd=' + text
                    yield Request(url=url, callback=self.parse, meta={'name': copy.deepcopy(company)})
                except:
                    print(company)

    def parse(self, response):
        item = StockItem()
        try:
            item['type'] = response.xpath(
                '//*[@id="page"]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/table/tbody/tr[1]/td[2]/text()').extract()[
                0]
            item['name'] = response.meta['name']
            print(item['name'], item['type'])
        except:
            logging.info('------类型不存在---------')
