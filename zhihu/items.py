# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    excerpt = scrapy.Field()
    follower = scrapy.Field()
    visit = scrapy.Field()
    answers = scrapy.Field()

