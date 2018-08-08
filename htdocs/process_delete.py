#!/usr/local/Cellar/python/3.7.0/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

print("Location: index.py")    # HTML is following
print()                             # blank line, end of headers
