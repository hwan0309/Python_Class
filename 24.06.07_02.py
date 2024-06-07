import requests
from bs4 import BeautifulSoup

종목들 = ['005930', '066575', '005380','035720', '034220','003490']
#리스트 = []
def 현재가(구멍) :
    데이터 = requests.get(f' https://finance.naver.com/item/sise.nhn?code={구멍}')
    soup = BeautifulSoup(데이터.content,'html.parser')
    print(soup.find_all('strong',id="_nowVal")[0].text)
    print(soup.find_all('span', class_="tah")[5].text)
    return soup.find_all('strong',id="_nowVal")[0].text
    #리스트.append(soup.find_all('strong',id="_nowVal")[0].text)

현재가('066575')

f=open('b.txt','w')
# for i in range(6):
#     f.write('\n' + 현재가(종목들[i] ) )

for i in 종목들:
    f.write('\n' + 현재가(i) )

f.close()



#이미지 = soup.select('#img_chart_area')[0] #css 형태 class 는 .태그, 띄어쓰기 내부요소 선택
#soup.select('.') #css 형태 id 는 #태그
#print(이미지['src'])