# requests를 이용해서 네이버 웹툰 페이지에 get 요청 전송

import requests
URL_TOTAL_LIST = 'https://comic.naver.com/webtoon/weekday.nhn'
response = requests.get(URL_TOTAL_LIST)
response.text


# get 요청으로 변환된 html 텍스트 데이터를 BeautifulSoup을 사용해서 파싱된 객체를 soup 변수에 저장

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')


# prettify 함수는 BeautifulSoup 에서 파실 처리한 파서 트리를 유니코드 형태로 리턴하는 함수

print(soup.prettify())


# CSS selectors 를 사용해서 a 태그의 class 명이 title 인 데이터들을 class_title_a_list 에 저장해서 해당 데이터 출력

class_title_a_list = soup.select('a.title')
len(class_title_a_list)

for a in class_title_a_list:
    print(a)


# 전체 웹툰들의 제목 문자열 목록

new_list=[]
for a in class_title_a_list:
    new_list.append(a['title'])
print(new_list)
print(list(set(new_list)))  # list 의 값 중복 제거


# '제목(URL)' 포멧으로 출력

for list in class_title_a_list:
    print('{0} (https://comic.naver.com{1})'.format(list['title'], list['href']))

# list.txt 파일에 '제목(링크)' 텍스트 포멧으로 저장

result = ''
for list in class_title_a_list:
    a_text = list.get_text()
    a_href = list['href']
    result += f'{a_text}({a_href})'

f = open('list.text','wt')
f.write('Djangostudy\n')
f.close()

f = open('list.txt','a')
f.write(result)
f.close()

# '웹툰 제목(링크)' 텍스트 리스트 형태로 저장된 list 라는 이름의 html 파일 생성

f = open('list.html', 'wt')

new_result = '''
<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=UTF-8">
    </head>
    <body>
'''

for list in class_title_a_list:
    a_text = list.get_text()
    a_href = list['href']
    new_result += '<a href="https://comic.naver.com{href}"> {text} </a><br>'.format(text=a_text, href=a_href)

new_result += '''
    </body>
</html>
'''
f.write(new_result)
f.close()

response = requests.get('https://shared-comic.pstatic.net/threquestsumb/webtoon/651673/thumbnail/thumbnail_IMAG10_659b9446-0940-494a-bb5f-5893290a84d0.jpg')
print(response)

f = open('image.jpg', 'wb')
f.write(response.content)
f.close()


