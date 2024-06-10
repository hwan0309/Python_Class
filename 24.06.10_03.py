import requests
import json
import time

url = [
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000,
  https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000,
]

def 함수(구멍):
    data = requests.get(구멍)
    딕셔너리 = json.loads(data.content)
    return 딕셔너리['data'][0]['Close']

#함수(url[0])

from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
pool.map()
pool.close()
pool.join()


# 리스트 = [2,3,4,5,6]
#
# def 더해주셈(x):
#     return x + 1
#
# result = map(더해주셈, 리스트)
# print(result)