
from scrapy import Spider, Request
from Broadway_Shows.items import BroadwayShowsItem
import re
from datetime import date, timedelta

class BroadwayShowSpider(Spider):
    name = 'broadway_shows_spider'
    allowed_urls = ['http://playbill.com/']
    start_urls = ['http://www.playbill.com/grosses']

    def parse(self, response):
        
        start_date = date(2019, 10, 20)
        end_date = date(1985, 6, 23)
        urls = ['http://www.playbill.com/grosses?week=' + str(start_date - timedelta(days = d)) for d in range(0, (start_date - end_date).days + 1, 7)]

        i = 0
        for url in urls:
            week = start_date - timedelta(days = i * 7)
            yield Request(url = url, callback = self.parse_weekly_page, meta = {'week': week})
            i += 1

    def parse_weekly_page(self, response):

        week = response.meta['week']
        rows = response.xpath('*//table/tbody/tr')

        for i in range(len(rows)):
            # week = start_date - timedelta(days = d)
            show = rows[i].xpath('./td[1]/a/span/text()').extract_first().replace('—', ' - ')
            theater = rows[i].xpath('./td[1]/span/text()').extract_first()
            weekly_gross = float(''.join(re.findall('[e.+-]?[0-9]+', rows[i].xpath('./td[2]/span/text()').extract_first())))
            avg_price = float(''.join(re.findall('[e.+-]?[0-9]+', rows[i].xpath('./td[4]/span/text()').extract()[0])))
            top_price = float(''.join(re.findall('[e.+-]?[0-9]+', rows[i].xpath('./td[4]/span/text()').extract()[1])))
            seats_sold = int(rows[i].xpath('./td[5]/span/text()').extract()[0])
            theater_size = int(rows[i].xpath('./td[5]/span/text()').extract()[1])
            performance = int(rows[i].xpath('./td[6]/span/text()').extract()[0])
            preview = int(rows[i].xpath('./td[6]/span/text()').extract()[1])
            attendance_rate = float(rows[i].xpath('./td[7]/span/text()').extract_first().strip('%'))/100

            item = BroadwayShowsItem()
            item['week'] = week
            item['show'] = show
            item['theater'] = theater
            item['weekly_gross'] = weekly_gross
            item['avg_price'] = avg_price
            item['top_price'] = top_price
            item['seats_sold'] = seats_sold
            item['theater_size'] = theater_size
            item['performance'] = performance
            item['preview'] = preview
            item['attendance_rate'] = attendance_rate

            yield item 