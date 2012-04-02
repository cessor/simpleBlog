import json
import time
import os
from datetime import date
from sys import argv

def write(): 
  title = argv[1]
  text = argv[2]
  author = "@cessor"
  timestamp = str(date.today())
  entry = { "author" : author, "timestamp" : timestamp, "title" : title, "text" : text }
  
  content = json.dumps(entry, indent=4)
  
  if "--save" in argv:
    save(timestamp, content)
  else:
    print content

def save(timestamp, content): 
  folder = "entries/"
  filename = "%s.json" % (timestamp) 
  path = os.path.join(folder, filename)
  with open(path, 'w') as file:
    file.write(content)

  def usage(): 
    print "Usage: %s title content [--save]" % argv[0]
    print "--save\tSaves an entry to entries/<today>.json"

if __name__ == "__main__":
  if len(argv) < 3:
    usage()
    exit()
  write()