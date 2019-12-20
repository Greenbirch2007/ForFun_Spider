#! coding:utf-8 -*-
import time
import os
import requests
import re
import urllib
from requests.exceptions import RequestException
from GDG_link import f_l



# def get_one_page(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#         return None
#
#     except RequestException:
#         return None
#
#
# def parse_Video(html):
#     pattern = re.compile('<video class="video" src=(.*?)></video>'+'.*?<h2 class="videoinfo-title">(.*?)</h2>',re.S)
#     items = re.findall(pattern,html)
#     for item in items:
#         n_path = os.getcwd()
#         urllib.request.urlretrieve(item[0], '{0}/{1}.mp4'.format(n_path,item[1]))
#
#
# if __name__ =="__main__":
#     for url_n in f_l:
#         f_url = 'https://haokan.baidu.com/v?vid={0}'.format(url_n)
#         html =get_one_page(f_url)
#         parse_Video(html)
#         time.sleep(1)
#         print(f_url)





# -----------------重构代码　1:写一个类，用类中的方法互相调用  2. 用with open上下文来下载-


# self
class Gdgvedio(object):
    def __init__(self,url):# 初始化时，直接传入url,相当于过渡了一层
        self.url =url

    def get_one_page(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                s_response = response.text
                return s_response
            return None

        except RequestException:
            return None

    def parse_Video(self):
        s_html = self.get_one_page()
        pattern = re.compile('<video class="video" src=(.*?)></video>'+'.*?<h2 class="videoinfo-title">(.*?)</h2>',re.S)

        items = re.findall(pattern,s_html)
        for item in items:
            n_path = os.getcwd()

            # 　使用request.urlretrieve 来下载
            urllib.request.urlretrieve(item[0], '{0}/{1}.mp4'.format(n_path,item[1]))







if __name__ =="__main__":
    for url_n in f_l:
        f_url = 'https://haokan.baidu.com/v?vid={0}'.format(url_n)
        v = Gdgvedio(f_url)
        v.parse_Video()