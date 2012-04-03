from __future__ import unicode_literals
from entries import Entries
from sys import argv
import re

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
 
def filter(markup):
  link = "REPL"
  #return re.sub("", , )
  return markup

def main():
  if len(argv) == 1:
    entries = Entries()
  else:
    date = argv[1]
    entries = Entries().written_on(date)
  markup = create_page(entries)
  markup = filter(markup)
  print markup

if __name__ == "__main__":
  main()