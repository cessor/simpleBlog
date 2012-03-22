from __future__ import unicode_literals
import json
from glob import glob

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

def write_html():
  data = read_json()
  #print data
  f = open('./index.html', 'w')
  f.write("<html><body>\n")

  for i in data:
    f.write("<h1>{0}</h1><p>{1}<br /><br />{2}</p>\n".format(*i))

  f.write("</body></html>")
  f.close()

write_html()
