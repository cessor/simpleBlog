from __future__ import unicode_literals
from template import Template
from entries import Entries

blog_name = ".::a small blog"
  
def create_page(): 
  content = create_markup_for_all(Entries())
  view_data = { "blog_name" : blog_name, "content" : content }
  return Template('templates/page.template', view_data)
  
def create_markup_for_all(entries):
  markup = ""
  for entry in Entries():   
    markup += str(Template("templates/entry.template", entry)) 
  return markup

if __name__ == "__main__":
  print create_page()
  
# Remarks: 
   # Calling Template per loop does I/O and should be cached instead!
   # The String concatenation is also slow