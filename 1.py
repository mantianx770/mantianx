import requests
from lxml import etree
from urllib.request import urlretrieve

# url = 'https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1502950999.03.webp'
# urlretrieve(url,'1.png')
import time

def get_small_sister():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    url = 'https://www.vmgirls.com/campus'

    resp = requests.get(url, headers=headers)

#     print(resp)
    resp_txt = resp.text
    # print(resp_txt)
    resp_html = etree.HTML(resp_txt)
    # print(resp_html)
    resp_list = resp_html.xpath('//div[@class="col-6 col-md-3 d-flex py-2"]')
    print(resp_list)

    for i in resp_list:

         pic_url = i.xpath('.//div[@class="post"]//img/@src')[0]
         name = i.xpath('.//div[@class="title"]/a/text()')[0].strip()
         print(pic_url,name)
         # print('正在下载图片_%s'%name)
         # urlretrieve(pic_url,'xiaojiejie/%s.jpg' % name)
         # time.sleep(1)


get_small_sister()


# for i in ros_list:
    #     pic_url = i.xpath('//div[@class="picBox"]//img//@src')
    #     name = i.xpath('//ul[@class="articleV4PicList oh"]/li/a//text()')
    #     print('正在下载图片_%s' % name)
    #     urlretrieve(pic_url, 'jiejiehao/%s.jpg' % name)
    #     time.sleep(1)
