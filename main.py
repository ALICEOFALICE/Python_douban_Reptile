print("hello world")
import requests
from lxml import etree
import pandas
douban_time_list=[]
douban_success_all=[]
url="https://www.douban.com/location/chengdu/events/week-all"
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}
douban=requests.get(url,headers=header)
douban_html=etree.HTML(douban.text)
douban_most_page=douban_html.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[2]/a[@*]/text()')[-1]

print(douban.status_code)
for url_num in range(1,int(douban_most_page)):
    douban_title_list=[]
    douban_time_list=[]
    douban_address_list=[]
    douban_pay_list=[]
    douban_creater_list=[]
    douban_participation_list=[]
    douban_like_list=[]
    url_lib="https://www.douban.com/location/chengdu/events/week-all?start="+str(int(url_num)*10)
    douban=requests.get(url_lib,headers=header)
    douban_html=etree.HTML(douban.text)
    douban_title_list=douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/div[@class='title']/a/@title")
    print(douban_title_list)
    for target_list in douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/ul[@class='event-meta']/li[@class='event-time']/text()"):
        douban_time_list.append(target_list.strip())
    while '' in douban_time_list:
        douban_time_list.remove('')
    print(douban_time_list)
    douban_address_list=douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/ul[@class='event-meta']/li[2]/@title")
    print(douban_address_list)
    douban_pay_list=douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/ul[@class='event-meta']/li[@class='fee']/strong/text()")
    print(douban_pay_list)
    douban_creater_list=douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/ul[@class='event-meta']/li[4]/a/text()")
    print(douban_creater_list)
    douban_participation_list=douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/p[@class='counts']/span[1]/text()")
    print(douban_participation_list)
    douban_like_list=douban_html.xpath("//li[@class='list-entry'][@*]/div[@class='info']/p[@class='counts']/span[3]/text()")
    print(douban_like_list)
    for title,time,address,pay,creater,participation,like in zip(douban_title_list,douban_time_list,douban_address_list,douban_pay_list,douban_creater_list,douban_participation_list,douban_like_list):
        tem_list=[]
        tem_list.append(title)
        tem_list.append(time)
        tem_list.append(address)
        tem_list.append(pay)
        tem_list.append(creater)
        tem_list.append(participation)
        tem_list.append(like)
        douban_success_all.append(tem_list)
print(douban_success_all)
data=pandas.DataFrame(data=douban_success_all,columns=["名称","时间","地点","费用","发起人","参与人数","感兴趣人数"])
data.to_excel(r"./test.xlsx",encoding="utf-8")
input("爬取完毕,按任意键退出")
