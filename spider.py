import requests
from lxml import etree
import db
import time

def get_weather(url):
    # 爬取数据 入库sql
    r = requests.get(url, headers = {"user-agent":"mozilla/5.0"})
    print(r.url)
    t = etree.HTML(r.text)
    ul = t.xpath("//ul[@class='lishitable_content clearfix']")[0]
    for i in ul.xpath("./li")[:-1]:
        temp = i.xpath("./div/text()")
        if len(temp) == 4:
            date = i.xpath("./div/a/text()")[0]
            if date:
                temp = [date] + temp
        db.insert_data(temp)

def page(url):
    # 获取所有月份
    # 返回2011年之后 每个月的href 
    r = requests.get(url, headers = {"user-agent":"mozilla/5.0"})
    t = etree.HTML(r.text)
    return t.xpath("//div/ul[@class='clearfix']/li/a/@href")

def main():
    # get_weather()
    for href in page(url):
        get_weather(href)
        time.sleep(timeout)

if __name__ == "__main__":
    url = 'http://lishi.tianqi.com/guangzhou/index.html'
    timeout = 0
    main()