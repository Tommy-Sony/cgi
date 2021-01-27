#!C:\Users\SON\AppData\Local\Programs\Python\Python39\python.exe
# http://localhost:81/cgi-bin/index.py

print("Content-Type: text/html")
print()
import cgi, os, view
 
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

#폼 액션을 process_update가 받음
#submit 버튼을 누를 때, process_update로 name을 넘기는것
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
  <form action="process_update.py" method="post">
      <input type="hidden" name="pageId" value="{form_default_title}">
      <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
      <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_default_description=description))

#input 타입이 hidden이면 사용자에게 노출되지 않음.