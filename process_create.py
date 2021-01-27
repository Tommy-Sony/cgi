#!C:\Users\SON\AppData\Local\Programs\Python\Python39\python.exe
# http://localhost:81/cgi-bin/index.py

import cgi
form = cgi.FieldStorage() #브라우저에서 전송한 정보를 해당 form 변수에 받아옴
title = form["title"].value #name이 title인 내용을 title 변수로 받고
description = form["description"].value  #name이 description인 내용을 description 변수에 받음 

opened_file = open('data/'+title, 'w') #없을시 새로 생성됨
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title) #Location: 해주면 해당 주소로 url query string이 됨
print()