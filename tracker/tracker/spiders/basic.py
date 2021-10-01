# -*- coding: utf-8 -*-
# Scraped -> check -> pipeline -> store -> push  

import scrapy
import sqlite3
import datetime
import re

from mailer import mailer 


from scrapy.http import Request

year = str(datetime.datetime.now().year) 
month = str(datetime.datetime.now().month)
base_url = "https://ves.ac.in/wp-content/uploads/sites/3"

url = base_url + "/" + year + "/" + "0" + month
#url = base_url + "/" + year + "/" + "03"
print(url)

class BasicSpider(scrapy.Spider):
	name = 'basic'
	allowed_domains = ['ves.ac.in']

	start_urls = [url]

	def parse(self, response):
		selector = 'table tr td a[href$=".pdf"]::attr(href)'
		for href in response.css(selector).extract():
			yield Request(
				url = response.urljoin(href),
				callback=self.save_pdf
			)


	def save_pdf(self, response):
		path = response.url.split('/')[-1]
		#print("saving at {}".format(path))


		#self.logger.info('Saving PDF %s',path); # ignore under specialcircum

		match = False 
		
		with open('d_record.txt', 'r') as dr:
			for line in dr:
				if path == line.strip('\n'):
					print('Match found')
					match = True
					break
		
		if match == False:
			self.logger.info('Saving PDF %s',path); 
			with open('d_record.txt', 'a') as dr:
				dr.write("{}\n".format(path)) # formatter used to record to next line

			with open(path, 'wb') as file:
				file.write(response.body)

			mailer(path)

		elif match == True:
			print("Document already preset")
		else:
			print("Someting else went wrong")