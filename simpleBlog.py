from __future__ import unicode_literals
from json import load
from glob import glob
from datetime import datetime
from sys import argv

blog_name = ".::a small blog"

def read(path):
  content = ""
  with open(path, 'r') as file:
    content = file.read()
  return content

def template(stencil, map):
  for field in map:
    stencil = stencil.replace("$%s$" % field, map[field])
  return stencil

def create_page(entries):
  content = create_markup_for_all(entries)
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
      object = self.read_json_object(path)
      object["date"] = str(DateFormat(object["timestamp"]))
      entries.append(object)
    return entries

  def written_on(self, date):
    return [ entry for entry in self.__iter__() if entry["timestamp"] == date ]

  def sort_by_date(self, entries):
    by_date = lambda object: object["timestamp"]
    entries.sort(key=by_date, reverse=True)

  def __iter__(self):
    entries = self.read()
    self.sort_by_date(entries)
    return entries.__iter__()

  def read_json_object(self,path):
    return load(open(path, 'r'))

####################################################

class DateFormat:
  def __init__(self,date):
    self.date = date

  def convert(self, date):
    return self.reformat(self.parse(date))

  def parse(self,date):
    return datetime.strptime(date, "%Y-%m-%d")

  def reformat(self,date):
    return datetime.strftime(date, "%A, %d. %B %Y")

  def __str__(self):
    return self.convert(self.date)

####################################################

if __name__ == "__main__":
  if len(argv) == 1:
    entries = Entries()
  else:
    date = argv[1]
    entries = Entries().written_on(date)
  print create_page(entries)