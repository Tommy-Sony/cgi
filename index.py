#!C:\Users\SON\AppData\Local\Programs\Python\Python39\python.exe
# http://localhost:81/cgi-bin/index.py

print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer

sanitizer = html_sanitizer.Sanitizer() #클래스를 받아옴
form = cgi.FieldStorage() #모든 폼 input과 그에 해당하는 값을 form 변수로 리턴

if 'id' in form: #이 id는 form의 input으로 넘어온 값
    pageId = form["id"].value #pageId라는 고유값 생성
    description = open('data/'+pageId, 'r').read() #파일 읽기
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId) #update.py의 해당 쿼리스트링으로 보냄

    delete_action = '''
      <form action="process_delete.py" method="POST">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
      </form>
      '''.format(pageId)

else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''

#id가 없을경우 update 링크가 없음
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), update_link=update_link, delete_action=delete_action))

