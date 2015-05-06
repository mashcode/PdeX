import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'crolpdf'
    allowed_domains = ['nyc.gov']
    start_urls = ['http://www.nyc.gov/html/dcas/html/about/cityrecord_editions.shtml']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('\.pdf', ), )), 
        # deny=('subsection\.php', )

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = scrapy.Item()
#       item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//ul/li/text()').extract()
        item['link'] = response.xpath('//ul/li/a/@href').extract()
        item['description'] = response.xpath('//ul/li/text()').extract()    
        
#        filename = response.url.split("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)

        return item


