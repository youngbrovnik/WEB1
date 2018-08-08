#!/usr/local/Cellar/python/3.7.0/bin/python3
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = sanitizer.sanitize(form["id"].value)
    description = open('data/'+pageId, 'r').read()
    # description = description.replace('<', '&lt;')
    # description = description.replace('>', '&gt;')
    description = sanitizer.sanitize(description)
    update_link = '<a href = "update.py?id={}"> update </a>'.format(pageId)
    delete_action = '''
    <form action="process_delete.py" method="POST">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
    </form>
    '''.format(pageId)
else:
    title = pageId = "Welcome"
    description = '''The World Wide Web(abbreviated WWW or the Web) is an information space where documents and other web resources are identified
        by Uniform Resource Locators(URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist
        Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed
        at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions
        starting in January 1991 and to the general public on the Internet in August 1991.'''
    update_link=''
    delete_action=''

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
        {update_link}
        {delete_action}
        <h2>{title}</h2>
        <p>{desc}</p>
    </body>
</html>
'''.format(title=title, 
    desc=description, 
    listStr=view.getList(),
    update_link=update_link, 
    delete_action=delete_action))
