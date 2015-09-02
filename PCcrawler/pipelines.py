# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class PccrawlerPipeline(object):
	''' save data '''
	def __init__(self):
		self.file_1 = codecs.open('result.json', mode='wb', encoding='utf-8')
		self.file_2 = codecs.open('data.json', mode='wb', encoding='utf-8')

    	def process_item(self, item, spider):
		article_name = ''.join(item['article_name'])
                search_str = ['70周年','阅兵']
                for s in search_str:
                        if s in article_name:
                                line = json.dumps(dict(item)) + '\n'
                                self.file_1.write(line.decode("unicode_escape"))
				break
		else:
			line = json.dumps(dict(item)) + '\n'
			self.file_2.write(line.decode("unicode_escape"))

        	return item

