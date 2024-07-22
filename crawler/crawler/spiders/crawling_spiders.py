from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ["technologiegrzewcze.pl"]
    start_urls = ["http://www.technologiegrzewcze.pl/"]

    rules = (
        Rule(LinkExtractor(allow=''), callback='items'),
    )

    def items(self, response):
        yield{
            "url": response.url
        }