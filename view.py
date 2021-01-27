#!C:\Users\SON\AppData\Local\Programs\Python\Python39\python.exe
#시각적 부분을 담당하는 함수를 넣는 모듈

import os, html_sanitizer

def getList():
  sanitizer = html_sanitizer.Sanitizer()
  files = os.listdir('data') #data 디렉토리의 파일목록을 리스트로 변수에 담는다
  listStr = ''

  #html 코드로 들어갈 string
  #{}로 포맷필드 이름을 입력하고, format() 안에 해당 변수 이름을 준다
  for item in files:
      item = sanitizer.sanitize(item)
      listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
  #files의 목록을 하나씩 li 태그로 listStr에 추가해줌>밑의 html에 쓰임
  
  return listStr