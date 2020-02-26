import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.17.50.43/varsity/gallery.html']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield{
                'Image Link': x.xpath(newsel).extract_first()
            }