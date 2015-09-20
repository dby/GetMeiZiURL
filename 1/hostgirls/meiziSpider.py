#coding:utf-8
import re
import time
from lxml import html
import requests
import random

'''
    爬虫模块
    这一模块主要负责从网上将妹子爬下来
'''
class MeiZiSpider:
        
    baseUrl =  "http://www.dbmeinv.com/dbgroup/show.htm?pager_offset="
    meiziArray = []

    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ] 
    
    '''
        获得某一页的妹子
    '''
    def getMeiZiAtPage(self, pageNum, cid):
        self.meiziArray = []
        headers = {'User-Agenr': random.choice(self.user_agents)}
        meiziUrl = self.baseUrl + str(pageNum)
        if cid > 1:
            meiziUrl += "&cid=" + str(cid)
        print meiziUrl
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
    print MeiZiSpider().getMeiZiAtPage(2, 2)

