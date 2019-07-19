students = {
    '01' : {
        '순번': '01',
        '이름': '김성훈'
        },
    '02' :{
        '순번': '02',
        '이름': '김은정'
        }
}

import csv
import pprint
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=864'
# 1. 요청
# json ->
# 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
with open('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름'] # 여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
    csv_writer.writeheader()
    for item in students.values(): # 딕셔너리 만든 것 반복
        csv_writer.writerow(item)