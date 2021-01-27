#!C:\Users\SON\AppData\Local\Programs\Python\Python39\python.exe
# http://localhost:81/cgi-bin/index.py

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value #고유값으로 사용

 
os.remove('data/'+pageId) #파이썬의 파일을 지우는 함수
 
#Redirection
print("Location: index.py")
print()