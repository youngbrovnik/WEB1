#!/usr/local/Cellar/python/3.7.0/bin/python3

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["desc"].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

print("Location: index.py?id="+title)    # HTML is following
print()                             # blank line, end of headers
