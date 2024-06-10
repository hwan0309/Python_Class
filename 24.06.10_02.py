import time
import datetime

시간 = time.time()
시간 = time.ctime(시간)
시간 = time.localtime()

print('현재시간:' + str(시간.tm_hour)+'시')
a = time.strftime('%Y year %m month',시간)
print(a)

name = 'yoon'
print(f'안녕하세요 {name}' )

aa = datetime.datetime(2024, 6, 11)
print(aa)