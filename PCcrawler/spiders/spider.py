#!/usr/bin/python
# -*- coding:utf-8 -*-  

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
                article_name = sel.xpath('//a/text()').extract()
                article_url = str(response.url)

                item['article_name'] = [n.encode('utf-8') for n in article_name]
                item['article_url'] = article_url.encode('utf-8')

                yield item

	def link_filtering(self, links):
		ret = []
		for link in links:
			print 
			ret.append(link)
			
		return ret
