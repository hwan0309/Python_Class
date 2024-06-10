import requests
import json
import time

data = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/5?code=CRIX.UPBIT.KRW-BTC&count=200&ciqrandom=1717984134563')
#print(data.content)

딕셔너리 = json.loads(data.content)

for i in range(200):
   print(딕셔너리[i]['tradePrice'])
   시간 = (딕셔너리[i]['timestamp'])
   글자시간 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(시간/1000))
   print(글자시간)
