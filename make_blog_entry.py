from __future__ import unicode_literals
from glob import glob
import json

blogname="<h1>.::a small blog</h1>"

html="<!DOCTYPE html>" + \
     "<html>" + \
     "<head>" + \
     "<meta charset='utf-8'>" + \
     "<title>simpleBlog</title>" + \
     "</head>" + \
     "<link rel='stylesheet' href='simple.css' type='text/css'>" + \
     "<body>\n"

html+=blogname

def read_json():
  storage = []

  for i in glob('./*.json'):
    f = open(i).read()
    data = json.loads(f)
    title = data["title"]
    text = data["text"]
    author = data["author"]
    timestamp = data["timestamp"]
    #print title, text, author, timestamp
    storage.append((title, text, author, timestamp))

  storage.sort(key=lambda timestamp: timestamp[3])
  print storage
  return storage

def create_html(html):
  data = read_json()
  #print data

  for index, item in enumerate(data):
    html+="<h2>"
    for i in item[3]:
        html+=i
    html+="</h2>"

    html+="<h3>"
    for i in item[0]:
        html+=i
    html+="</h3>"

    html+="<p>"
    for i in item[1]:
        html+=i

    html+="<br />author: "
    for i in item[2]:
        html+=i
    html+="</p>"

  html+="</body></html>"
  return html

f = open('./index.html', 'w')
f.write(create_html(html))
print html
f.close()
