import scrapy


class ShopecommerceSpider(scrapy.Spider):
    name = "shopecommerce"
    allowed_domains = ["www.scrapingcourse.com"]
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]

    def parse(self, response):
        pass
