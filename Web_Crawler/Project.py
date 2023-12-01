import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import random

headers = {"User-Agent": "Mozilla/5.0"}

total_price_list = []
price_list = []
area_list = []
name_list = []
areaName_list = []
room_list = []

for page in range(1, 6):
    url = f"https://cd.ke.com/ershoufang/pg{page}su1ie2sf1l2p5/"
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    content_all = soup.find_all(class_="VIEWDATA CLICKDATA maidian-detail")

    for content in content_all:
        detail_url = content.attrs["href"]
        detail_res = requests.get(detail_url, headers=headers)
        detail_html = detail_res.text
        detail_soup = BeautifulSoup(detail_html, "lxml")
        total_price = detail_soup.find(class_="total").string
        total_price_list.append(total_price)
        price = detail_soup.find(class_="unitPriceValue").string
        price_list.append(price)
        area = detail_soup.find(class_="area").contents[1].string
        area_list.append(area)
        name = detail_soup.find(class_="communityName").contents[3].string
        name_list.append(name)
        areaName = detail_soup.find(class_="areaName").find(class_="info").contents[1].string
        areaName_list.append(areaName)
        room = detail_soup.find(class_="base").find("li").contents[1]
        room_list.append(room)
        print(f"{total_price},{price},{area},{name},{areaName},{room}")
        time.sleep(random.randint(1, 3))

total = {"房子总价/万": total_price_list, "单价价格(元/平方)": price_list, "建筑面积": area_list, "小区名称": name_list, "所在区域": areaName_list, "房屋户型": room_list}
info = pd.DataFrame(total)
writer = pd.ExcelWriter("二手房.xlsx")
info.to_excel(excel_writer=writer, sheet_name="成都")
writer.save()
writer.close()
