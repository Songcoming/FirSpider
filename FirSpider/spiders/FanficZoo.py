# !/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.spiders import Spider

import scrapy
import re

class FanficZoo(Spider):
	name = "fanficzoo"
	allowed_domains = ["www.fanfiction.net"]
	start_urls = ["https://www.fanfiction.net/search.php?ready=1&keywords=zootopia&type=story&ppage=1"]

	def parse(self, response):
		for artical in response.css("div.z-list"):
			info = artical.css("div.z-padtop2::text").extract_first()
			isexist = re.search(r'Reviews:\s(.*?)\s', info)
			if isexist and int(isexist.group(1)) >= 100:
				yield {
					"arturl": "https://www.fanfiction.net" + artical.css("a.stitle::attr(href)").extract_first(),
					"title" : re.search(r'<img .*>(.*?)</a>', re.sub(r'</?b>', '', artical.css("a.stitle").extract_first())).group(1),
					"author": re.sub(r'-', ' ', artical.css("a::attr(href)").re(r'\/u\/\d*\/(.*)')[0]),
					"disc"  : re.search(r'z-padtop">(.*?)<div class="z-padtop2', re.sub(r'</?b>', '', artical.css("div.z-indent").extract_first())).group(1),
					"info"  : info
				}

		pagelist = response.css("center").css("a")
		nextpage = pagelist[-1]
		if re.match(r'^Next', nextpage.css("a::text").extract_first()):
			url = response.urljoin("https://www.fanfiction.net/search.php" + nextpage.css("a::attr(href)").extract_first())
			yield scrapy.Request(url, self.parse)