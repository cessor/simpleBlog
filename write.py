import json
import time
from datetime import date
from sys import argv

def write(): 
  folder = "entries/"
  title = argv[1]
  text = argv[2]
  author = "@cessor"
  timestamp = str(date.today())
  entry = { "author" : author, "timestamp" : timestamp, "title" : title, "text" : text }
  
  content = json.dumps(entry, indent=4)
  
  if len(argv) == 4 and argv[3] == "--save":
    with open(("%s%s.json" % (folder,timestamp)), 'w') as f:
      f.write(content)
  else:
    print content
  

if __name__ == "__main__":
  if len(argv) < 3:
    print "Usage: %s title content [--save]" % argv[0]
    print "--save\tSaves an entry to entries/<today>.json"
    exit()
  write()
