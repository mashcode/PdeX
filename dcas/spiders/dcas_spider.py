import scrapy

from dcas.items import CrolItem

class CrolSpider(scrapy.Spider):
    name = "crol"
    allowed_domains = ["nyc.gov"]
    start_urls = [
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2014editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2013editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2012editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2011editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2010editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2009editions.shtml",
        "http://www.nyc.gov/html/dcas/html/about/cityrecord_2008editions.shtml",
#        "http://www.nyc.gov/html/dcas/html/about/"
    ]
    def parse(self, response):
        for sel in response.xpath('//ul/li' '//span/p'):
            item = CrolItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
#           item['desc'] = sel.xpath('text()').extract()
            yield item

#        for sel in response.xpath('//span/p'):
#            item = CrolItem()
#            item['title'] = sel.xpath('a/text()').extract()
#            item['link'] = sel.xpath('a/@href').extract()
#            yield item


#        filename = response.url.split("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)

# Running crol
# pip install scrapy
# crawl and write to json
# scrapy crawl crol -o mload.json

# Convert json to yml
# npm install -g yamljs
# json2yaml mload.json > mload.yml --pretty
# or
# json2yaml mload.json > mload.yml --indentation 4


