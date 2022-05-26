import scrapy


class GorvernanceSpider(scrapy.Spider):
    name = 'gorvernance'
    allowed_domains = ['gov.uniswap.org']
    start_urls = ['http://gov.uniswap.org/']

    def parse(self, response):
        titles = response.css('a.title::text').extract()
        links = response.css('a.title.raw-link.raw-topic-link::attr("href")').extract()
        # activity = replies = response.css('.relative-date::text').extract()

        for item in zip(titles, links, views):
            scraped_info = {
                'title' : item[0],
                'link' : item[1]
            }
            yield scraped_info