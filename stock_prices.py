import requests
import json

base_url = "https://api.alphasquare.co.kr/data/v2/price/current-price?"
search_url = "https://api.alphasquare.co.kr/api/square/autocomplete/stock"

print('종목명 입력: ', end='')
stock_name = str(input())

param = {"stock":stock_name}
response = requests.post(search_url, data=param)

stocks = json.loads(response.text)

index = 0
if len(stocks) == 0:
    print('일치하는 종목명이 없습니다')
    exit(-1)

if len(stocks) > 1:
    count = 0
    for s in stocks:
        print(count+1, s['cname'])
        count += 1

    print(f'종목 선택[1-{count}]: ', end='')
    index = int(input())
    index -= 1

stock_num = stocks[index]['code']
response = requests.get(base_url+f"code={stock_num}")

price_json = json.loads(response.text)
open = int(price_json[stock_num]["open"])
close = int(price_json[stock_num]["close"])
prev_close = int(price_json[stock_num]["prev_close"])
updown_ratio = round((close - prev_close) / prev_close * 100, 2)
volume = price_json[stock_num]["volume"]
volume_valued = price_json[stock_num]["volume_valued"]
print(f'{stocks[index]["cname"]} 시초가: {open}, 현재가: {close}, 전일대비등락률: {updown_ratio}%')
for i in range(len(stocks[index]["cname"])):
    print('  ', end='')
print(f' 거래량: {volume}, 거래대금: {volume_valued}')
