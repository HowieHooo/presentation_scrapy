import scrapy
from scrapyspider_OReilly.items import EmojiSpiderItem

class EmoSpider(scrapy.Spider):
	name = 'emo'
	allowed_domains = ['emoji-cheat-sheet.com']
	start_urls = [
	    'http://www.emoji-cheat-sheet.com/',
	]

	def parse(self, response):
                #find all h2 h3 selector in document
		headers = response.xpath('//h2|//h3')
		lists = response.xpath('//ul')
		all_items = []
		for header, list_cont in zip(headers, lists):
			#get the emoji title
			section = header.xpath('text()').extract()[0]
			for li in list_cont.xpath('li'):
				item = EmojiSpiderItem()
				item['section'] = section
				#get the two spans
				spans = li.xpath('div/span')
				if len(spans):
					#first span contains link, extract it
					link = spans[0].xpath('@data-src').extract()
					if link:
						item['emoji_link'] = response.url + link[0]
					handle_code = spans[1].xpath('text()').extract()
				#not a link, get the text
				else:
					handle_code = li.xpath('div/text()').extract()
				if handle_code:
					item['emoji_handle'] = handle_code[0]
				all_items.append(item)
		return all_items
