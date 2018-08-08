#!/usr/local/Cellar/python/3.7.0/bin/python3
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = "Welcome"
    description = '''The World Wide Web(abbreviated WWW or the Web) is an information space where documents and other web resources are identified
        by Uniform Resource Locators(URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist
        Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed
        at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions
        starting in January 1991 and to the general public on the Internet in August 1991.'''

print('''
<!docutype html>
<html>
    <head>
        <title>My Home</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>
            <a href="index.py" id="active">WEB</a>
        </h1>
        <ol>
            {listStr}
        </ol>
        <a href="creat.py">creat</a>
        <form action="process_update.py" method="POST">
            <input type="hidden" name="pageId" value="{form_default_title}">
            <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
            <p><textarea name="desc" id="" cols="30" rows="4" placeholder="description">{form_deafault_dcscription}</textarea></p>
            <p><input type="submit"></p>
        </form>
    </body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_deafault_dcscription=description))

