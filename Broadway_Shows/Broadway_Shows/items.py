# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BroadwayShowsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    week = scrapy.Field()
    show = scrapy.Field()
    theater = scrapy.Field()
    weekly_gross = scrapy.Field()
    avg_price = scrapy.Field()
    top_price = scrapy.Field()
    seats_sold = scrapy.Field()
    theater_size = scrapy.Field()
    performance = scrapy.Field()
    preview = scrapy.Field()
    attendance_rate = scrapy.Field()
    
