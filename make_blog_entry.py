from __future__ import unicode_literals
from glob import glob
from sys import argv
from convert_date import convert_date
import json
blog_name = ".::a small blog"
debug = True

def read_json_object(path): 
  return json.load(open(path, 'r'))

def read_json():
  entries = []
  for path in glob('./*.json'):
    object = read_json_object(path)
    object["date"] = convert_date(object["timestamp"])
    entries.append(object)
  by_date = lambda object: object["date"]
  entries.sort(key=by_date, reverse=True)
  return entries
  
def read_all(path):
  content = ""
  with open(path, 'r') as file:
    content = file.read()
  return content
  
def create_html():
  page = read_all("page.template")
  entries = read_json()
  content = ""
  for entry in entries:
    content += create_entry(entry) # this is bad, use stringio instead
  view_data = { "blog_name" : blog_name, "text" : content }
  return template(page, view_data)

def create_entry(entry): # this is called per loop ant therefore inefficient, cache it!
  text = read_all("entry.template")
  return template(text, entry)
  
def template(text, map): 
  for field in map:
    text = text.replace("$%s$" % field, map[field]) # also slow
  return text

if __name__ == "__main__":
  print create_html()