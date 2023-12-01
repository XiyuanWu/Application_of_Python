import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import random

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

titles = []
position_icons = []
house_icons = []
price_infos = []
total_prices = []
unit_price = []

for page in range(1, 6):
    url = f"https://nocturne-spider.baicizhan.com/practise/61/PAGE/{page}.html"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        continue
    soup = BeautifulSoup(response.text, 'lxml')
    content_all = soup.find_all(class_="info clear")

    for content in content_all:
        title = content.find(class_="title").contents[1].string
        titles.append(title)
        position = content.find(class_="positionInfo").a.string
        position_icons.append(position)
        house = content.find(class_="houseInfo").contents[2].replace('\n', '').replace('\r', '')
        house_icons.append(house)
        totalPrice = content.find(class_="totalPrice totalPrice2").text.replace('\n', '').replace('\r', '')
        total_prices.append(totalPrice)
        unitPrice = content.find(class_="unitPrice").span.string
        unit_price.append(unitPrice)

        print(f"{title},{position},{house},{totalPrice},{unitPrice}")

total = {"房屋户型": titles, "小区地址": position_icons, "建筑信息": house_icons, "单价价格(元/平方)": unit_price,"房子总价/万": total_prices}

info = pd.DataFrame(total)

writer = pd.ExcelWriter("/Users/二手房.xlsx")

info.to_excel(excel_writer=writer, sheet_name="成都")

writer.save()