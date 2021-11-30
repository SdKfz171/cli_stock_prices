import requests
import json

base_url = "https://api.alphasquare.co.kr/data/v2/price/current-price?"
search_url = "https://api.alphasquare.co.kr/api/square/autocomplete/stock"

print('type stock\'s name: ', end='')
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

    print(f'choose stock name[1-{count}]: ', end='')
    index = int(input())
    index = index - 1

stock_num = stocks[index]['code']
response = requests.get(base_url+f"code={stock_num}")

price_json = json.loads(response.text)
print(f'{stocks[index]["cname"]} 현재가: {price_json[stock_num]["close"]}')
