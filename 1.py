# 不太完善，抓取到图片分辨率不是1920*1080
import requests
from lxml import etree
from urllib.request import urlretrieve
import os
import time
if not os.path.exists('Miss'):
    os.mkdir('Miss')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
url = 'http://www.netbian.com/meinv/index_{}.htm';

class Beauty(object):

    def miss_sister(self):
        for i in range(1, 5):
            time.sleep(1)
            if i == 1:  
                urls = 'http://www.netbian.com/meinv/index.htm'
            else:
                urls = url.format(i)
            print(urls + "获取列表")

            r = requests.get(urls,headers=headers)
            r.encoding = 'gb2312'
            html = etree.HTML(r.text)
            self.xpath_data(html)

    def xpath_data(self,html):
        r_list = html.xpath('//*[@id="main"]/div[2]/ul/li/a')

        for i in r_list:
            pic_1 = i.xpath('.//@src')[0]
            name_2 = i.xpath('.//b/text()')[0].strip( )
            print('正在下载图片_%s' % name_2 )
            urlretrieve(pic_1,'Miss/%s.jpg' % name_2)
            time.sleep(1)




beauty = Beauty()
beauty.miss_sister()
