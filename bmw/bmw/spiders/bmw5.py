# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem

class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/4350.html#pvareaid=2042194']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class = 'uibox-title']/a/text()").get()
            urls = uibox.xpath(".//li/a/img/@src").getall()
            for url in urls:
                # url = "https:" + url
                url = response.urljoin(url)
            # urls = map(lambda url:response.urljoin(url),urls)
                print(url)
                item = BmwItem(category=category, url=url)
                yield item



