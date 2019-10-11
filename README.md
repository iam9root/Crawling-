# Crawling-
## 네이버 웹툰 Crawling-1
* requests를 이용해서 네이버 웹툰 페이지에 get 요청 전송
* get 요청으로 변환된 html 텍스트 데이터를 BeautifulSoup을 사용해서 파싱된 객체를 soup 변수에 저장
* prettify 함수는 BeautifulSoup 에서 파실 처리한 파서 트리를 유니코드 형태로 리턴하는 함수
* CSS selectors 를 사용해서 a 태그의 class 명이 title 인 데이터들을 class_title_a_list 에 저장해서 해당 데이터 출력
* 전체 웹툰들의 제목 문자열 목록
* '제목(URL)' 포멧으로 출력
* list.txt 파일에 '제목(링크)' 텍스트 포멧으로 저장
* '웹툰 제목(링크)' 텍스트 리스트 형태로 저장된 list 라는 이름의 html 파일 생성
* 
