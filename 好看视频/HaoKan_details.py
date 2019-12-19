#! coding:utf-8 -*-
import time
import os
import requests
import re
import urllib
from requests.exceptions import RequestException
from GDG_link import f_l



def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None

    except RequestException:
        return None


def parse_Video(html):
    pattern = re.compile('<video class="video" src=(.*?)></video>'+'.*?<h2 class="videoinfo-title">(.*?)</h2>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        n_path = os.getcwd()
        urllib.request.urlretrieve(item[0], '{0}/{1}.mp4'.format(n_path,item[1]))


if __name__ =="__main__":
    for url_n in f_l:
        f_url = 'https://haokan.baidu.com/v?vid={0}'.format(url_n)
        html =get_one_page(f_url)
        parse_Video(html)
        time.sleep(1)
        print(f_url)






