#wykorzystuje biblioteke scrapy
#crawler/crawler/spiders/crawling_spiders do sprawdzenia samego crawlera
from scrapy.crawler import CrawlerProcess
from crawler.crawler.spiders.crawling_spiders import CrawlingSpider

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "strony.xml": {"format": "xml",
                           "overwrite": True
            },
        },
    })

    process.crawl(CrawlingSpider)
    process.start()
