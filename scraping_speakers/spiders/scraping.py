# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'scrapSites'
    start_urls = [
        'https://www.tech-festival.com/2019-speakers',
    ]

    def parse(self, response):
        for quote in response.css('div.m-speakers-list__items__item__header'):
            yield {
#                'link': quote.xpath('./a[@class="full-link"]/@href').extract(),
'author': quote.css('h3.m-speakers-list__items__item__header__title > a.m-speakers-list__items__item__header__title__link js-librarylink-entry::text').extract_first(),
'position': quote.css('span.m-speakers-list__items__item__header__meta__position::text').extract_first(),
'company': quote.css('span.m-speakers-list__items__item__header__meta__company::text').extract_first()
            }
# Go to next page            
#        next_page_url = response.css("li.next > a::attr(href)").extract_first()
#        if next_page_url is not None:
#            yield scrapy.Request(response.urljoin(next_page_url))
