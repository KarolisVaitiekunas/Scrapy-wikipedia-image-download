import scrapy

class ParisSpider(scrapy.Spider):
    name = 'paris'
    allowed_domains = ['https://en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        raw_image_urls = response.xpath('//img/@src').getall()
        clean_image_urls = []
        for img_url in raw_image_urls:
           clean_image_urls.append(response.urljoin(img_url)) #urljoin funcion converts whatever url you give it into absolute url
        yield{
            "image_urls": clean_image_urls
        }
