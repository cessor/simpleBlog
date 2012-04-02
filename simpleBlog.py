from __future__ import unicode_literals
from json import load
from glob import glob
from datetime import datetime
from sys import argv

blog_name = "A Python Blog"

def read(path):
  with open(path, 'r') as file:
    return file.read()
  
def template(stencil, map):
  for field in map:
    stencil = stencil.replace("$%s$" % field, map[field])
  return stencil

def create_page(entries):
  markup_for_entries = create_markup_for_all(entries)
  view_data = { "blog_name" : blog_name, "content" : markup_for_entries }
  page_stencil = read("templates/page.template")
  return template(page_stencil, view_data)

def create_markup_for_all(entries):
  entry_stencil = read("templates/entry.template")
  templates = [template(entry_stencil, entry) for entry in entries]
  markup = ''.join(templates) # fast :) 
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

  def parse(self,date):
    return datetime.strptime(date, "%Y-%m-%d")

  def reformat(self,date):
    return datetime.strftime(date, "%A, %d. %B %Y")

  def __str__(self):
    return self.reformat(self.parse(self.date))

####################################################

def main():
  if len(argv) == 1:
    entries = Entries()
  else:
    date = argv[1]
    entries = Entries().written_on(date)
  print create_page(entries)

if __name__ == "__main__":
  main()