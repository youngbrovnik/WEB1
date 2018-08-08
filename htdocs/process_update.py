#!/usr/local/Cellar/python/3.7.0/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["desc"].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

os.rename('data/'+pageId, 'data/'+title)

print("Location: index.py?id="+title)    # HTML is following
print()                             # blank line, end of headers
