# 파일 = open('a.txt', 'w')
# 파일.write('hello')
# 파일.close()
#
# 파일 = open('a.txt','a')
# 파일.write('\n반가워')
# 파일.close()
#
# 파일 = open('a.txt', 'r')
# print(파일.read())
# 파일.close()


# f = open('data.csv', 'w')
# f.write('김, 이, 박')
# f.write('\n김, 이, 박')
# f.close()

# 리스트 = open('list.txt', 'w')
# 리스트.write[
#     '삼성전자',
#     '\n카카오',
#     '\n네이버',
#     '\n신풍제약'
# ]
# 리스트.close()

# for i in range(2,10):
#     for i2 in range(1,10):
#         print(i, '*', i2, '=', i * i2)

리스트 = ['삼성전자','카카오','네이버','신풍제약']
파일 = open('ab.txt','w')

for i in range(4):
       파일.write(리스트[i] + '\n')
파일.close()


