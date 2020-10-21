# -*- coding: utf-8 -*-
# @project : watchdog
# @file   : scan_lianjia.py
# @time   : 2020-10-21

import requests
from bs4 import BeautifulSoup
import lxml
import json
import math

def main():
    cookies = {
        'lianjia_uuid': 'd5e1c07d-04fb-48ad-81d3-8e9c274b0a74',
        'UM_distinctid': '17470bef5cf61a-0b1d755302a55c-15336251-13c680-17470bef5d1c85',
        '_jzqc': '1',
        '_jzqx': '1.1599619398.1599619398.1.jzqsr=google%2Ecom|jzqct=/.-',
        '_smt_uid': '5f584146.98d850d',
        '_qzjc': '1',
        '_ga': 'GA1.2.41963018.1599619402',
        'select_city': '110000',
        'lianjia_ssid': 'a1ccac83-d2de-4c53-aa14-2950f6c2de10',
        'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1603264771',
        'CNZZDATA1253477573': '682320383-1599618897-https%253A%252F%252Fwww.google.com%252F%7C1603262268',
        'CNZZDATA1254525948': '856817249-1599617858-https%253A%252F%252Fwww.google.com%252F%7C1603263607',
        'CNZZDATA1255633284': '1348733405-1599616573-https%253A%252F%252Fwww.google.com%252F%7C1603264269',
        'CNZZDATA1255604082': '1813226886-1599614958-https%253A%252F%252Fwww.google.com%252F%7C1603263542',
        '_jzqa': '1.2358846149395703000.1599619398.1599619398.1603264771.2',
        '_jzqckmp': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217470befa7770d-02781f6c5cecb8-15336251-1296000-17470befa78c69%22%2C%22%24device_id%22%3A%2217470befa7770d-02781f6c5cecb8-15336251-1296000-17470befa78c69%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
        '_gid': 'GA1.2.1647573117.1603264773',
        'Hm_lpvt_9152f8221cb6243a53c83b956842be8a': '1603264889',
        '_qzja': '1.1595082764.1599619398602.1599619398602.1603264771114.1603264884932.1603264889463.0.0.0.7.2',
        '_qzjb': '1.1603264771114.6.0.0.0',
        '_qzjto': '6.1.0',
        '_jzqb': '1.6.10.1603264771.1',
        'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiZmUwYTkyNGIwMTFiYjk0NDg5MTNjMmQwYWI2MDc3ZWFkNmE2MGNkZDM3ZjYyMTg2ZDE4OTc4MDY4MThiMTMwYmMzYjI0YTE1N2Y3NWYyOGZjMDVlNDhmOTQzOWExMjllNjZiODE5ZGZmOWQ0NzIwMTYwYmE5MDg3NjQ4ZmNmMDBkMzliZGQxZTgyN2M1Y2MyYjdkYTljMzc5NWQ5NzM4MDg1NTIwMmY4YzM0NGIyNzgxMTA5MTJhN2Y1ZjAxNGM1OTIyOGQxMDM0YWIzMzY4M2U0NGJkODNjZGNjMTI1OTFjZjE5ZTQxMjYwZjI1MGE4MzVhZmM1ZGYxOTA4ODU5NDI4ZjIwYjRhYWMwNDk4M2I3OGQyMDcyYmZlN2RmYzJhMTU1MDIyYzdiYzE0MDVjYzQ5OTA3NGQ0MWU0ZWFkMjM4MWU0MDFkMzA5NDU5MzhhMDBkYmI3ZjBiNDk2MGVmZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI3ODQwMTdiM1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvMTAxMTA5NDMyNDE5Lmh0bWwiLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get('https://bj.lianjia.com/ershoufang/101109432419.html', headers=headers, cookies=cookies)
    # print (response.content)

    soup = BeautifulSoup(response.content, "lxml")
    price = soup.find("span", {"class": "total"}).get_text()
    # print (price)

    shoufu_data = soup.find("div", {"class": "new-calculator VIEWDATA"}).get("data-shoufu")
    # print (shoufu_data)

    shoufu_json = json.loads(shoufu_data)
    shoufu = shoufu_json.get("totalShoufuDesc", None)
    # print (shoufu)

    unitprice = soup.find("span", {"class": "unitPriceValue"}).get_text().replace("元/平米", "")

    area = soup.find("div", {"class": "area"}).find("div", {"class": "mainInfo"}).get_text().replace("平米", "")

    # unitprice = math.ceil(float(price)/float(area)*10000)
    print (price, shoufu, unitprice, area)

if __name__ == '__main__':
    main()