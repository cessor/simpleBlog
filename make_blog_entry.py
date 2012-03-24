from __future__ import unicode_literals
from glob import glob
import json

html="<!DOCTYPE html>" + \
     "<html>" + \
     "<head>" + \
     "<meta charset='utf-8'>" + \
     "<title>simpleBlog</title>" + \
     "</head>" + \
     "<link rel='stylesheet' href='simple.css' type='text/css'>" + \
     "<body>\n"

def read_json():
  storage = []

  for i in glob('./*.json'):
    f = open(i).read()
    data = json.loads(f)
    title = data["title"]
    text = data["text"]
    timestamp = data["timestamp"]
    #print title, text, timestamp
    storage.append((title, text, timestamp))

  storage.sort(key=lambda timestamp: timestamp[2])
  #print storage
  return storage

def create_html(html):
  data = read_json()
  #print data

  for index, item in enumerate(data):
    html+="<h1>"
    for i in item[0]:
        html+=i
    html+="</h1>"

    html+="<p>"
    for i in item[1]:
        html+=i

    for i in item[2]:
        html+="<br />"+i
    html+="</p>"

  html += "</body></html>"
  return html

f = open('./index.html', 'w')
f.write(create_html(html))
f.close()
