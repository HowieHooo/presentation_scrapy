# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmojiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    emoji_handle = scrapy.Field()
    emoji_image = scrapy.Field()
    emoji_link = scrapy.Field()
    section = scrapy.Field()



	
