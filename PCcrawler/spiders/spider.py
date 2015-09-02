#!/usr/bin/python
# -*- coding:utf-8 -*-  

import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from PCcrawler.items import PccrawlerItem

class PCcrawlerSpider(CrawlSpider):

        """继承自CrawlSpider，实现自动爬取的爬虫。"""

        name = "PCcrawler"
        #设置下载延时  
        download_delay = 2
        #allowed_domains = ['*']
        #第一篇文章地址  
        start_urls = ['http://news.baidu.com/']

	#rules = [Rule(LinkExtractor(allow=('/u012150179/article/details'),restrict_xpaths=('//li[@class="next_article"]')),callback='parse_item',follow=True)]
	rules = [Rule(LinkExtractor(allow=('//a')),process_links='link_filtering',callback='parse_item',follow=True)]

        def parse_item(self, response):

                item = PccrawlerItem()
                sel = Selector(response)
		all_hypers = sel.xpath('//a').extract()
		for i in all_hypers:
			obj = re.search(r'阅兵',i.encode('utf-8'),re.M|re.I)	
			if obj:
                		article_name = i 
                		article_url = 'I am a URL'

                		item['article_name'] = article_name.encode('utf-8') 
                		item['article_url'] = article_url.encode('utf-8')

                		yield item

	def link_filtering(self, links):
		ret = []
		for link in links:
			#print '\n'
			print 'link text:',link.text
			print 'link url:',link.url
			#print '\n' 
			ret.append(link)
			#s = raw_input('wait...')		
		return ret
