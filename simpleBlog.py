from __future__ import unicode_literals
from json import load
from glob import glob
from datetime import datetime

def read(path):
  content = ""
  with open(path, 'r') as file:
    content = file.read()
  return content

def template(stencil, map):
  for field in map:
    stencil = stencil.replace("$%s$" % field, map[field])
  return stencil

####################################################

blog_name = ".::a small blog"

def create_page():
  content = create_markup_for_all(Entries())
  view_data = { "blog_name" : blog_name, "content" : content }
  stencil = read("templates/page.template")
  return template(stencil, view_data)

def create_markup_for_all(entries):
  markup = ""
  stencil = read("templates/entry.template")
  for entry in entries:
    markup += template(stencil, entry)
  return markup

####################################################

class Entries:
  def read(self):
    entries = []
    for path in glob('./entries/*.json'):
      object = read_json_object(path)
      object["date"] = convert_date(object["timestamp"])
      entries.append(object)
    return entries

  def sort_by_date(self, entries):
    by_date = lambda object: object["timestamp"]
    entries.sort(key=by_date, reverse=True)

  def __iter__(self):
    entries = self.read()
    self.sort_by_date(entries)
    return entries.__iter__()

def read_json_object(path):
  return load(open(path, 'r'))

####################################################

def parse_date(date):
  return datetime.strptime(date, "%Y-%m-%d")

def reformat_date(date):
  return datetime.strftime(date, "%A, %d. %B %Y")

def convert_date(date):
  return reformat_date(parse_date(date))

####################################################

if __name__ == "__main__":
  print create_page()
