#coding:utf-8
import re
import time
from lxml import html
import requests

'''
    爬虫模块
    这一模块主要负责从网上将妹子爬下来
'''
class MeiZiSpider:
        
    baseUrl =  "http://www.dbmeinv.com/?pager_offset="
    meiziArray = []
    
    '''
        获得某一页的妹子
    '''
    def getMeiZiAtPage(self, pageNum):

        #for page in range(2598, 1, -1):
        meiziUrl = self.baseUrl + str(pageNum)
        r = requests.get(meiziUrl)
        doc = html.document_fromstring(r.text)
        xdivs = doc.xpath('//div[@class="img_single"]')

        for div in xdivs:
            meizi = {}
            href = div.xpath('.//a')[0]
            img = div.xpath('.//img')[0]
            meizi['topiclink'] = href.xpath('@href')[0]
            meizi['title'] = img.xpath('@title')[0]
            meizi['imgsrc'] = img.xpath('@src')[0]
            meizi['startcount'] = 0
            self.meiziArray.append(meizi)

        return self.meiziArray

if __name__ == '__main__':
    dbmeiziSpider()

