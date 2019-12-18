import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 正则和lxml混用
def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list =[]
    f_l = []

    patt = re.compile('vid=(.*?)",',re.S)
    items = re.findall(patt,html)
    # for item in items:
    #
    #     f_l.append("https://haokan.baidu.com/v?vid="+item)
    #
    # f_tup =tuple(f_l)
    # big_list.append(f_tup)


    return items













def insertDB(content):

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='FUN',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into HaoKan_link (HK_link) values (%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    for n in range(1,501):

        url = 'https://haokan.baidu.com/videoui/page/pc/search?pn='+str(n)+'&rn=10&_format=json&tab=video&query=%E9%83%AD%E5%BE%B7%E7%BA%B2%E7%9B%B8%E5%A3%B0'
        html = call_page(url)
        content = parse_html(html)
        print(content)
        time.sleep(1)
        insertDB(content)


# create table HaoKan_link(
# id int not null primary key auto_increment,
# HK_link varchar(255)
# ) engine=InnoDB  charset=utf8;


# drop table HaoKan_link;