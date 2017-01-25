# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TotalimmoItem(scrapy.Item):
	# define the fields for your item here like:
    # name = scrapy.Field()
    immo_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    zip_code = scrapy.Field()
    district = scrapy.Field()
    contact_name = scrapy.Field()
    media_count = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    sqm  = scrapy.Field()
    rent = scrapy.Field()
    rooms = scrapy.Field()
	# time_to = scrapy.Field()  # time to destination using transit or driving
	

