#!C:\Users\SON\AppData\Local\Programs\Python\Python39\python.exe
# http://localhost:81/cgi-bin/index.py

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value #고유값으로 사용
title = form["title"].value
description = form['description'].value
 
opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()
 
os.rename('data/'+pageId, 'data/'+title) #파이썬의 파일 이름 바꾸는 함수. os를 import해야 사용가능
 
#Redirection
print("Location: index.py?id="+title)
print()